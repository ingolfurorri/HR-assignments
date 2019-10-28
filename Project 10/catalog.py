class Catalog:
    def __init__(self, name = ''):
        '''Initialize the variables'''
        self.__name = name
        self.__collection = []

    def add(self, item):
        '''Adds item to a collection'''
        self.__collection.append((item._Item__name, item._Item__category))

    def remove(self, item):
        '''Removes item from a collection'''
        self.__collection.remove((item._Item__name, item._Item__category))

    def set_name(self, name):
        '''Updates the name of the collection'''
        self.__name = name

    def find_item_by_name(self, item_name):
        '''Checks if an item is in a collection'''
        for item in self.__collection:
            if item[0] == item_name:
                return 'Name: ' + item[0] + ', Category: ' + item[1]

    def clear(self):
        '''Clears the collection'''
        self.__collection = []

    def __str__(self):
        '''Prints information on collection'''
        return_string = 'Catalog ' + self.__name + ':'
        for item in self.__collection:
            return_string += '\n\tName: ' + item[0] + ', Category: ' + item[1]
        
        return return_string



class Item:
    def __init__(self, name = '', category = ''):
        '''Initialize the variables'''
        self.__name = name
        self.__category = category

    def set_name(self, name = ''):
        '''Updates the items' name'''
        self.__name = name

    def set_category(self, category = ''):
        '''Updates the category name'''
        self.__category = category

    def __str__(self):
        '''Prints information on collection'''
        return 'Name: ' + self.__name + ', Category: ' + self.__category