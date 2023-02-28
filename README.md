# About Dataset
## Context
Due to rapid growth in field of cashless or digital transactions, credit cards are widely used in all around the world. Credit cards providers are issuing thousands of cards to their customers. Providers have to ensure all the credit card users should be genuine and real. Any mistake in issuing a card can be reason of financial crises. Due to rapid growth in cashless transaction, the chances of number of fraudulent transactions can also increasing. 

A Fraud transaction can be identified by analyzing various behaviors of credit card customers from previous transaction history datasets. If any deviation is noticed in spending behavior from available patterns, it is possibly of fraudulent transaction

The data is related to information about online payment fraud.

## Content
The data contains historical information about fraudulent transactions which can be used to detect fraud in online payments.

- train.csv:

- test.csv:
## Detailed Column Descriptions
1 - step: represents a unit of time where 1 step equals 1 hour (numeric)
2 - type: type of online transaction (categorical: "CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT")
3 - amount: the amount of the transaction (numeric)
4 - oldbalanceOrig: balance before the transaction (numeric)
5 - newbalanceOrig: balance after the transaction (numeric)
6 - oldbalanceDest: initial balance of recipient before the transaction (numeric)
7 - newbalanceDest: the new balance of recipient after the transaction (numeric)

**Output variable (desired target):**
8 - isFraud: fraud transaction (binary: "yes","no")

Missing Attribute Values: None


# Usage

Top-level directory layout

    
    ├── config                        # Config files (alternatively `configs`)
    ├── docs                          # Documentation files (alternatively `doc`)
    ├── scripts                       # Bash files (alternatively `script`)
    ├── src                           # Source files 
    (alternatively `lib` or `app`)
        ├── notebook                  # Notebook files 
            ├── BusinessUnderstanding.ipynb # BusinessBrainstom
            ├── DataUnderstanding.ipynb     # EDA data
            ├── 
    ├── tests                         # Automated tests (alternatively `spec` or `tests`)
    ├── LICENSE
    └── README.md


# Result:

|  | Model  | F-beta | AUC | Avg Precision |
| ------------- | ------------- | ------------- | ------------- | ------------- | 
| 0  |  |  |  |
| 1  |  |  |  |
| 2  |  |  |  |
| 3  |  |  |  |
| 4  |  |  |  |
| 5  |  |  |  |

