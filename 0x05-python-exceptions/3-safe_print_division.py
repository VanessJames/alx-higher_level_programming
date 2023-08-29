#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Error: Division by zero")
    except Exception as e:
        result = None
        print("An error occurred:", e)
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        return result