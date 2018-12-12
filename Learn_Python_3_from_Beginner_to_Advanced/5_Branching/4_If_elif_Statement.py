
passergy_speech = 'Hi'              # keeping condictions specific so allways only one outcome is possible
if passergy_speech == 'Hello':
    print("Hi")
elif passergy_speech == "Hi":
    print("Hello")
else:
    print("Hey")

# if condition:                     # syntax of the if / elif / else statement
    # code
# elif condiction2:
    # code
# elif condiction3:
    # code
# else:
    # code

num = 3                             # If more are True, only the first condiction is going to happen
if(num > 1 and num < 5):
    print(num)
elif (num > 2 and num < 4):
    print(num+1)
else:
    print(num-1)