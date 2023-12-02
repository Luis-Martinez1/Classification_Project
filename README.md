# Classification_Project
 
# Project Description
 
This projects delves into the Telco Customer Churn data to identify key drivers influencing customer attrition. The goal of this project is to provide insights for the Telco company and poteintal solutions to enhance customer retention strategies through a combination of visualizations, statistical tests, and predictive modeling.

# Project Goals
 
* Discover drivers of churn for Telco customers.
* Use drivers to develop a supervised machine learning model that classifies customers as ethier churned or not churned.
* Customer churn occurs when a customer stops using Telco's telecomunications services. 
* This information could be used to further our understanding of what factors drive a customer to leave a telecomunications service provider and poteintaly provide solutions to prevent profitable customers from leaving.
 
# Initial Thoughts
 
My My initial hypothesis is that drivers of churn will be a combinations of factors related to customer service, communcaition services rendered, and charges to customers.
 
# The Plan
 
* Aquire the data from Codeup's Data Science Database Server.
 
* Prepare data
   * Remove unnecessary columns from existing data
       * payment_type_id
       * internet_service_type_id
       * contract_type_id
       
   * Change Index
       * customer_id will be used as the index 
      
   * Handle Null Values
       * total_charges will have zeros instead of blank spaces
       * internet_service_type null values will have "No internet service" to match other columns 
       
   * Change data tyoe
       * total_charges data type is changed to a float 
       * senior_citizen is changed from boolean to string for easier reading
       
   * Create Engineered columns from existing data
       * !!!!!enter new columns here when you combine multiple columns into one!!!!!!!!!
       * !!!!!enter new columns here when you combine multiple columns into one!!!!!!!!!
       * !!!!!enter new columns here when you combine multiple columns into one!!!!!!!!!

* Explore data in search of drivers of upsets
   * Answer the following initial questions
       * Is there a relationship between contract type and whether or not someone has churned?
       * How do different payment methods relate to churn?
       * Is there a correlation between the number of additional services rendered and churn?
       * Does customer tenure effect churn?
      
* Develop a Model to predict if a customer has churned or not
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Rated| True or False, The game's result is reflected in each player's rating|
|Winning Pieces| The color of pieces the winning player was moving|
|White Rating| Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess|
|Black Rating| Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess|
|Rating Difference| The difference in rating between the players in the game|
|Game Rating| The average rating of the two players in the game|
|Lower Rated White| True or False, The lower rated player is moving the white pieces|
|Opening Name| The name of the opening played in the game|
|Time Control Group| The amount of time allotted to each player to make their moves, **Standard** (60 min or more), **Rapid** (30 - 15 min), **Blitz** (5 - 3 min), or **Bullet** (2 or less), **Other** (any other time limit)|
|Upset (Target)| True or False, The lower rated player won the game|
|Additional Features|Encoded and values for categorical data and scaled versions continuous data|
 
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
 
# Recommendations
* To increase the skill intensity of a game add to the length of time players are able to consider their moves
* Based on the data longer time controls make it less likely for a less skilled player to beat a more skilled player