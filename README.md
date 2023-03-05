# About Dataset
## Context
Due to rapid growth in field of cashless or digital transactions, credit cards are widely used in all around the world. Credit cards providers are issuing thousands of cards to their customers. Providers have to ensure all the credit card users should be genuine and real. Any mistake in issuing a card can be reason of financial crises. Due to rapid growth in cashless transaction, the chances of number of fraudulent transactions can also increasing. 

A Fraud transaction can be identified by analyzing various behaviors of credit card customers from previous transaction history datasets. If any deviation is noticed in spending behavior from available patterns, it is possibly of fraudulent transaction

The data is related to information about online payment fraud.

## Content
The data contains historical information about fraudulent transactions which can be used to detect fraud in online payments.

- train.csv: 6,351,193 rows and 10 columns

## Detailed Column Descriptions

| | Name | Type  | Desciption |
| ------------- | ------------- | ------------- | ------------- | 
| 1 | step | Integer | maps a unit of time in the real world. In this case, 1 step is 1 hour of time. |
| 2 | type | String | CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER |
| 3 | amount | Decimal | amount of the transaction in local currency. |
| 4 | nameOrig | String | customer who started the transaction.|
| 5 | oldbalanceOrig | Decimal | initial balance before the transaction. |
| 6 | newbalanceOrig | Decimal | customer's balance after the transaction. |
| 7 | nameDest | String | recipient ID of the transaction. |
| 8 | oldbalanceDest | Decimal | initial recipient balance before the transaction. |
| 9 | newbalanceDest | Decimal | recipient's balance after the transaction. |

**Output variable (desired target):**

10 - isFraud: fraud transaction (binary: "yes","no")

Missing Attribute Values: None


# Usage

Top-level directory layout

    
    ├── config                        # Config files (alternatively `configs`)
    ├── docs                          # Documentation files (alternatively `doc`)
    ├── scripts                       # Bash files (alternatively `script`)
    ├── src                           # Source files 
    (alternatively `lib` or `app`)
        ├── helpers                   # Contain several functions
        ├── loaders                   # Data transform/ Feature engineering / Custom Estimator
        ├── notebook                  # Notebook files 
            ├── BusinessUnderstanding.ipynb # BusinessBrainstom
            ├── DataUnderstanding.ipynb     # EDA data
            ├── DataPreparation.ipynb       # Data Intergration
            ├── Modeling.ipynb              # Modeling
            ├── 
    ├── tests                         # Automated tests (alternatively `spec` or `tests`)
    ├── LICENSE
    └── README.md


# Result:

#### Confusion Matrix
|  | Predict 0  | Predict 1 |
| ------------- | ------------- | ------------- |
| **Target 0** | 77221 | 62 |
| **Target 1** | 25 | 677 |





#### Metrics
|  | Model  | F-beta | AUC | Avg Precision |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 0  | XGBoost | 0.9396 | 0.9997 | 0.9376 |
| 1  | LightGBM | TODO | TODO | TODO |

