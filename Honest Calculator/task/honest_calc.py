msg_list = ["Enter an equation",
            "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy",
            " ... very lazy",
            " ... very, very lazy",
            "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]

operators = ["+", "-", "*", "/"]
memory = 0


def is_one_digit(v):
    try:
        if v.is_integer() and -10 < v < 10:
            return True
        else:
            return False
    except AttributeError:
        if -10 < v < 10:
            return True
        else:
            return False


def variable_messages(v1, sign, v2):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_list[6]
    if (v1 == 1 or v2 == 1) and sign == "*":
        msg = msg + msg_list[7]
    if (v1 == 0 or v2 == 0) and (sign == "*" or sign == "+" or sign == "-"):
        msg = msg + msg_list[8]
    if msg != "":
        msg = msg_list[9] + msg
        print(msg)


while True:

    calc = input(msg_list[0])
    x, operator, y = calc.split()
    if x == y == "M":
        x = memory
        y = memory

    elif x == "M" and y != "M":
        x = memory

        try:
            if str(type(y)) != "<class 'float'>":
                y = float(y)

        except ValueError:
            print(msg_list[1])
            continue

    elif y == "M" and x != "M":
        y = memory

        try:
            if str(type(x)) != "<class 'float'>":
                x = float(x)

        except ValueError:
            print(msg_list[1])
            continue
    else:
        try:
            x = float(x)
            y = float(y)

        except ValueError:
            print(msg_list[1])
            continue

    if operator not in operators:
        print(msg_list[2])
        continue

    variable_messages(x, operator, y)

    if operator == "+":
        result = x + y
    elif operator == "-":
        result = x - y
    elif operator == "*":
        result = x * y
    elif operator == "/" and y != 0:
        result = x / y
    else:
        print(msg_list[3])
        continue

    print(result)

    while True:
        answer = input(msg_list[4])
        if answer == "y":
            if is_one_digit(result):
                index = 10
                while index <= 12:
                    answer = input(msg_list[index])
                    if answer == "y":
                        index += 1
                    elif answer == "n":
                        break
                if answer == "y":
                    memory = result
            else:
                memory = result
            break
        elif answer == "n":
            break

    answer = input(msg_list[5])
    end = False
    while True:
        if answer == "y":
            break
        elif answer == "n":
            end = True
            break

    if end:
        break
