class Person:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year
        
    @property
    def name(self):
        return self.__name
    
    @property
    def year(self):
        return self.__year
    
    def print_info(self):
        print(f"Name: {self.name}\tYear: {self.year}")
        

        