def make_snippet(input_string):
    if len(input_string.split()) <= 5:
        print(input_string)
        return input_string
    else:
        return " ".join(input_string.split()[:5]) + " ..."
