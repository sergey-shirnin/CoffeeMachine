class CoffeeMachine:
    def __init__(self):

        self.money_password = 'you555imma666'
        self.security = ''  # unlocked / 'locked' to restrict
        self.attempts = 3  # incorrect passwords tries for withdrawal
        self.money_show = 0  # 1 to show balance on main screen

        # machine power up q-ties  / #machine capacity
        self.water = 100;            self.top_up_water = 2000
        self.milk = 540;             self.top_up_milk = 1000
        self.beans = 20;             self.top_up_beans = 500
        self.cups = 5;               self.top_up_cups = 25
        self.money = 550

        # recipes >>>      format >> water, milk, beans, cup, price
        self.espresso =              [250,     0,    16,   1,    4]
        self.latte =                 [350,    75,    20,   1,    7]
        self.cappuccino =            [200,   100,    12,   1,    6]
        # copy and paste to add more recipes here

        self.prompts = {
'main':'''
    Select action:
        1 >  buy
        2 >  state
        3 >  fill
        >> Select to proceed with your choice
        4 >> take (authorized only)
        5 >> exit\n 
    ''',
'buy':'''
    What would you like now?
        1 >  espresso
        2 >  latte
        3 >  cappuccino
        >> Select to proceed with your choice
        4 >> back to main menu\n
    ''',
'fill_check':'''
    Fill up now? 
        1 >  proceed with filling
        2 >> back to drinks menu\n
    ''',
'take':'''
        > Enter service password or <0> back to main menu:\n
    ''',
'undefined':'''
        < not defined entry, try again... >
'''
        }

        self.state = 'power up'
        self.machine_state()

        self.state = 'main'

    def machine_state(self):
        if self.state == 'power up':
            print('''
        >Machine power up<
    Welcome to BWS Coffee Makers
        >>You make coffee
        >We make your day\n
    The coffee machine > READY''')

        if self.state == 'refill':
            print('''     
    The coffee machine got refilled''')

        print(f'''    > State:
        ---
        {self.water}ml of water
        {self.milk}ml of milk
        {self.beans}g of coffee beans
        {self.cups}ea of disposable cups
        ---''')

        if self.money_show == 1:
            print(f'        ${self.money} of money')

    def take(self):
        self.state = 'take'
        attempts = 0
        if self.security == 'locked':
            print('!Access denied.')
        else:
            while attempts < self.attempts:
                pw = self.user_inp()
                if pw == self.money_password:
                    if self.money == 0:
                        print(f'    !Nothing to withdraw\n'
                              f'    Balance   >> ${self.money}')
                        break
                    else:
                        print(f'    Withdrawn >> ${self.money}')
                        self.money = 0
                        print(f'    Balance   >> ${self.money}')
                        break
                if pw == '0':
                    break
                else:
                    attempts += 1
                    if attempts == 3:
                        print('!Access denied.')
                        self.security = 'locked'
                    else:
                        print('    Wrong password. Try again...')
        self.state = 'main'

    def fill(self):
        self.state = 'refill'
        def fill_go_through(what, limit, UoM,):
            while 555 < 666:
                try:
                    fill_ = int(input(f'Adding {what} >> specify your add in > {UoM} ({limit} to <FULL>): '))
                    if not limit < fill_:
                        return fill_
                    else:
                        print(f'    !can not be more than {limit}. Try again...')
                except ValueError:
                    print(self.prompts['undefined'])

        self.water += fill_go_through('water', self.top_up_water - self.water, 'ml')
        self.milk += fill_go_through('milk', self.top_up_milk - self.milk, 'ml')
        self.beans += fill_go_through('beans', self.top_up_beans - self.beans, 'gr')
        self.cups += fill_go_through('cups', self.top_up_cups - self.cups, 'pcs')


        self.machine_state()
        self.state = 'main'

    def check_(self, water, milk, beans, cups, price):
        self.state = 'fill_check'
        shortage = []
        if self.water >= water and self.milk >= milk and self.beans >= beans and self.cups >= cups:
            print("Making coffee in progress...Enjoy!")
            return True
        else:
            if not self.water >= water:
                shortage.append('water' + " > " + str(water - self.water) + 'ml' + ' to proceed')
            if not self.milk >= milk:
                shortage.append('milk' + " > " + str(milk - self.milk) + 'ml' + ' to proceed')
            if not self.beans >= beans:
                shortage.append('coffee beans' + " > " + str(beans - self.beans) + 'gr' + ' to proceed')
            if not self.cups >= cups:
                shortage.append('disposable cups' + " > " + str(cups - self.cups) + 'ea' + ' to proceed')
            print('!Resources insufficient >> Please add to proceed:')
            for i in shortage:
                print('>> ', i)

            while 555 < 666:
                filling = self.user_inp()
                if filling == '1':
                    self.fill()
                    self.state = 'buy'
                    break
                elif filling == '2':
                    self.state = 'buy'
                    break
                else:
                    print(self.prompts['undefined'])
            return False
        self.state = 'main'

    def buy_update(self, water, milk, beans, cups, price):
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += price

        self.machine_state()

    def user_input(self, selection):
        # if input() != 'buy' or input() != 'take':
        #     return input()
        # else:
        return input(self.messages[self.state])

    def buy(self):
        self.state = 'buy'
        while 555 < 666:
            choice = self.user_inp()
            if choice == '1':                              #espresso recipe unpack
                if self.check_(*(self.espresso)):
                    self.buy_update(*(self.espresso))
                    break
            elif choice == '2': #espresso recipe           #latte recipe unpack
                if self.check_(*(self.latte)):
                    self.buy_update(*(self.latte))
                    break
            elif choice == '3':                            #cappuccino recipe unpack
                if self.check_(*(self.cappuccino)):
                    self.buy_update(*(self.cappuccino))
                    break
            elif choice == '4':
                break
            else:
                print(self.prompts['undefined'])
        self.state = 'main'

    def user_inp(self):
        return input(self.prompts[self.state])

    def run(self):
        while 555 < 666:
            action = self.user_inp()
            if action == "1":
                self.buy()
            elif action == "2":
                self.machine_state()
            elif action == "3":
                self.fill()
            elif action == "4":
                self.take()
            elif action == "5":
                print('''
        >Machine power off<
                   ''')
                break
            else:
                print(self.prompts['undefined'])

BWS_maker = CoffeeMachine()
BWS_maker.run()