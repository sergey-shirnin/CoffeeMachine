class CoffeeMachine:
    def __init__(self):

        # machine power up q-ties  / # machine capacity
        self.water = 400;           self.top_up_water = 2000
        self.milk = 540;            self.top_up_milk = 750
        self.beans = 120;           self.top_up_beans = 250
        self.cups = 9;              self.top_up_cups = 25
        self.money = 550

        # recipes >>>      format >> water, milk, beans, cup, price
        self.espresso =              [250,     0,    16,   1,    4]
        self.latte =                 [350,    75,    20,   1,    7]
        self.cappuccino =            [200,   100,    12,   1,    6]

        self.prompts = {
'main': '''
    Select action:
        >>  buy
        >>  state
        >>  fill
        ---
        >>> take
        >   exit\n 
    ''',
'buy': '''
    What would you like now?
        1 > espresso
        2 > latte
        3 > cappuccino
    >> Select to proceed with your choice
    >> back > to main menu\n
    '''
        }
        self.state = 'main'

    def machine_state(self):
        print(f'''
    The coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.beans} of coffee beans
    {self.cups} of disposable cups
    ${self.money} of money''')

    def take(self):
        if self.money == 0:
            print(f'    !Nothing to withdraw\n'
                  f'    Balance   >> ${self.money}')
        else:
            print(f'    Withdrawn >> ${self.money}')
            self.money = 0
            print(f'    Balance   >> ${self.money}')


    def fill(self):
        # self.state = 'refill'
        def fill_go_through(what, limit, UoM):
            return int(input(f'Adding {what} >> specify your add in > {UoM} ({limit} to FULL): '))
        self.water += fill_go_through('water', self.top_up_water - self.water, 'ml')
        self.milk += fill_go_through('milk', self.top_up_milk - self.milk, 'ml')
        self.beans += fill_go_through('beans', self.top_up_beans - self.beans, 'g')
        self.cups += fill_go_through('cups', self.top_up_cups - self.cups, 'pcs')
        print('> The coffee machine got refilled')
        # self.state = 'main'

    def buy_update(self, water, milk, beans, cups, price):
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += price

    def buy(self):
        self.state = 'buy'
        choice = self.user_inp()
        if choice == '1':  # espresso recipe unpack
            if self.check_(*(self.espresso)):
                self.buy_update(*(self.espresso))
        elif choice == '2':  # latte recipe unpack
            if self.check_(*(self.latte)):
                self.buy_update(*(self.latte))
        elif choice == '3':  # cappuccino recipe unpack
            if self.check_(*(self.cappuccino)):
                self.buy_update(*(self.cappuccino))
        elif choice == 'back':
            pass
        self.state = 'main'

    def check_(self, water, milk, beans, cups, price):
        shortage = []
        if self.water >= water and self.milk >= milk and self.beans >= beans and self.cups >= cups:
            print("Making coffee in progress...Enjoy!")
            return True
        else:
            if not self.water >= water:
                shortage.append('water' + " > " + str(water - self.water) + 'ml' + ' to proceed')
            if not self.milk >= milk:
                shortage.append('milk' + "  > " + str(milk - self.milk) + 'ml' + ' to proceed')
            if not self.beans >= beans:
                shortage.append('beans' + " > " + str(beans - self.beans) + 'g' + ' to proceed')
            if not self.cups >= cups:
                shortage.append('cups' + "  > " + str(cups - self.cups) + 'pcs' + ' to proceed')
            print('!Resources insufficient >> Please add to proceed:')
            for i in shortage:
                print('>> ', i)
            return False

    def user_inp(self):
        return input(self.prompts[self.state])

    def run(self):
        while 555 < 666:
            action = self.user_inp()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.machine_state()
            elif action == "exit":
                print('''
        >Machine power off<
                   ''')
                break

BWS_maker = CoffeeMachine()
BWS_maker.run()
