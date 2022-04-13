# HW1
from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from dirty_main import *


def decorator_function(wrapped_func):
    def wrapper(*args):
        print(datetime.now())
        wrapped_func(*args)
    return wrapper


@decorator_function
def accounting(value):
    if value == 1:
        get_employees()
    if value == 2:
        calculate_salary()


accounting(1)
accounting(2)
print_birthday()
print_job()