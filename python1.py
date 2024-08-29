a = 1
b = 2
c = a + b

for x in range(10):
    y = x * c   #Debugger stops before executing this line
                #It will run line 6 TEN times (len of range)
message = "Hello World!"

print(message)