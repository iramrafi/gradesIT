print("#######################   MESSAGE SENDER  #########################")
print("Hello MIT CELL:")
k = int(input("Please enter k value to shift transform message: "))
string = str(input("Now, please enter your message: "))
#Converting input string to encoded message
message = ""
for letter in string:
    if 'a'<= letter  <= 'z' or 'A'<= letter <= 'Z':
        newl = chr(ord(letter) + 3)
        message = message + str(newl)
    elif letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        newl = int(letter) + 3
        message = message + str(newl)
    elif letter == " ":
        message = message + "@"
    elif letter == ".":
        message = message + "#"
    else:
        continue

print("You send: ", message, "\n")
print("#######################   MESSAGE RECEIVER   #########################")
print("Hello Instructor,\nYou got a message: ", message)
new_k = int(input("To read this in original form, please enter given value of k: "))
if new_k == k:
    print("Original message: ", string)
else:
    print("Sorry, wrong value of k entered!")
