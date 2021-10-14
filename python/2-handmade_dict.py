# I didn't know what to do so I did that...

class mytable:
    'Dict based on lists'
    def __init__(self):
        self.keys = []
        self.value = []

    def find_key(self,key):
        if key in self.keys:
            return self.keys.index(key)
        else:
            return -1

    def check_value(self,key):
        return self.value[self.find_key(key)]

    def append(self,key,value):
        self.keys.append(key)
        self.value.append(value)

    def print_table(self):
        if len(self.keys) == 0:
            print("It's empty")
        else:
            for i in self.keys:
                print(i,' : ',self.check_value(i))

table=mytable()
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
            table.append(inp[0],int(inp[1]))
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
            try:
                edit = int(input('Enter a variable change: '))
                table.value[temp] += edit
            except ValueError:
                print('Error with int value')
    elif inp == 'print':
        table.print_table()
    elif inp == 'exit':
        break
    else:
        print('Something went wrong, try again')

print('\nGoodbye\n')
