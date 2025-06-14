class Restaurant():
    '''A simple model of a restaurant.'''

    def __init__(self, restaurant_name, restaurant_type, number_served=0):
        '''Initializes the restaurant's attributes.'''
        self.restuarant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = number_served

    def describe_restaurant(self):
        '''Describes the restaurant.'''
        print(f'{self.restuarant_name} is a {self.restaurant_type} restaurant which has served {self.number_served} people.')

    def open_restaurant(self):
        '''Prints an opening statement.'''
        print(f'{self.restuarant_name} is now open!')

    def set_number_served(self, new_number_served):
        '''Changes the number served value.'''
        if new_number_served >= self.number_served:
            self.number_served = new_number_served
        else:
            print('You cannot roll this value back!')

    def increment_number_served(self, increment):
        '''Increments the number of customers served'''
        if increment >= 0:
            self.number_served += increment
        else:
            print('Increment cannot be negative!')


class IceCreamStand(Restaurant):
    '''A simple model of an ice cream stand.'''

    def __init__(self, restaurant_name, restaurant_type, number_served=0):
        super().__init__(restaurant_name, restaurant_type, number_served)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def list_favors(self):
        print('These flavors are availabe:')
        for flavor in self.flavors:
            print(flavor)


baskin_robins = IceCreamStand('Baskin Robins', 'Ice Cream Stand', 500)
baskin_robins.open_restaurant()
baskin_robins.describe_restaurant()
baskin_robins.list_favors()
