# Execute your methods here.
from src import *
from Taxman import Taxman
from Calculator import Calculator
from CarCollector import CarCollector
from Character import Character
from Drawf import Drawf
from Fighter import Fighter
from Invoice import Invoice
import inspect
from pprint import pprint

def main():
    #ex1()
    # ex2()
    #ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    ex10()

def ex1():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    people_list.sort(key= lambda p:p['name'])
    print(people_list) 

def ex2():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    new_list = list(filter(lambda p: p['sex'] == 'male', people_list))
    print(new_list)

def transformEx3(person):
    retval = {
        'id':person['id'], 
        'name':person['name'],
        'weight_kg':person['weight_kg'],
        'height_meters':person['height_meters'],
        'bmi': round(person['weight_kg']/person['height_meters'] ** 2, 1)
    }
    return retval

def ex3():
    people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    new_list = list(map (transformEx3, people_list))
    print(new_list)

def ex4():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    new_list = [p['name'] for p in people_list if p['age'] >= 15]
    print(new_list)
    
def ex5():
    words = []
    sentence = "This is a test of the emergency broadcast system"
    words = sentence.split(" ")
    shortest = len(sentence)
    longest = len(words[0])
    for i in words:
        if (len(i) < shortest):
            shortest = len(i)
        if (len(i) > longest):
            longest = len(i)
    print(len(words))
    print(shortest)
    print(longest)


def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = Taxman(items, "10%")
    tm.calc_total()
    print(tm.get_total())
    
def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

def ex8():
     print(CarCollector.get_data())

def ex9():
    f = Fighter(18)
    d = Drawf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)

def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]
    new_list = []
    for x in data:
        index = x.split(", ")
        invoice = Invoice(index[0], index[1], index[2], index[3])
        new_list.append(invoice)

    print(new_list)

if __name__ == '__main__':
    main()
