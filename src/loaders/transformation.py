import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import PowerTransformer


class CustomLogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self) -> None:
        self._estimator = PowerTransformer()

    def fit(self, X, y=None):
        X_copy = np.copy(X) + 1
        self._estimator.fit(X_copy)
        return self

    def transform(self, X):
        X_copy = np.copy(X) + 1
        return self._estimator.transform(X_copy)

    def inverse_transform(self, X):
        X_reversed = self._estimator.inverse_transform(np.copy(X))

        return X_reversed - 1
