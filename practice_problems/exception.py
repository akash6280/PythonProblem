def divide():
    a = 5
    b = 0
    try:
        c = a / b
    except ZeroDivisionError as e:
        print(e.__str__())
    finally:
        print("In finally block")


divide()
