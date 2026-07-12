class MLPredictor:
    def __init__(self):
        self.models = {}       # {task: RandomForestClassifier}
        self.encoders = {}     # {task: {col: LabelEncoder}}
        self.le_target = {}    # {task: LabelEncoder} pour la cible
        self.X_means = {}      # moyennes des features
        self.feature_names = {}
        self._is_trained = False

    

    def predict_all(self, features: dict) -> dict:
        predictions = {}
        for task, model in self.models.items():
            pred = model.predict([list(features.values())])[0]
            proba = max(model.predict_proba([list(features.values())])[0])
            label = self.le_target[task].inverse_transform([pred])[0]
            predictions[task] = {"label": label, "confidence": round(proba * 100, 1)}
        return predictions
