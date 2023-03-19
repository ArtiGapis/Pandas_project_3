'''----------Section 7: Visualization----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd
import matplotlib.pyplot as plt

'''Step 2. Import the dataset from this address.'''
'''Step 3. Assign it to a variable titanic'''

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv"
titanic = pd.read_csv(url)
# print(titanic)

'''Step 4. Set PassengerId as the index'''

titanic.set_index("PassengerId", inplace=True)
# print(titanic)

'''Step 5. Create a pie chart presenting the male/female proportion'''

gender_counts = titanic['Sex'].value_counts()
gender_counts.plot.pie(figsize=(5,5), autopct='%1.1f%%')
plt.title('Male/Female Proportion')
plt.ylabel('')
plt.show()

'''Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender'''

colors = {'male':'b', 'female':'r'}
titanic.plot.scatter(x='Age', y='Fare', c=titanic['Sex'].apply(lambda x: colors[x]), figsize=(8,6))
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Fare paid vs. Age by Gender')
plt.show()

'''Step 7. How many people survived?'''

survived_counts = titanic['Survived'].value_counts()
num_survived = survived_counts[1]
print("Survived:", num_survived)

'''Step 8. Create a histogram with the Fare payed'''

plt.figure(figsize=(8,6))
plt.hist(titanic['Fare'], bins=50)
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Histogram of Fare paid')
plt.show()