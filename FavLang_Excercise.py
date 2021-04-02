data_scientist = { #A dictionary containing keys to store name age and years
    "Name": None,
    "Age": None,
    "Years": None
}

data_scientist["Name"] = input("Enter your name: ") #Inputs to place strings into data_scientist dictionary 
data_scientist["Age"] = input("Enter your age: ")
data_scientist["Years"] = input("Enter how long you've been coding: ")
print(data_scientist)

languages = input("Enter your first three programming languages (w/spaces): ") #Input for first three languages learned
lang_list = languages.split(" ") #splits each language inputted as a list 
lang_tuple = tuple(lang_list) #casting lang_list into a tuple (lang_tuple) 
data_scientist["first_lanugages"] = lang_tuple #adds a new key for favorite languages along with the list into the dictionary

favorites = input("Enter your three favorite programming languages: ") #input for favorite languages
fav_list = favorites.split(" ") #splits the inputs into a list 
data_scientist["favorite_languages"] = fav_list #adds new favorite languages key and returns the list

first_set = set(lang_list)#Casting lang_list as a set
fav_set = set(fav_list) #Casting fav_list as a set 
consistent_fav = first_set.intersection(fav_set) #Compares values of each list with .intersection() and returns commonalities between both
data_scientist["consistent_favorites"] = consistent_fav #adds new consistent key into dictionary 
print(data_scientist)
