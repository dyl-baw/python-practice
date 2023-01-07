def format_names(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    name = (f'Result: {f_name} {l_name}').title()
    return name

print(format_names(input("What is your first name? "), input("What is your last name? ")))

