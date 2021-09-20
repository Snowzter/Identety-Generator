import random
import json
age = random.randint(1,99)
name = random.choice(json.loads(open('names.json').read()))
country = random.choice(json.loads(open('countries.json').read()))


print (name)
print (age)
print (country)
