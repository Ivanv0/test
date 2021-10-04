def calc(v1,v2,act):
    'Это функция-калькулятор'
    print('Ответ: ',end='')
    if act == '+':
        print(v1+v2)
    elif act == '/':
        print(v1/v2)
    elif act == '-':
        print(v1-v2)
    elif act == '*':
        print(v1*v2)

def prov(type,inp=''):
    while True:
        pr=input(inp)
        if type=='chislo' and pr.isnumeric():
            return int(pr)
        elif type=='act' and pr in sp_act:
            return pr
        else: print('Что-то не так...')

sp_act=['+','-','*','/']

c1 = prov('chislo','Введите первое число: ')
c2 = prov('chislo','Теперь второе: ')
act = prov('act','Какое действие выполнить? ')
calc(c1,c2,act)
