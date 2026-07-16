class features:
    def __init__(self):
        self.models = {}       # {task: RandomForestClassifier}
        self.encoders = {}     # {task: {col: LabelEncoder}}
        self.le_target = {}    # {task: LabelEncoder} pour la cible
        self.X_means = {}      # moyennes des features
        self.feature_names = {}

    

    def predict_all(self) :
        # write code here
        for col in cat_cols:
            if col in df.columns and col != meta["target"]:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.encoders[task] = {col: le
        return predictions
