class Taxman:

    def __init__(self, items, tax):
        self.items = items
        self.__tax = tax
        self.total = 0.00

    @property
    def tax(self):
        return self.__tax

    @tax.setter
    def tax(self, tax):
        self.__tax = tax

    def calc_total(self):
        for i in self.items:
            self.total += i['price']
        
        self.total += self.total * (int(self.__tax.split("%")[0]) / 100)

    def get_total(self):
        return self.total
    

