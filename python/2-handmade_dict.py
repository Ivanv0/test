# I didn't know what to do so I did that...

class Mytable:
    'Dict based on lists'
    def __init__(self):
        self.keys = []
        self.value = []

    def get_keys(self):
        return self.keys

    def get_value(self):
        return self.value

    def find_key(self,key):
        if key in self.keys:
            return self.keys.index(key)
        else:
            return -1

    def edit(self,key,edit):
        self.value[self.find_key(key)] += edit

    def value_by_key(self,key):
        return self.value[self.find_key(key)]

    def append(self,key,value):
        self.keys.append(key)
        self.value.append(value)

    def print_table(self):
        if len(self.keys) == 0:
            print("It's empty")
        else:
            for i in self.keys:
                print(i,' : ',self.value_by_key(i))

table=Mytable()
print('Welcome to my improvised dictionary based on lists')
print('''You can: [add] new, find out if the key [exist],
[find] value by key, [edit] exist value or [print] all table''')
print('If you want to stop this, enter [exit]')

while True:
    print('\nWrite down what you want to do\n')
    inp = input('> ')


    if inp == 'add':
        inp = input('Enter key and value: ').split()
        try:
            inp[1] = int(inp[1])
            index = table.find_key(inp[0])
            print(inp)
            if inp[0] in table.keys:
                print('You already have this key')
                if table.value[index] + inp[1] >= 0:
                    print('Do you want to edit it?\n[y]es [n]o')
                    if input() == 'y':
                        table.edit(inp[0],inp[1])
                        print('Now you have',table.value_by_key(inp[0]),'at',inp[0])
            else:
                table.append(inp[0],inp[1])
                print('Success')
        except ValueError:
            print('Error with int value')


    elif inp == 'exist' or inp == 'find':
        temp = table.find_key(input('Enter key: '))
        if temp == -1:
            print("This key doesn't exist")
        else:
            print("This key exist, it's value:", table.value[temp])
    elif inp == 'edit':
        temp = table.find_key(input('Enter key: '))
        if temp == -1:
            print("This key doesn't exist")
        else:
            print('You have',table.value[temp],'in this key')
            try:
                edit = int(input('Enter a variable change: '))
                if table.value[temp] + edit >= 0:
                    table.edit(temp,edit)
                else:
                    print("You don't have enough")
            except ValueError:
                print('Error with int value')
    elif inp == 'print':
        table.print_table()
    elif inp == 'exit':
        break
    else:
        print('Something went wrong, try again')

print('\nGoodbye\n')
