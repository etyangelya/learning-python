#this is my first python





first_name= "new"
second_name= "\tfriend"
third_name= ""
full_name= first_name + second_name + third_name
message = "hello\t" + full_name + "\nwould you like to learn python today" + "?"
print(message)
answer= input("yes or no ?:\n")
if answer == "yes":
    print( "proceed")
    name = input( "enter your name:\n ")
    age = int(input( "enter your age:\n "))
    highschool = input( "enter your highschool:\n ")
    print("i am  " +  name )
    print("i am  " + str(age) )
    print("i used to go to " +  highschool [0:])
else:
    print("sorry")

