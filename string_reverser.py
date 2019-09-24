def string_reverser(our_string):
    temp = ""
    for index in range(len(our_string)):
        temp += our_string[(len(our_string)-(index+1))]
        
    return temp
