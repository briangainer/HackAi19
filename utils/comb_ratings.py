import pandas as pd

ratings = pd.read_csv('ratings.csv', delimiter=',')
recipes = pd.read_csv('clean_recipes.csv', delimiter=';')

joined = recipes.set_index('RecipeID').join(ratings.set_index('RecipeID'), how='inner')

joined.to_csv(path_or_buf='final_recipes.csv', index=False, header=True)
