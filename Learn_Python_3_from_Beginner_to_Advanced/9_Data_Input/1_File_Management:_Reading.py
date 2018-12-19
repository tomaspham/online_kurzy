

#open(filename, access, buffering)

file = open("/Users/juraj/PycharmProjects/Online_kurzy/Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt","r")
print(file.read())
file.close()

# /Users/juraj/PycharmProjects/Online_kurzy/Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt                                  # actual file path
# Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt                                                                            # relative file path


file = open("/Users/juraj/PycharmProjects/Online_kurzy/Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt","r")
print(file.read(4))
file.close()


file = open("/Users/juraj/PycharmProjects/Online_kurzy/Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt","r")
print(file.read(4))
print(file.tell())                                                                                                                          # tells us where the cursor is located in the file
file.seek(5)                                                                                                                                # moves the cursor in the file to the given index
print(file.tell())
file.close()


file = open("/Users/juraj/PycharmProjects/Online_kurzy/Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt","r")
for line in file:
    print(line)

file.close()


file = open("/Users/juraj/PycharmProjects/Online_kurzy/Learn_Python_3_from_Beginner_to_Advanced/9_Data_Input/file.txt","r")
print("File name: " + file.name)
# print("is closed:" + str(file.closed))                                                                                                      # converts boolean result to string / tels us if the file is closed or open
# print("is closed:{0}".format(str(file.closed)))
print(f"is closed:{str(file.closed)}")
print("Mode: " + file.mode)
file.close()