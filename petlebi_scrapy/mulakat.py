# abba aba

def isPalindrome(myString):
    otherString = myString[::-1]
    for i in range(len(myString)):
        if(myString[i] != otherString[i]):
            return False        

    return True
        

# print(isPalindrome("abbc"))

# 1 1 2 3 5 8
# <= 0: hata
def fibonacci(number):
    numbers = []
    

    if(number == 1):
        numbers.append(1)
    elif(number == 2):
        numbers.append(1)
        numbers.append(1)
    else:
        numbers.append(1)
        numbers.append(1)
        for i in range(number-2):
            numbers.append(numbers[i+1] + numbers[i])
    return numbers


print(fibonacci(6))
    
