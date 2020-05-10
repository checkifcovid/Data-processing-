from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import pandas as pd


def split_and_balance_with_SMOTE(X,y, test_size=0.25):
    """
    returns properly oversampled data

    Use as follows: `X_train, X_test, y_train, y_test = balance_data_with_SMOTE(X,y)`

    ---
    Documentation:
        https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html
        
    """

    keep_splitting = True
    n = 0

    while keep_splitting:
        # Split em
        X_train, X_test, y_train, y_test = train_test_split(X, y.values.ravel(), test_size=test_size, random_state=n)

        # Make sure there are minimum 2 of each class for y_train and y_test
        # If not, retry with another random_state
        all_val_counts = []
        for data in [y_train, y_test]:
            data_counts = pd.Series(data).value_counts()
            # Add to list of all
            all_val_counts.extend(data_counts.values)

        min_v_count = min(all_val_counts)
        if min_v_count <=1:
            print(f" * Samples aren't balanced enough for smote. Try splitting again. {n=}")
            n+=1
        else:
            keep_splitting = False
            print(f" * Done splitting. {n=}")


    # Adding the following parameters to allow flexibility for extra small data set
    k = min_v_count-1 if min_v_count <10 else 10
    os_ = SMOTE(random_state=0,k_neighbors=k)

    os_data_X, os_data_y=os_.fit_sample(X_train, y_train)
    X_train = pd.DataFrame(data=os_data_X, columns=X_train.columns)
    y_train = pd.DataFrame(data=os_data_y, columns=['y'])

    return X_train, X_test, y_train, y_test
