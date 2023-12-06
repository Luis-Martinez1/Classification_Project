import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



def prep_telco(df):
    '''Takes in the telco churn dataframe as an argument and returns the dataframe
    with unnecessary columns dropped and empty values in the [total_charges] column
    changed from a blank space to a zero. The new column total_add_on_count is created by 
    summing each customers number of add-ons while also accounting for customers with no internet.
    It creates a new column tenure years which is the age of customer account starting with 0 for 
    customers with accounts up to 12 months old. 
    '''
    # A variable that represents all possible add-on services a customer can have
    columns_to_sum = ['online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']

    # New column that looks through each row and when a "yes" is found in columns_to_sum, it adds a 1
    df['total_add_on_count'] = df[columns_to_sum].apply(lambda row: sum(1 if value == 'Yes' else 0 if value == 'No' else 9 for value in row), axis=1)
    
    # change the number 54 to no internet service
    df['total_add_on_count'].replace({54:'No internet service'}, inplace=True)

    # Remove the add-on service columns
    df.drop(columns=df[columns_to_sum], inplace=True)

    # bin edges for each year 
    bins = [0, 12, 24, 36, 48, 60, 72, 84] 

    # Create labels for the bins (representing years)
    labels = ['0', '1', '2', '3', '4', '5', '6']

    # Bin the 'tenure' column
    df['tenure_years'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=False)

    # drop SQL joiner columns, phone service is replaced with phone service type, and tenure is replaced with tenure years
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'phone_service', 'tenure'], inplace=True)
    
    # Handle blank spaces in total_charges
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    
    # Replace empty spaces to match the rest of the columns
    df.internet_service_type.fillna('No internet service', inplace = True)
    
    #change the type of total_charges to float
    df['total_charges'] = df['total_charges'].astype(float)
    
    # Repalce bool to string for easier reading
    df['senior_citizen'].replace({0:'No', 1: 'Yes'}, inplace=True)
    
    # Rename column to combine multiple lines and phone service into one column
    df.rename(columns={'multiple_lines': 'phone_service_type'}, inplace=True)
    
    # 
    df['phone_service_type'].replace({'Yes':'Multiple lines', 'No': 'Single line'}, inplace=True)
    
    # change index to customer ID since it is a unique identifier and relevant to stakeholders
    df = df.set_index('customer_id')

    return df







def split_data(df, target):
    """
    This function takes in any DataFrame and a target variable as an argument 
    and returns train, validate, and test dataframes stratifying on the target variable.
    It returns three DataFrames with a printout of their proportion to the original DataFrame.
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
    This function takes three DataFrames as an argument 
    and returns train, validate, and test dataframes ready for machine learning.
    It returns DataFrames with all string values changed to represent a binary equivalent.
    '''
    # variable for all of our columns that should be in a numerical type
    columns_to_convert = ['gender', 'senior_citizen', 'partner', 'dependents', 'paperless_billing', 'churn', 'tenure_years', 'total_add_on_count']

    # variable for our features with string values
    encoding_vars = ['contract_type', 'internet_service_type', 'payment_type', 'phone_service_type']

    # Initialize a lsit of dataframes
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        # Replace certain string values with numerical values
        df.replace({"No": 0, "Yes": 1, "Male": 1, "Female": 0, "No internet service": 0}, inplace=True)

        # get dummy variables for columns with string values
        df_encoded_cats = pd.get_dummies(df[encoding_vars], drop_first=True).astype(int)
        
        # concatenate dummy columns to dataframe and drop the orginal columns 
        df = pd.concat([df, df_encoded_cats], axis=1).drop(columns=encoding_vars)
        
        # Convert specified columns to integer type
        df[columns_to_convert] = df[columns_to_convert].astype(int)
        
        # add changes to all three dataframes
        encoded_dfs.append(df)

    return encoded_dfs








def predicted_probabilities(y_pred_proba, y_pred, title='Predicted Probabilities vs Predicted Class'):
    """
    Plot a scatter plot of predicted probabilities vs predicted class labels.

    Parameters:
    - y_pred_proba: Array-like, predicted probabilities for the positive class.
    - y_pred: Array-like, predicted class labels (0 or 1).
    - title: String, title of the plot.

    Returns:
    None
    """
    fig = plt.figure(figsize=[5, 3])
    ax = fig.add_subplot()

    # scatter plot where x is the probabilities and y is the class (0, 1)
    ax.scatter(y_pred_proba, y_pred, alpha=0.05)

    plt.xlabel('Predicted Probabilities')
    plt.ylabel('Predicted Class (0 or 1)')
    plt.title(title)
    plt.show()













