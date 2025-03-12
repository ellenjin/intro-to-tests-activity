def count_a_letter(sentence, letter): 
    # if type(letter) is int or not letter.isalpha():
    if not letter.isalpha():
        return None
    if not sentence: # confusion on what exactly -- checking if sentence is empty?
        return None
    
    count = 0
    for char in sentence:
        if char == letter:
            count +=1
    
    return count

# test cases:
# Sentence = A, letter = A -- return count = 1
# check if we input integer for 'letter', the return result None
# check that empty string returns None