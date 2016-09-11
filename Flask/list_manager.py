import pickle

file_spirits_all = open('./lists/spirits_all.lst','r')
spirit_list = [spirit.strip() for spirit in file_spirits_all]
file_spirits_all.close()
spirit_list = filter(None,sorted(spirit_list))
#print spirit_list

file_mixers_all = open('./lists/mixers_all.lst','r')
mixer_list = [mixer.strip() for mixer in file_mixers_all]
file_mixers_all.close()
mixer_list = filter(None,sorted(mixer_list))
#print mixer_list

file_garnishes_all = open('./lists/garnishes_all.lst','r')
garnish_list = [garnish.strip() for garnish in file_garnishes_all]
file_garnishes_all.close()
garnish_list = filter(None,sorted(garnish_list))
#print garnish_list

list_pourable_all=spirit_list + mixer_list
list_ingredients_all= spirit_list + mixer_list + garnish_list

def load_garnishes():
  file_garnishes_sel=open('./lists/garnishes_selected.lst','r')
  with file_garnishes_sel as input:
    read_garnish_list = pickle.load(input)
  file_garnishes_sel.close()
  return read_garnish_list

def save_garnishes(garn_list):
  file_garnishes_sel=open('./lists/garnishes_selected.lst','w')
  with file_garnishes_sel as output:
    pickle.dump(garn_list,output,-1)

def create_usable_cocktails():
  #Goes through all the selected ingredients and the list of cocktails to create a list of cocktails that can be made. Promptly stores the list.
  for cocktail_name, cocktail_ingredients in cocktail_list:
    for usable_ingredient in list_ingredient_all:
      match=0
      for ingredient in cocktail_ingredients:
        if ingredient is not 'Directions': #because 'Directions' will never be an ingredient
          if ingredient is usable_ingredient: 
            match = match +1
      if match == len(cocktail_ingredients)-1:
        print "add " + str(cocktail_name) + " to usable cocktails"

