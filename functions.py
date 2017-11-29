def palindrome(number_t):
    '''return True if *number_t* is a palindrome'''
    if number_t<=0:
        return False
    number_test = str(number_t)
    number_reverse = number_test[-1::-1] #Reversing the number
    if number_test == number_reverse:
        return True
    else:
        return False

def change_basis(number,base):
    """Return *number* in the new *base*"""
    l = []
    while number>0:
        l.insert(0,str(number%base))
        number = number//base
    l = ''.join(l)  # joining to obtain the str(number) 
    return(int(l))


