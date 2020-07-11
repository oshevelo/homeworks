def count(elements):
    element_count = int(input("Enter the number of elements: "))
    while element_count < elements:
        print("Please, enter a number starting from 2")
        return count(elements)
    else:
        return element_count


def enter_number():
    try:
        input_number = int(input("Enter the number: "))
    except ValueError:
        print('Please, enter a number!')
        enter_number()


def enter_operator():
    valid_operators = ["*", "-", "+", "/"]
    input_operator = input("Enter operator: ")
    if input_operator in valid_operators:
        return_operator = input_operator
    else:
        enter_operator()
    return return_operator


def calculate():
    count_int = count(2) - 1
    result = 0
    for x in range(count_int):
        if x == 0:
            result = enter_number()
        temp_operator = enter_operator()
        if temp_operator == "+":
            result += enter_number()
        elif temp_operator == "-":
            result -= enter_number()
        elif temp_operator == "*":
            result *= enter_number()
        elif temp_operator == "/":
            temp_number = enter_number()
            while temp_number == 0:
                print("U cant enter zero value")
                temp_number = enter_number()
            else:
                result /= temp_number

    print(result)


calculate()



