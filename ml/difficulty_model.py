# Simple TF-IDF + logistic regression pipeline to predict problem difficulty.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


class DifficultyModel:
def __init__(self):
self.vec = TfidfVectorizer(max_features=4000)
self.clf = LogisticRegression(max_iter=1000)


def train(self, statements, labels):
X = self.vec.fit_transform(statements)
self.clf.fit(X, labels)
joblib.dump({'vec': self.vec, 'clf': self.clf}, 'model.joblib')


def predict(self, statement):
X = self.vec.transform([statement])
return self.clf.predict_proba(X)[0]
