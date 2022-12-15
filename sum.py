def sum(a, b):
    return (a + b)

def getNumber() :
    num = input('Enter number: ')
    try:
        num = int(num)
        return num
    except:
        return getNumber()
    

a = getNumber()
b= getNumber()

print(f'Sum of {a} and {b} is {sum(a, b)}')
