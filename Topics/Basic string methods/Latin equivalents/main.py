name = input()


def normalize(name_input):

    # put your code here
    new_name = name_input.replace("é", "e")
    new_name = new_name.replace("ë", "e")
    new_name = new_name.replace("á", "a")
    new_name = new_name.replace("å", "aa")
    new_name = new_name.replace("œ", "oe")
    new_name = new_name.replace("æ", "ae")

    return new_name


print(normalize(name))
