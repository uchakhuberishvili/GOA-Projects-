def enough(cap, on, wait):
    if on + wait >= cap:
        thing = on + wait
        result = thing - cap
        return result
    else:
        return 0
    
def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
    
def combine_names(first,second):
    return str(first + " " + second)

def _if(bool_value, func1, func2):
    if bool_value:
        func1()
    else:
        func2()
