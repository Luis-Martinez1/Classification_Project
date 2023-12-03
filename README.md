# Classification_Project
 
# Project Description
 
This projects delves into the Telco Customer Churn data to identify key drivers influencing customer attrition. The goal of this project is to provide insights for the Telco company and poteintal solutions to enhance customer retention strategies through a combination of visualizations, statistical tests, and predictive modeling.

# Project Goals
 
* Discover drivers of churn for Telco customers.
* Use drivers to develop a supervised machine learning model that classifies customers as ethier churned or not churned.
* Customer churn occurs when a customer stops using Telco's telecomunications services. 
* This information could be used to further our understanding of what factors drive a customer to leave a telecomunications service provider and poteintaly provide solutions to prevent profitable customers from leaving.
 
# Initial Thoughts
 
My My initial hypothesis is that drivers of churn will be a combinations of factors related to customer service, communcaition services provided, and customer charges.
 
# The Plan
 
* Aquire the data from Codeup's Data Science Database Server.
 
* Prepare data
   * Remove unnecessary columns from existing data
       * payment_type_id
       * internet_service_type_id
       * contract_type_id
       * phone_service
       
   * Change Index
       * customer_id will be used as the index 
      
   * Handle Null Values
       * total_charges will have zeros instead of blank spaces
       * internet_service_type null values will have "No internet service" to match other columns 
       
   * Change data tyoe
       * total_charges changed to a numerical type.
       * senior_citizen canged to non-numerical type.

       
   * Create Engineered columns from existing data
       * phone_service_type holds every possible value for each customer's phone status 
       * total_add_on_count counts the number of add-ons for each customer with internet and includes customers without internet 

* Explore data in search of drivers of churn
   * Answer the following initial questions
       * Is there a relationship between contract type and whether or not a customer has churned?
       * How do different payment methods relate to churn?
       * Is there a correlation between the number of add-on services rendered and churn?
       * Does customer tenure affect churn?
      
* Develop a Model to predict if a customer has churned or not
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|gender| Male or Female, The gender the customer identifies with|
|senior_citizen| Yes or No, Whether or not a customer is over the age of 60|
|partner| Yes or No, Whether or not a customer is married|
|dependents| Yes or No, Whether or not a customer has children|
|tenure| how many months a customer has been paying for Telco services|
|phone_service_type| Whether or not a customer has phone service and if it is multiple lines or single|
|paperless_billing| Yes, No, or No internet service, Whether or not a customer has children|
|monthly_charges| The charges per customer for each month of their tenure|
|total_charges| The aggaragate amount of monthly charges throughout a cutomer's tenure|
|churn (target)| Yes or No, The customer has left the company as their telecommuncations service provider|
|contract_type| Montly, One-Year, or Two-years, The type of contact type the customer has|
|internet_service_type|  None, Fiber, or DSL, The type of internet service the customer has|
|payment_type| Electronic check, Mailed check, Bank transfer, or Credit card, The type of payment a customer uses|
|contract_type|Encoded and values for categorical data and scaled versions continuous data|
|total_add_on_count| Encoded values for the number of add_ons a customer is rendered|

# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from Codeup DS Databse Server.
3) Put the data in the file containing the cloned repo.
4) Run notebook.
 
# Takeaways and Conclusions
* Upsets occur in 1/3 of games
* In games where the lower rated player moves first there is a 4% greater chance of an upset
* Games that are rated have a 3% higher chance of an upset
* Games with a "quick" time control (30 min or less) have about a 1 in 3 chance of upset
* Games with a "slow" time control (60 min or more) have about a 1 in 5 chance of upset
* The mean rating of players in a game is not a driver of upsets
* The difference in player rating is a driver of upsets
* A player's choice of opening is a driver of upsets, however its influence is complicated and I would need more time to discover what role it plays
* If I had more time, I would look through each add-on and see which specific add-on has a relationship with whether or not a customer has churned. 

 
# Recommendations
* Based on the data, customers should be signup up for longer contract types and provided the option to use automatic payemnts.
* Customers should be offered more add-on services and offered lower rates for longer contract types to prevent churning before 24 month tenure.
* If I had more time, I would look into the exact add-ons that are related to customer churn. 