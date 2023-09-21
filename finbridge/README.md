# Default Prediction

## Data Description

### train.pkl

Dataset for training.
The dataset contains aggregated profile features for each customer at each statement date. Features are anonymized and normalized, and fall into the following general categories:
- D_* = Delinquency variables
- S_* = Spend variables
- P_* = Payment variables
- B_* = Balance variables
- R_* = Risk variables

with the following features being categorical:
- B_30, B_38, D_114, D_116, D_117, D_120, D_126, D_63, D_64, D_66, D_68

The "target" is a binary variable for prediction:
- 0 = no default event
- 1 = default event


### test.pkl

Dataset for submission. Everything are the same as for train.pkl, except for the "target" column.


## Task Description

Based on the data provided:
- Train a machine learning model (the choice of a specific algorithm is yours):
    - Evaluate the quality of the final model (metric for evaluating - ROC AUC)
    - Analyze feature importance (identify the "strongest" features)
- Make a submission for the test file
    - Put the excel file with name "submission.xlsx" into the "data" directory
    - File should contain 2 columns:
        - "customer_ID" - Id for each test customer
        - "score" - probability of default event (probability of belonging to target == 1)


## Download Links

Both datasets you can download from [Datasets link](https://drive.google.com/drive/folders/16u1krMzSYqtcNNF_XeRWasmnS8B6jHU8?usp=sharing).


## Working Pipeline

- Fork this project
- Deal with project in your own Github account
- After finishing add us to the contributors and connect with us