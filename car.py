class Car:
    '''A simple car. Khushal'''

    def __init__(self, make, model, year):
        '''init attributes for car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odo_reading = 0

    def get_descriptive_name(self):
        '''Return a formatted name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odo(self):
        '''Print a mileage statement.'''
        print(f"This car has {self.odo_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odo_reading:
            self.odo_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odo_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_range(self):
        '''Gets a range value for the car.'''
        if self.battery.battery_size == 40:
            print('The range of this car is 100 miles.')
        elif self.battery.battery_size == 60:
            print('The range of this car is 150 miles.')


class Battery():
    '''A simple attempt to model a battery.'''

    def __init__(self, battery_size=40):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement about the battery'''
        print(f'This car has a {self.battery_size}-kWh battery.')

    def upgrade_battery(self):
        '''Increases the size of the car battery.'''
        if self.battery_size == 40:
            self.battery_size = 60
        elif self.battery_size == 60:
            print('The battery is already upgraded!')


my_leaf = ElectricCar('nissan', 'leaf', '2024')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.get_range()
