# Function

def linprint(input_str):
    if isinstance(input_str, str):
        print("Oh, you wanted \"" + input_str + "\" printed?")
    else:
        print("That's not a string")