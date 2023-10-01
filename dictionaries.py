#What?  A dictionary is an unordered collection of data in key-value pair format. Each key must be unique within a dictionary, and it is used to access its corresponding value.
#When?  A dictionary in Python is an unordered collection of data in a key-value pair format. Each key must be unique within a dictionary, and it is used to access its corresponding value.
#Why?  They provide fast lookups for items in the dictionary and have a similar structure to JSON), useful for working with data in this format.

monthConversions = {
    "Jan": "January",   #all keys in a dictionary must be unique
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "July": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
## Using our dictionary to retrieve values
# print(monthConversions["Nov"] )
# print(monthConversions.get("Dec"))
#when a value that doesn't map to any of the keys returns None, How to fix
print(monthConversions.get("Luv", "A valid 3 digit month was not entered"))  # the second value passsed