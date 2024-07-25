def calculator(x,y,operation):
    if operation == 'Addition':
        return x+y
    elif operation == 'Difference':
        return abs(x-y)
    elif operation == 'Division':
        return x/y
    elif operation == 'Multiplication':
        return x*y