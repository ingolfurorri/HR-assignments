class Catalog:
    def __init__(self, name):
        self.__name = name
        self.__collection = []

    def add(self, item):
        self.__collection.append((item._Item__name, item._Item__category))

    def remove(self, item):
        self.__collection.remove((item._Item__name, item._Item__category))

    def set_name(self, name):
        self.__name = name

    def find_item_by_name(self, item_name):
        for item in self.__collection:
            if item[0] == item_name:
                return 'Name: ' + item[0] + ', Category: ' + item[1]

    def clear(self):
        self.__collection = []

    def __str__(self):
        print('Catalog ' + self.__name + ':')
        if self.__collection != []:
            for i in range(len(self.__collection)):
                if(i == len(self.__collection)-1):
                    return '\t' + 'Name: ' + self.__collection[i][0] + ', Category: ' + self.__collection[i][1]
                print('\t' + 'Name: ' + self.__collection[i][0] + ', Category: ' + self.__collection[i][1])
        else:
            return ''

    
            



class Item:
    def __init__(self, name = '', category = ''):
        self.__name = name
        self.__category = category

    def set_name(self, name = ''):
        self.__name = name

    def set_category(self, category = ''):
        self.__category = category

    def __str__(self):
        return 'Name: ' + self.__name + ', Category: ' + self.__category