
file = open("write.txt","w+")               # reading + writing / also creates the file in the project directory if the file does not exists
file.write("Hello file. I am string!")
file.seek(0)                                # returns cursor to the given index
file.write("this")
file.seek(0)
print(file.read())
file.close()