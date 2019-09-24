def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: Write your solution here
    if len(str1) != len(str2):
        return None
    else:
        i = 0
        nonMatch = 0
        for a,b in zip(str1,str2):
            if a != b:
                nonMatch += 1
            i += 1
        return nonMatch
