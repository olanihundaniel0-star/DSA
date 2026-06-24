# decorators in python
def check_log(func):
    def wrap(a,b):
        print("Values are : ",a,b)
        return func(a,b)
    return wrap


def is_greater(func):
    def wrap(a,b):
        if a > b:
            a , b = b , a
        return func(a,b)
    return wrap


@check_log
@is_greater
def add(a,b):
    result1 = a + b
    print("The sum is : ",result1)
add = is_greater(add)
add(5, 10)

@check_log
@is_greater
def divide(a,b):
    result2 = a / b
    print("The division is : ",result2)

divide = is_greater(divide)
divide(10, 5)




