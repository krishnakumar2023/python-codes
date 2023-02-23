# create the dictionary of cities and languages
city_languages = {
    "New York": ["English", "Spanish"],
    "Paris": ["French"],
    "Tokyo": ["Japanese"],
    "Bangkok": ["Thai", "English"],
    "Sydney": ["English"]
}

# a. Print all keys
print("Keys:")
for city in city_languages.keys():
    print(city)

# b. Print all the values
print("\nValues:")
for languages in city_languages.values():
    print(languages)

# c. If a value contains multiple languages, print the count
print("\nCounts:")
for languages in city_languages.values():
    if len(languages) > 1:
        print(f"{len(languages)} languages")
