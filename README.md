# About Dataset
## Context
Term deposits are a major source of income for a bank. A term deposit is a cash investment held at a financial institution. Your money is invested for an agreed rate of interest over a fixed amount of time, or term. The bank has various outreach plans to sell term deposits to their customers such as email marketing, advertisements, telephonic marketing, and digital marketing.

Telephonic marketing campaigns still remain one of the most effective way to reach out to people. However, they require huge investment as large call centers are hired to actually execute these campaigns. Hence, it is crucial to identify the customers most likely to convert beforehand so that they can be specifically targeted via call.

The data is related to direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe to a term deposit (variable y).

## Content
The data is related to the direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed by the customer or not. The data folder contains two datasets:-

- train.csv: 45,211 rows and 17 columns ordered by date (from May 2008 to November 2010)

- test.csv: 4521 rows and 17 columns with 10% of the examples (4521), randomly selected from train.csv

## Detailed Column Descriptions
Bank client data:

1 - age (numeric)
2 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student",
"blue-collar","self-employed","retired","technician","services")
3 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
4 - education (categorical: "unknown","secondary","primary","tertiary")
5 - default: has credit in default? (binary: "yes","no")
6 - balance: average yearly balance, in euros (numeric)
7 - housing: has housing loan? (binary: "yes","no")
8 - loan: has personal loan? (binary: "yes","no")

\# related with the last contact of the current campaign:

9 - contact: contact communication type (categorical: "unknown","telephone","cellular")
10 - day: last contact day of the month (numeric)
11 - month: last contact month of year (categorical: "jan", "feb", "mar", …, "nov", "dec")
12 - duration: last contact duration, in seconds (numeric)

\# other attributes:

13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
15 - previous: number of contacts performed before this campaign and for this client (numeric)
16 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

**Output variable (desired target):**
17 - y - has the client subscribed a term deposit? (binary: "yes","no")

Missing Attribute Values: None


# Usage

Top-level directory layout

    
    ├── config                        # Config files (alternatively `configs`)
    ├── docs                          # Documentation files (alternatively `doc`)
    ├── scripts                       # Bash files (alternatively `script`)
    ├── src                           # Source files 
    (alternatively `lib` or `app`)
        ├── notebook                  # Notebook files 
            ├── data_processing.ipynb # Preprocessing data
            ├── eda.ipynb             # EDA data
            ├── modeling.ipynb        # Modeling/Evaluateing 
    ├── tests                         # Automated tests (alternatively `spec` or `tests`)
    ├── LICENSE
    └── README.md


# Result:

| ID | Model  | Accuracy | AUC
| ------------- | ------------- | ------------- | ------------- |
| 0  | Logistic Regression | 0.901349 | 0.64 |
| 1  | SVM | 0.9079859 | 0.65 |
| 2  | KNN | 0.917054 | 0.71 |
| 3  | Decision Tree | 1.000000 | 1.00 |
| 4  | Random Forest | 1.000000 | 1.00 |
| 5  | Naive Bayes | 0.833002 | 0.68 |

