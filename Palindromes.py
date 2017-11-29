from functions import palindrome,change_basis

n=1000
print('decimal',' ','smallest base in which the number is a palindrome','\n')
for number in range(1,n+1):
    count = 2
    nume = change_basis(number,count)
    while not palindrome(nume):
        count += 1
        nume = change_basis(number,count)
    print(number,count)
