# Write a python program to create a dictionary which contains the name of cities as key
# and languages used in that city as value. The values may contain multiple languages, use
# a list to store multiple languages. Perform the following operations:
# a. Print all keys
# b. Print all the values
# c. if a value contains multiple languages, print the count

# create the dictionary of cities and languages
city_languages = {
    "New York": ["English", "Spanish"],
    "Paris": ["French"],
    "Tokyo": ["Japanese"],
    "Mumbai": ["Hindi", "Marathi"],
    "Sydney": ["English"],
    "Beijing": ["Mandarin", "Cantonese"]
}

# print all the keys
print("Cities:")
for city in city_languages.keys():
    print(city)

# print all the values
print("Languages:")
for languages in city_languages.values():
    print(languages)

# print the count of languages for each city
print("Language counts:")
for city, languages in city_languages.items():
    if len(languages) > 1:
        print(f"{city}: {len(languages)}")
