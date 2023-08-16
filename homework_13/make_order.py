import datetime

from homework_13.dish import Dish
from homework_13.menu_list import Menu_list


class Order:
    def __init__(self):
        self.items = []
        self.order_time = datetime.datetime.now()


    def add_item(self, name):
        if name == 'Pizza':
            self.items.append(name)
        elif name == 'Pasta':
            self.items.append(name)
        elif name == 'Salad':
            self.items.append(name)
        else:
            raise Exception('The dish is not in the menu')

    def display_order(self):
        for item in range(1):
            print(f'Order: {self.items}')
            print(f'Order time: {self.order_time}')


our_order = Order()
pizza = our_order.add_item('Pizza')
pasta = our_order.add_item('Pasta')
salad = our_order.add_item('Salad')
our_order.display_order()
our_order2 = Order()
pizza1 = our_order2.add_item('Pizza')
our_order2.display_order()
