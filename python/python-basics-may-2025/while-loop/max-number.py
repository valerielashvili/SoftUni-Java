import sys

usr_input = input()
num = 0
biggest = -sys.maxsize

while usr_input != "Stop":
    if int(usr_input) > biggest:
        biggest = int(usr_input)
        
    usr_input = input()

print(biggest)