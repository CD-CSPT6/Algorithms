#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  for key in recipe.keys():
    if ingredients.keys() == recipe.keys():
      print(f"values are: {recipe.values()} and {ingredients.values()}")
      values = ingredients[key] // recipe[key] 
      print(f"value variable is {values}")  
      return values
    elif recipe.keys() != ingredients.keys():
      return 0



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))