data = [12]

def elements(data):
    try:
        res = 12/0
    except ZeroDivisionError as ex:
        print("Error: {ex}")
    else:
        print(res)
    finally:
        print("Visca Barca Visca Catalunya")

# Call the function
elements(data)