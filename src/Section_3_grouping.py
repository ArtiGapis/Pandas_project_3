'''----------Section 3: Grouping----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd

'''Step 2. Import the dataset from this address.'''
url_3 = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'

'''Step 3. Assign it to a variable called drinks.'''
drinks = pd.read_csv(url_3)
# print(drinks)

'''Step 4. Which continent drinks more beer on average?'''
# print(drinks.groupby('continent')['beer_servings'].mean())

'''Step 5. For each continent print the statistics for wine consumption.'''
# print(drinks.groupby('continent')['wine_servings'].describe())

'''Step 6. Print the mean alcohol consumption per continent for every column'''
# print(drinks.groupby('continent').mean())

'''Step 7. Print the median alcohol consumption per continent for every column'''
# print(drinks.groupby('continent').median())

'''Step 8. Print the mean, min and max values for spirit consumption.(This time output a DataFrame)'''
# print(pd.DataFrame(drinks['spirit_servings'].agg(['mean', 'min', 'max'])))

