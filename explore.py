import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import chi2_contingency
from scipy.stats import mannwhitneyu
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt








def visualize_churn_distribution(df):
    '''
    Trakes in a DataFrame and returns a pie plot visual of the 'churn' column
    distribution for the  data set. 
    '''
    # Count the number of customers who have churned and those who haven't
    churn_counts = df['churn'].value_counts()

    # Plot a pie chart
    labels = ['Not Churned', 'Churned']
    colors = ['lightsteelblue', 'sandybrown']

    plt.pie(churn_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Churned vs Not Churned Customers')
    plt.show()






def analyze_tenure_years(df, column, target_column):
    # Create a contingency table
    contingency_table = pd.crosstab(df[column], df[target_column])
    
    # Plot a stacked bar chart (count plot)
    plt.figure(figsize=(6, 3))
    sns.countplot(x=column, hue=target_column, data=df, palette='pastel')
    plt.title(f' Bar Chart - {column} vs {target_column}')
    plt.show()


    # Perform a chi-squared test
    chi2, p, _, _ = chi2_contingency(contingency_table)
    
    # Display the contingency table
    print("Contingency Table:")
    print(contingency_table)
    
    # Display the chi-squared test results
    print("\nChi-squared test:")
    print(f"Chi2 Statistic: {chi2}")
    print(f"P-value: {p}")


    



def analyze_contract_type(df, column, target_column):
    # Create a contingency table
    contingency_table = pd.crosstab(df[column], df[target_column])

    # Plot a stacked bar chart (count plot)
    plt.figure(figsize=(6, 3))
    sns.countplot(x=column, hue=target_column, data=df, palette='pastel')
    plt.title(f' Bar Chart - {column} vs {target_column}')
    plt.show()


    # Perform a chi-squared test
    chi2, p, _, _ = chi2_contingency(contingency_table)
    
    # Display the contingency table
    print("Contingency Table:")
    print(contingency_table)
    
    # Display the chi-squared test results
    print("\nChi-squared test:")
    print(f"Chi2 Statistic: {chi2}")
    print(f"P-value: {p}")






def analyze_monthly_charges(df, continuous_column, target_column):
    """
    Perform Mann-Whitney U test and visualize the relationship with a box plot.

    Parameters:
    - df: DataFrame
    - continuous_column: str, name of the continuous column
    - target_column: str, name of the target (categorical) column

    Returns:
    - printed bar chart, contingency table, and Mann-Whitney U test
    """
    # Separate data into two groups based on target_column
    data_churned = df[df['churn'] == 'Yes']['monthly_charges']
    data_not_churned = df[df['churn'] == 'No']['monthly_charges']

    # Perform Mann-Whitney U test
    stat, p_value = mannwhitneyu(data_churned, data_not_churned)

    # Visualize with a box plot
    plt.figure(figsize=(6, 3))
    sns.boxplot(x='churn', y='monthly_charges', data=df, palette='pastel')
    plt.title('Box Plot of monthly_charges by churn')
    plt.xlabel('churn')
    plt.ylabel('monthly_charges')
    plt.show()

    # Print Mann-Whitney U test results
    print(f'Mann-Whitney U statistic: {stat}')
    print(f'P-value: {p_value}')













def analyze_total_add_on_count(df, column, target_column):
    # Create a contingency table
    contingency_table = pd.crosstab(df[column], df[target_column])
    
    # Assuming df is your DataFrame and 'total_add_on_count' is the column you want to plot
    order = ['0', '1', '2', '3', '4', '5', '6', 'No internet service']

    # Convert the column to categorical with the specified order
    df['total_add_on_count'] = pd.Categorical(df['total_add_on_count'], categories=order, ordered=True)

    # Create the countplot
    contingency_table.plot.bar(stacked=False, color=['lightsteelblue', 'sandybrown'], figsize=(6, 3))
    plt.title(f'total_add_on_count vs. churn')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

    # Perform a chi-squared test
    chi2, p, _, _ = chi2_contingency(contingency_table)
    
    # Display the contingency table
    print("Contingency Table:")
    print(contingency_table)
    
    # Display the chi-squared test results
    print("\nChi-squared test:")
    print(f"Chi2 Statistic: {chi2}")
    print(f"P-value: {p}")



    


def analyze_payment_type(df, column, target_column):
    # Create a contingency table
    contingency_table = pd.crosstab(df[column], df[target_column])

    # Plot a stacked bar chart (count plot)
    plt.figure(figsize=(10, 3))
    sns.countplot(x=column, hue=target_column, data=df, palette='pastel')
    plt.title(f' Bar Chart - {column} vs {target_column}')
    plt.show()


    # Perform a chi-squared test
    chi2, p, _, _ = chi2_contingency(contingency_table)
    
    # Display the contingency table
    print("Contingency Table:")
    print(contingency_table)
    
    # Display the chi-squared test results
    print("\nChi-squared test:")
    print(f"Chi2 Statistic: {chi2}")
    print(f"P-value: {p}")









