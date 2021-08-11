class CoffeeMachine:

    def __init__(self, **resources):
        self.resources = {
            'money': resources['money'],
            'water': resources['water'],
            'milk': resources['milk'],
            'coffee beans': resources['beans'],
            'cups': resources['cups']
        }
        self.recipes = {
            '1': {  #espresso
                'water': 250,
                'coffee beans': 16,
                'cups': 1,
                'money': -4
            },
            '2': {  # latte
                'water': 350,
                'milk': 75,
                'coffee beans': 20,
                'cups': 1,
                'money': -7
            },
            '3': {  # cappuccino
                'water': 200,
                'milk': 100,
                'coffee beans': 12,
                'cups': 1,
                'money': -6
            }
        }

    def get_status(self):
        print('The coffee machine has:\n\
                {} of water \n\
                {} of milk \n\
                {} of coffee beans \n\
                {} of disposable cups \n\
                {} of money'.format(self.resources['water'], self.resources['milk'],
                                    self.resources['coffee beans'], self.resources['cups'], self.resources['money']))
    def take(self):
        print('I gave you ${}'.format(self.resources['money']))
        self.resources['money'] = 0

    def buy(self):
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if not choice == 'back':
            ready = True
            lacking = []
            for resource in self.recipes[choice]:
                if self.recipes[choice][resource] > self.resources[resource]:
                    lacking.append(resource)
                    ready = False
            if ready:
                print('I have enough resources, making you a coffee!')
                for resource in self.recipes[choice]:
                    self.resources[resource] -= self.recipes[choice][resource]
            else:
                print('Sorry, not enough {}!'.format(", ".join(lacking)))


    def refill(self):
        for resource in self.resources:
            if not resource == 'money':
                if resource in ('water', 'milk'):
                    self.resources[resource] += int(input(f'Write how many ml of {resource} you want to add:'))
                elif resource == 'beans':
                    self.resources[resource] += int(input(f'Write how many grams of {resource} you want to add:'))
                else:
                    self.resources[resource] += int(input(f'Write how many {resource} you want to add:'))

    def run(self):
        while 555 < 666:
            action = input('Write action (buy, fill, take, remaining, exit):')
            if action == 'buy':
                self.buy()
            if action == 'fill':
                self.refill()
            if action == 'take':
                self.take()
            if action == 'remaining':
                self.get_status()
            if action == 'exit':
                break

my_machine1 = CoffeeMachine(money=550,
    water=100,
    milk=540,
    beans=2,
    cups=9
)

my_machine1.run()
