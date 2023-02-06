msg_list = ["Enter an equation",
            "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):"]

operators = ["+", "-", "*", "/"]
memory = 0

while True:

    calc = input(msg_list[0])
    x, operator, y = calc.split()

    if x == "M":
        x = memory

        try:
            y = float(y)

        except ValueError:
            print(msg_list[1])
            continue

    elif y == "M":
        y = memory

        try:
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
