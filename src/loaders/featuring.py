from typing import List, Union

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CumTransactionCustomerinStep(BaseEstimator, TransformerMixin):
    """
    Number of transaction of customer in each step
    """

    def __init__(self, step, customer_ids) -> None:
        self.step = step
        self.customer_ids = customer_ids

    def fit(self, X, y=None):
        """ """
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        cum_transaction_in_hour = "Cum" + self.customer_ids + "TransactionInStep"
        X[cum_transaction_in_hour] = X.groupby([self.step, self.customer_ids])[
            [self.customer_ids]
        ].transform("count")
        # print(X) # check working
        return X[cum_transaction_in_hour].to_numpy().reshape(-1, 1)


class AggAmountTransactionofCustomer(BaseEstimator, TransformerMixin):
    """
    Agg amout transaction of customer
    """

    def __init__(self, amount, customer_ids, aggregation="mean"):
        self.amount = amount
        self.customer_ids = customer_ids
        self.aggregation = aggregation

    def fit(self, X, y=None):
        """ """
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        agg_amount_transaction_of_customer = (
            "Agg" + self.aggregation + "TransactionOf" + self.customer_ids
        )
        X[agg_amount_transaction_of_customer] = X.groupby([self.customer_ids])[
            [self.amount]
        ].transform(self.aggregation)
        # print(X)  # check working

        return X[agg_amount_transaction_of_customer].to_numpy().reshape(-1, 1)


class CountFrequency(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        variables: Union[None, int, str, List[Union[str, int]]],
        to_prop: bool = False,
    ) -> None:
        self.variables = variables
        self.to_prop = to_prop

    def fit(self, X, y=None):
        """ """
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        fetures_name = []
        for variable in self.variables:
            count_freq = "FrequenceOf" + variable
            fetures_name.append(count_freq)
            if self.to_prop:
                X[count_freq] = X[variable].map(
                    (X[variable].value_counts() / float(len(X))).to_dict()
                )
            else:
                X[count_freq] = X[variable].map(X[variable].value_counts().to_dict())
        return X[fetures_name].to_numpy()
