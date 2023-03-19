'''----------Section 8: Creating Series and DataFrames----------'''

'''Step 1. Import the necessary libraries'''
import pandas as pd

'''Step 2. Create a data dictionary that looks like the DataFrame below'''
'''Step 3. Assign it to a variable called pokemon'''

pokemon = {
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
    'hp': [45, 39, 44, 45],
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'pokedex': ['yes', 'no', 'yes', 'no'],
    'type': ['grass', 'fire', 'water', 'bug']
}
# print(pokemon)

'''Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, 
    type, hp, evolution, pokedex'''

pokemon_df = pd.DataFrame(pokemon, columns=['name', 'type', 'hp', 'evolution', 'pokedex'])
# print(pokemon_df)

'''Step 5. Add another column called place, and insert what you have in mind.'''
pokemon_df['place'] = ['jungle', 'volcano', 'beach', 'meadow']
# print(pokemon_df)

'''Step 6. Present the type of each column'''
print(pokemon_df.dtypes)
