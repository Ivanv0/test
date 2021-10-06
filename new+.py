def isfloat(value,c):
    try:
        value=float(value)
        if not value:
            if c:
                del(sp_act[3])
                del(sp_act[4])
            print('Зачем тебе "0" в калькуляторе?')
        return True
    except ValueError:
        return False

def prov(type,inp='',c=0):
    while True:
        pr=input(inp)
        if type=='chislo' and isfloat(pr,c):
            return pr
        elif type=='act' and pr in sp_act:
            return pr
        elif pr=='/' or pr=='//': print('Вселенная так схлопнется')
        else: print('Что-то не так...')

sp_act=['+','-','*','/','**','//']

c1 = prov('chislo','Введите первое число: ')
c2 = prov('chislo','Теперь второе: ',1)
act = prov('act','Какое действие выполнить? ')
print('Ответ:',eval(c1+act+c2))
