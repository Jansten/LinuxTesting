# lists_inventory_managment.py
# 2016-08-22, Michael Hannon
# A program straight from my CodeCademy course.  A multi=-dimensional list with inserts and sorting

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory["pocket"] = ["seashell","strange berry","lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] = inventory["gold"] + 50