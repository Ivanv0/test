class Engine:
    def __init__(self):
        self.engine_start_up = False
    def start_engine(self):
        if self.engine_start_up:
            print('Engine already running')
        else:
            print('The engine is running now')
            self.engine_start_up = True
    def stop_engine(self):
        if not self.runnung:
            print('Engine already stopped')
        else:
            print('The engine is stopped now')
            self.engine_start_up = False

class Pedals(Engine):
    def __init__(self):
        super().__init__()
        self.gas_pedal = False
        self.brake_pedal = False
    def accelerate(self):
        if self.engine_start_up:
            print('Accelerate')
            self.gas_pedal = True
            self.brake_pedal = False
        else:
            print('You need to start_engine first')
    def stop(self):
        if self.brake_pedal:
            print('You already stoped')
        else:
            self.gas_pedal = False
            self.brake_pedal = True
            print('Stop')

class Car(Pedals):
    'My fantasy is over'
    def __init__(self):
        super().__init__()

methods_list=['methods']
def methods(ml=methods_list):
    print()
    print(*ml,sep=', ',end='\n\n')

car = Car()

print('\nSorry I was too lazy so here are the available methods.')
for i in dir(car):
    if i[0] != '_':
        methods_list.append(i)
methods()
print('Your Car named "car"\n')

while True:
    try:
        eval(input())
    except KeyboardInterrupt:
        break
    except:
        print('Error')
