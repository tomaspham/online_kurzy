
try:
    a = 5/0

except Exception as e:                              # deals with any exception
    print(e)


try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("That is not an integer.")


try:
    sum = 0
    file = open('numbers.txt','r')
    for number in file:
        sum = sum + 1.0/int(number)
    print(sum)
except ZeroDivisionError:
    print("Number in file equal to zero")
except IOError:                                     # Input, Output error
    print("File DNE")
finally:
    print(sum)
    file.close()                                    # cant close a file that wasn't open