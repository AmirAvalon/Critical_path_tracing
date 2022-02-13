import random
import re

tasks = dict()  # contains all the tasks
branches = list()
output = dict()
gates = dict()


def read_task():
    global tasks, gates
    counter = 0
    file = open('c17.txt') 
    for line in file:  # slide the file line by line

        if '#' in line or line == '\n':
            continue

        if re.match('INPUT.*$', line):
            singleElement = re.findall(r'\w*\((\d*)\)', line)  # split a line in sub parts
            tasks['input_' + str(singleElement[0])] = dict()
            tasks['input_' + str(singleElement[0])]['name'] = singleElement[0]
            tasks['input_' + str(singleElement[0])]['value'] = random.randint(0, 1)
            tasks['input_' + str(singleElement[0])]['isCritical'] = False
            tasks['input_' + str(singleElement[0])]['branch'] = False
            tasks['input_' + str(singleElement[0])]['subset'] = list()
            tasks['input_' + str(singleElement[0])]['randomly'] = True
        if re.match('OUTPUT.*$', line):
            singleElement = re.findall(r'\w*\((\d*)\)', line)  # split a line in sub parts
            single_value = re.findall(r'\d*', line)  # split a line in sub parts
            output['output' + str(singleElement[0])] = dict()
            output['output' + str(singleElement[0])]['name'] = singleElement[0]
            output['output' + str(singleElement[0])]['value'] = single_value[0]
        if '=' in line:
            input_element = (line.split(' '))
            name_gate = input_element[2].split('(')
            text = line.split('=')
            input_ = re.findall('[0-9]{1,3}', text[1])
            result_ = re.findall('[0-9]{1,3}', text[0])
            tasks['input_' + str(input_element[0])] = dict()
            tasks['input_' + str(input_element[0])]['name'] = input_element[0]
            tasks['input_' + str(input_element[0])]['value'] = 0
            tasks['input_' + str(input_element[0])]['isCritical'] = False
            tasks['input_' + str(input_element[0])]['branch'] = False
            tasks['input_' + str(input_element[0])]['subset'] = list()
            tasks['input_' + str(input_element[0])]['randomly'] = False
            gates['gate_' + str(name_gate[0]) + str(counter)] = dict()
            gates['gate_' + str(name_gate[0]) + str(counter)]['name'] = name_gate[0]
            gates['gate_' + str(name_gate[0]) + str(counter)]['input'] = input_
            gates['gate_' + str(name_gate[0]) + str(counter)]['result'] = result_
            counter += 1


def AND(a, b, d='', c='', e='', f='', g='', h='', i=''):
    if i != '':
        if a and b and d and c and e and f and g and h and i:
            return 1
        else:
            return 0

    if h != '':
        if a and b and d and c and e and f and g and h:
            return 1
        else:
            return 0
    
    if g != '':
        if a and b and d and c and e and f and g:
            return 1
        else:
            return 0

    if f != '':
        if a and b and d and c and e and f:
            return 1
        else:
            return 0

    if e != '':
        if a and b and d and c and e:
            return 1
        else:
            return 0

    if c != '':
        if a and b and d and c:
            return 1
        else:
            return 0
    if d != '':
        if a and b and d:
            return 1
        else:
            return 0
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def NAND(a, b, d='', c=''):
    if c != '':
        if a and b and d and c == 1:
            return 0
        else:
            return 1
    if d != '':
        if a and b and d == 1:
            return 0
        else:
            return 1
    if a and b == 1:
        return 0
    else:
        return 1


def OR(a, b, d='', c='', e=''):
    if e != '':
        if a == 1 or b == 1 or d == 1 or c == 1 or e == 1:
            return 1
        else:
            return 0
    if c != '':
        if a == 1 or b == 1 or d == 1 or c == 1:
            return 1
        else:
            return 0
    if d != '':
        if a == 1 or b == 1 or d == 1:
            return 1
        else:
            return 0
    if a == 1 or b == 1:
        return 1
    else:
        return 0


def XOR(a, b):
    return a ^ b


def NOT(a):
    if not a:
        return 1
    return 0


def NOR(a, b):
    if (a == 0) and (b == 0):
        return 1
    elif (a == 0) and (b == 1):
        return 0
    elif (a == 1) and (b == 0):
        return 0
    elif (a == 1) and (b == 1):
        return 0


def update_value(value, name_gate):
    
    input_a = 'input_' + str(name_gate[0])
    tasks[input_a]['value'] = value


def subset_check(gate, *args):
    
    input_a = 'input_' + str(gate[0])
    for arg in args:
        tasks[input_a]['subset'].append(arg)


def critical_path(str_gates, list_task):
    

    for name_input in list_task:
        if name_input in branches:
           
            tasks[name_input]['branch'] = True
            try:
                
                for i in tasks[name_input]['subset']:
                    tasks['input_' + i]['isCritical'] = False
            finally:
                pass

    for i in list_task:
        branches.append(i)

    if str_gates == 'NAND':
        if len(list_task) == 2:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            if input_1 == 1 and input_2 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1:
                tasks[list_task[0]]['isCritical'] = True
