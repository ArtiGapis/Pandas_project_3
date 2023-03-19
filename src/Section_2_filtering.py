'''----------Section 2: Filtering and Sorting----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd

'''Step 2. Import the dataset from this address.'''
url_2 = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'

'''Step 3. Assign it to a variable called euro12.'''
euro12 = pd.read_csv(url_2)

'''Step 4. Select only the Goal column.'''
# print(euro12['Goals'])

'''Step 5. How many team participated in the Euro2012?'''
# print(euro12['Team'].nunique())

'''Step 6. What is the number of columns in the dataset?'''
num_rows, num_cols = euro12.shape
# print(num_cols)

'''Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline'''
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
# print(discipline)

'''Step 8. Sort the teams by Red Cards, then to Yellow Cards'''
discipline = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
# print(discipline)

'''Step 9. Calculate the mean Yellow Cards given per Team'''
# print(euro12['Yellow Cards'].mean())

'''Step 10. Filter teams that scored more than 6 goals'''
# print(euro12[euro12['Goals'] > 6])

'''Step 11. Select the teams that start with G'''
# print(euro12[euro12['Team'].str.startswith('G')])

'''Step 12. Select the first 7 columns'''
# print(euro12.head(7))

'''Step 13. Select all columns except the last 3.'''
# print(euro12.iloc[:, :-3])

'''Step 14. Present only the Shooting Accuracy from England, Italy and Russia'''
three_teams = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]
# print(three_teams[['Team', 'Shooting Accuracy']])
