from catalog import Item
from catalog import Catalog

item1 = Item("12 Angry Men", "Drama")
item2 = Item("The Godfather", "Crime")
item3 = Item("Schindler's List", "Biography")
item4 = Item("Pulp Fiction", "Crime")
catalog = Catalog('Films')
catalog.add(item1)
catalog.add(item2)
catalog.add(item3)
catalog.add(item4)
#print(catalog)

catalog.clear()
assert catalog.__str__() == "Catalog Films:"
assert catalog.__str__() == "Catalog Films:\n\tName: 12 Angry Men, Category: Drama\n\tName: The Godfather, Category: Crime\n\tName: Schindler's List, Category: Biography\n\tName: Pulp Fiction, Category: Crime"