#new
        if len(list_task) == 3:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            if input_1 == 1 and input_2 == 1 and input_3 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 1:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 0:
                tasks[list_task[2]]['isCritical'] = True

        if len(list_task) == 4:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            input_4 = tasks[list_task[3]]['value']
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
                tasks[list_task[3]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 1 and input_4 == 1:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 1 and input_4 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 0 and input_4 == 1:
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 0:
                tasks[list_task[3]]['isCritical'] = True

#new

    if str_gates == 'AND':
        if len(list_task) == 2:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            if input_1 == 1 and input_2 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1:
                tasks[list_task[0]]['isCritical'] = True

        if len(list_task) == 4:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            input_4 = tasks[list_task[3]]['value']
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
                tasks[list_task[3]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 1 and input_4 == 1:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 1 and input_4 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 0 and input_4 == 1:
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 0:
                tasks[list_task[3]]['isCritical'] = True

        if len(list_task) == 5:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            input_4 = tasks[list_task[3]]['value']
            input_5 = tasks[list_task[4]]['value']
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
                tasks[list_task[3]]['isCritical'] = True
                tasks[list_task[4]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 1 and input_4 == 1 and input_5 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 0 and input_4 == 1 and input_5 == 1:
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 0 and input_5 == 1:
                tasks[list_task[3]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 0:
                tasks[list_task[4]]['isCritical'] = True
#new
        if len(list_task) == 8:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            input_4 = tasks[list_task[3]]['value']
            input_5 = tasks[list_task[4]]['value']
            input_6 = tasks[list_task[5]]['value']
            input_7 = tasks[list_task[6]]['value']
            input_8 = tasks[list_task[7]]['value']
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
                tasks[list_task[3]]['isCritical'] = True
                tasks[list_task[4]]['isCritical'] = True
                tasks[list_task[5]]['isCritical'] = True
                tasks[list_task[6]]['isCritical'] = True
                tasks[list_task[7]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 0 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1:
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 0 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1:
                tasks[list_task[3]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 0 and input_6 == 1 and input_7 == 1 and input_8 == 1:
                tasks[list_task[4]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 0 and input_7 == 1 and input_8 == 1:
                tasks[list_task[5]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 0 and input_8 == 1:
                tasks[list_task[6]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 0:
                tasks[list_task[7]]['isCritical'] = True    

        if len(list_task) == 9:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            input_4 = tasks[list_task[3]]['value']
            input_5 = tasks[list_task[4]]['value']
            input_6 = tasks[list_task[5]]['value']
            input_7 = tasks[list_task[6]]['value']
            input_8 = tasks[list_task[7]]['value']
            input_9 = tasks[list_task[8]]['value']
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
                tasks[list_task[3]]['isCritical'] = True
                tasks[list_task[4]]['isCritical'] = True
                tasks[list_task[5]]['isCritical'] = True
                tasks[list_task[6]]['isCritical'] = True
                tasks[list_task[7]]['isCritical'] = True
                tasks[list_task[8]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 0 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 0 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[3]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 0 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[4]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 0 and input_7 == 1 and input_8 == 1 and input_9 == 1:
                tasks[list_task[5]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 0 and input_8 == 1 and input_9 == 1:
                tasks[list_task[6]]['isCritical'] = True
            if input_1 == 1 and input_2 == 1 and input_3 == 1 and input_4 == 1 and input_5 == 1 and input_6 == 1 and input_7 == 1 and input_8 == 1 and input_9 == 0:
                tasks[list_task[7]]['isCritical'] = True    
        
#new
    if str_gates == 'XOR':
        if len(list_task) == 2:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            if input_1 == 0 and input_2 == 0:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True

    if str_gates == 'OR':
         if len(list_task) == 2:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            if input_1 == 0 and input_2 == 0:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0:
                tasks[list_task[0]]['isCritical'] = True
    if len(list_task) == 4:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            input_3 = tasks[list_task[2]]['value']
            input_4 = tasks[list_task[3]]['value']
            if input_1 == 0 and input_2 == 0 and input_3 == 0 and input_4 == 0:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
                tasks[list_task[2]]['isCritical'] = True
                tasks[list_task[3]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0 and input_3 == 0 and input_4 == 0:
                tasks[list_task[0]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1 and input_3 == 0 and input_4 == 0:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 0 and input_2 == 0 and input_3 == 1 and input_4 == 0:
                tasks[list_task[2]]['isCritical'] = True
            if input_1 == 0 and input_2 == 0 and input_3 == 0 and input_4 == 1:
                tasks[list_task[3]]['isCritical'] = True

    if str_gates == 'NOT':
        if len(list_task) == 1:
            input_1 = tasks[list_task[0]]['value']
            tasks[list_task[0]]['isCritical'] = True
#new    
    if str_gates == 'NOR':
         if len(list_task) == 2:
            input_1 = tasks[list_task[0]]['value']
            input_2 = tasks[list_task[1]]['value']
            if input_1 == 0 and input_2 == 0:
                tasks[list_task[0]]['isCritical'] = True
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 0 and input_2 == 1:
                tasks[list_task[1]]['isCritical'] = True
            if input_1 == 1 and input_2 == 0:
                tasks[list_task[0]]['isCritical'] = True 
 #new               
def c17():
    read_task()

    for gate in gates:
        if str(gates[gate]['name']) == 'NAND':
            list_input = list()
            for i in range(len(gates[gate]['input'])):
                list_input.append('input_' + str(gates[gate]['input'][i]))
        
            if len(list_input) == 2:
                value = NAND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'])
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)
#new                
            if len(list_input) == 4:
                value = NAND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                tasks[list_input[2]]['value'], tasks[list_input[3]]['value'])
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                tasks[list_input[2]]['name'], tasks[list_input[3]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)
            if len(list_input) == 3:
                value = NAND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                tasks[list_input[2]]['value'])
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                tasks[list_input[2]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)
#new
        if str(gates[gate]['name']) == 'AND':
            list_input = list()
            for i in range(len(gates[gate]['input'])):
                list_input.append('input_' + str(gates[gate]['input'][i]))

            if len(list_input) == 2:
                value = AND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

            if len(list_input) == 4:
                value = AND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                            tasks[list_input[2]]['value'], tasks[list_input[3]]['value'])
               
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                             tasks[list_input[2]]['name'], tasks[list_input[3]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

            if len(list_input) == 5:
                value = AND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                            tasks[list_input[2]]['value'], tasks[list_input[3]]['value'],
                            tasks[list_input[4]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                             tasks[list_input[2]]['name'], tasks[list_input[3]]['name'], tasks[list_input[4]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)
#new
            if len(list_input) == 8:
                value = AND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                            tasks[list_input[2]]['value'], tasks[list_input[3]]['value'],
                            tasks[list_input[4]]['value'], tasks[list_input[5]]['value'],
                            tasks[list_input[6]]['value'], tasks[list_input[7]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                             tasks[list_input[2]]['name'], tasks[list_input[3]]['name'], tasks[list_input[4]]['name'],
                             tasks[list_input[5]]['name'], tasks[list_input[6]]['name'], tasks[list_input[7]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

            if len(list_input) == 9:
                value = AND(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                            tasks[list_input[2]]['value'], tasks[list_input[3]]['value'],
                            tasks[list_input[4]]['value'], tasks[list_input[5]]['value'],
                            tasks[list_input[6]]['value'], tasks[list_input[7]]['value'],
                            tasks[list_input[8]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                             tasks[list_input[2]]['name'], tasks[list_input[3]]['name'], tasks[list_input[4]]['name'],
                             tasks[list_input[5]]['name'], tasks[list_input[6]]['name'], tasks[list_input[7]]['name'],
                             tasks[list_input[8]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

#new
        if str(gates[gate]['name']) == 'XOR':
            list_input = list()
            for i in range(len(gates[gate]['input'])):
                list_input.append('input_' + str(gates[gate]['input'][i]))

            
            if len(list_input) == 2:
                value = XOR(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

        if str(gates[gate]['name']) == 'OR':
            list_input = list()
            for i in range(len(gates[gate]['input'])):
                list_input.append('input_' + str(gates[gate]['input'][i]))
            
            if len(list_input) == 2:
                value = OR(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

            if len(list_input) == 4:
                value = OR(tasks[list_input[0]]['value'], tasks[list_input[1]]['value'],
                            tasks[list_input[2]]['value'], tasks[list_input[3]]['value'])
                
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'], tasks[list_input[1]]['name'],
                             tasks[list_input[2]]['name'], tasks[list_input[3]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)

        if str(gates[gate]['name']) == 'NOT':
            list_input = list()
            for i in range(len(gates[gate]['input'])):
                list_input.append('input_' + str(gates[gate]['input'][i]))
            

            if len(list_input) == 2:
                value = NOT(tasks[list_input[0]]['value'])
                subset_check(gates[gate]['result'], tasks[list_input[0]]['name'])
                update_value(value, gates[gate]['result'])
                critical_path(gates[gate]['name'], list_input)


c17()
# =============================================================================
# PRINTING
# =============================================================================
for task in tasks:
    if str(tasks[task]['randomly']) == 'True':
        print(f"input {tasks[task]['name']}, value is {tasks[task]['value']}")

for task in tasks:
    if str(tasks[task]['isCritical']) == 'True':
        print(f"stuck at {NOT(tasks[task]['value'])} in {tasks[task]['name']}")

for out in output:
    print(f"stuck at {NOT(output[out]['value'])} in {output[out]['name']}")
