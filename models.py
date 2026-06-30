class RandomForestPredictor:
    def __init__(self):
        self.models = {}       # {task: RandomForestClassifier}
        self.encoders = {}     # {task: {col: LabelEncoder}}
        self.le_target = {}    # {task: LabelEncoder} pour la cible
        self.X_means = {}      # moyennes des features
        self.feature_names = {}
        self._is_trained = False

    def train(self):
        df = pd.read_excel("dataset_final.xlsx")
        df = df.drop_duplicates()
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].fillna(0)
            else:
                df[col] = df[col].fillna("Inconnu")

        for task, meta in TASK_META.items():
            self._train_one(df, task, meta)

        self._is_trained = True

    def _train_one(self, df, task, meta):
        # − Preparation des features −
        cat_cols = [c for c in CAT_COLS if c in df.columns]
        if task != "segment_taille" and "segment_taille" in df.columns:
            cat_cols = cat_cols + ["segment_taille"]

        for col in cat_cols:
            if col in df.columns and col != meta["target"]:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.encoders[task] = {col: le}

        # − Encodage de la cible −
        le_t = LabelEncoder()
        df[meta["target"] + "_enc"] = le_t.fit_transform(df[meta["target"]].astype(str))
        self.le_target[task] = le_t

        # − Separation X/y −
        to_drop = [meta["target"], meta["target"] + "_enc"] + meta.get("drop_extra", [])
        X = df.drop(columns=to_drop, errors="ignore").select_dtypes(include=[np.number])
        y = df[meta["target"] + "_enc"]

        # − SMOTE (sur-echantillonnage) si disponible −
        if HAS_SMOTE and len(y.unique()) > 1:
            X, y = SMOTE(random_state=42).fit_resample(X, y)

        # − Entrainement Random Forest −
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.20, random_state=42, stratify=y
        )
        rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)

        # − Evaluation −
        acc = (rf.predict(X_test) == y_test).mean()
        print(f"[ML] {task:<20} Accuracy={acc:.4f}  classes={list(le_t.classes_)}")
        self.models[task] = rf

    def predict_all(self, features: dict) -> dict:
        predictions = {}
        for task, model in self.models.items():
            pred = model.predict([list(features.values())])[0]
            proba = max(model.predict_proba([list(features.values())])[0])
            label = self.le_target[task].inverse_transform([pred])[0]
            predictions[task] = {"label": label, "confidence": round(proba * 100, 1)}
        return predictions
