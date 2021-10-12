def isfloat(value):
    try:
        value = float(value)
        return True
    except ValueError:
        print('Кажется это не число')
    except:
        print('Что-то не так')
    return False

def num_check(inp_text=''):
    while True:
        current_input = input(inp_text)
        if isfloat(current_input):
            return current_input

def sign_check(inp_text):
    while True:
        current_input = input(inp_text)
        if current_input in ['+','-','*','/','**','//']:
            return current_input
        else:
            print('Что-то не так')

number_1 = num_check('Введите первое число: ')
number_2 = num_check('Теперь второе: ')
sign = sign_check('Какое действие выполнить? ')

try:
    answer = eval(number_1 + sign + number_2)
    print('Ответ:', number_1, sign, number_2, '=', answer)
except ZeroDivisionError:
    print('Ты попытался разделить на ноль')
except:
    print('Что-то не так')
