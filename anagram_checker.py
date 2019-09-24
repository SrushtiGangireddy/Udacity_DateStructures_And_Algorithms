def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    count1 = [0]*256
    count2 = [0]*256
    
    for letter1 in str1.lower():
        if letter1 and letter1 != ' ':
            count1[ord(letter1)] += 1
    
    for letter2 in str2.lower():
        if letter2 and letter2 != ' ':
            count2[ord(letter2)] += 1
    
    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True
