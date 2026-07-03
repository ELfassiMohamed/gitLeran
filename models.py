class features:
    def __init__(self):
        self.models = {}       # {task: RandomForestClassifier}
        self.encoders = {}     # {task: {col: LabelEncoder}}
        self.le_target = {}    # {task: LabelEncoder} pour la cible
        self.X_means = {}      # moyennes des features
        self.feature_names = {}
        self._is_trained = False

    
