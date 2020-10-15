# Dictionaries are the mapping files in python
# It cannot have duplicated at the key part (Before :)
month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(month_Conversions["Mar"])

print(month_Conversions.get("Jan","Default value"))

print(month_Conversions.get("Sel","Default value"))
