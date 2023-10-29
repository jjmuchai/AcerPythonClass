# Data type

number = 25  # int
second = 56.78  # float
text = 'Hello there'  # str
ispythoninteresting = True  # bool

# store multiple values in a single variable
cars = ['toyota', 'nissan', 'vw']  # List - ordered and changeable
fruits = ('banana', 'orange', 'apple')  # Tuple- ordered and unchangeable
countries = {'Kenya', 'Tunisia', 'Algeria'}  # set - unordered and unchangeable
details = dict(firstname='James', age=34, course='web development', nationality='Kenyan')
# Dictionary - key-value pair

print(details['course'])
print(second)
print(text)
print(ispythoninteresting)
print(cars)
print(countries)
print(details)

# Determine a data type
print(type(number))
print(type(details))
print(type(countries))

# Typecasting - Converting one data to another
print(float(number))
print(int(second))
