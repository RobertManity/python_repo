import os
import time
from Coffee_Operator import CoffeeOperator

class Coffee(CoffeeOperator):
    def __init__(self):
        dict_coffee = CoffeeOperator.get_dict(CoffeeOperator)
        quantity = CoffeeOperator.get_quantity(CoffeeOperator)
        power_status = CoffeeOperator.get_power(CoffeeOperator)

        self.power_status = True       
        print('Welcome User')
        while self.power_status == True:
            self.display(len(self.quantity))
            if self.quantity == [0] or len(self.quantity) == 0:
                print("No Coffee. Turning off")
                self.power_status = False
                break
            else:
                user_input = int(input('Your choice: ')) - 1
                if 0 <= user_input < len(self.quantity):
                    if self.available(user_input) == True:
                        print('Coffee is getting ready, Please pay the cost')
                    self.coffee_cost(user_input)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Invalid input. There is no coffee at option {}'.format(user_input+1))

    def available(self,user_input):
        if self.quantity[user_input] > 0:
            self.quantity[user_input] -= 1
            return True