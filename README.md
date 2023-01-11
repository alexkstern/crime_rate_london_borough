# Crime and Socioecological Factors in London Boroughs

This project aims to quantitatively explore the relationship between crime and socioecological factors in the 32 London boroughs using Random Forest Regression models. The following socioecological indicators will be examined:

- Population density
- Employment
- Income
- Social inequalities
- Wellbeing

## Data

The data used in this project was mainly acquired from the London Data Store. The data cleaning methods used to prepare the data for analysis can be found in the dataset_formation.ipynb notebook in the main repository. 

## Analysis
The statistical analysis used to answer our research question was Random Forest Regression. The Random Forest Regression model implementation can be found in the random_forest_1999_2021.ipynb and random_forest_2016_2018.ipynb files located in the Random Forest folder.
The main package used for the random Forest regression was scikit-learn. The work in the Random Forest folder is done by Alexander Stern, while the maps file is done by André Sebastián Cóndor.

## Visualizations
The choropleth visualisations used in this project are located in the maps folder.

## Conclusion
In conclusion, our analysis of crime rates in London using Random Forest regression models found that the most important borough attributes for predicting crime rates were population per hectare, consumer expenditure on pubs and wine bars, percentage of health workers, percentage of public administration and defence workers, and dwelling per hectare. We hope that this analysis will be useful for researchers, policy makers and the public for understanding the relationship between crime and socioecological factors in London.
