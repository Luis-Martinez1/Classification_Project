import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split







def prep_telco(df):
    '''Takes in the telco churn dataframe as an argument and returns the dataframe
    with unnecessary columns dropped and empty values in the [total_charges] column
    changed from a blank space to a zero.
    '''
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'], inplace=True)
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    df.internet_service_type.fillna('No internet service', inplace = True)
    df['total_charges'] = df['total_charges'].astype(float)
    df['senior_citizen'].replace({0:'No', 1: 'Yes'}, inplace=True)
    df = df.set_index('customer_id')

    return df






def split_data(df, target):
    """
    This function takes in any DataFrame and a target variable as an argument 
    and returns train, validate, and test variables stratifying on the target variable.
    It returns these variables as DataFrames with a printout of their proportion to the original DataFrame.
    """
    train, validate_test = train_test_split(
        df, train_size=0.6, random_state=123, stratify=df[target]
    )
    validate, test = train_test_split(
        validate_test, train_size=0.5, random_state=123, stratify=validate_test[target]
    )
    print(f"train: {len(train)} ({round(len(train)/len(df), 2)*100}% of {len(df)})")
    print(
        f"validate: {len(validate)} ({round(len(validate)/len(df), 2)*100}% of {len(df)})"
    )
    print(f"test: {len(test)} ({round(len(test)/len(df), 2)*100}% of {len(df)})")

    return train, validate, test




def preprocess_telco(train_df, val_df, test_df):
    '''
    preprocess_telco will take in three pandas dataframes
    of an acquired and prepared telco data set that has also been split into train, validate, and test.
    
    output:
    encoded, ML-ready versions of train, validate, and test with 
    object type colummncs encoded in the one-hot fashion
    return: (pd.DataFrame, pd.DataFrame, pd.DataFrame)
    '''
     
    encoding_vars = []
    # loop through the columns to fill encoded_vars with appropriate datatype 
    for col in train_df.columns:
        if train_df[col].dtype == 'O':
            encoding_vars.append(col)
    # initialize an empty list to hold our encoded dataframes:
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        df_encoded_cats = pd.get_dummies(
            df[encoding_vars],
              drop_first=True).astype(int)
        encoded_dfs.append(pd.concat(
            [df,
            df_encoded_cats],
            axis=1).drop(columns=encoding_vars))
    return encoded_dfs
