# we want to multiply any 2 digit no with only 11
constant = 11

# we want to create a loop such that it only accepts 2 digit no, if
# user enters more single or 3 digit number, then it should ask him to enter 
# 2 digit no again. it only executes the programm untill he provides the valid 2 digit no

while True:
    ui = int(input("Please enter the two digit number: "))
    if ui>99 or ui<10:
        print("Wrong! Please enter only two digit number: ")
    else:
        break


# convert the input into a list
list1 = list(str(ui))


breakthroughnumber = int(list1[0]) + int(list1[1])  #adding elements of list and making them nos

list1.append(breakthroughnumber) # later add the above addition to the previous list of string. note this list now has strings and nos.

list1 = [int(x) for x in list1] # now converting all the strings to int in the list

last_element = list1.pop() #it extracts the last element of list
middleplacing = len(list1)//2 # this extracts the middle position as we divide with 2(i.e., exactly half)
list1.insert(middleplacing,last_element) #using the above middle position, there we are inserting the last elemment that we got earlier


individualnos = [] #empty list
# creating a for loop to make all the elements to unit level(or atom sized elements)
for item in list1:   
    individualnos.extend(int(x) for x in str(item))


if len(individualnos)<=3:
    result = int("".join(map(str,individualnos)))
    print(result)
else:
    #till this point we have got all the individual nos separted into atom sized elements
    # now we have to add first two nos and place the result beside the rest of element
    # for this am defining a function 
    def placenos(individualnos):
        list2 = int(individualnos[0]) + int(individualnos[1]) #adding first 2 elements
        list2 = list(str(list2))  #making the addition result to a list
        list2.extend(individualnos[-2:]) #it makes all the elements to atom sized elements
        numb = int("".join(map(str,list2))) # converting all strings to int
        return numb
    print(f"Multiplying {ui} with {constant} ")
    print(placenos(individualnos))
