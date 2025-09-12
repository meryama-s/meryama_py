#challenge 1
number= int(input("enter a number: "))
length=int(input("enter the length: "))
for i in range(length):
    print(number + i*number)

#challenge 2

wordd= input("enter a word with that doesn't have dupplicate letter in the first place but repeat as you want to see the result :) : ")
no_dupp= ""
for lett in wordd:
    if lett not in no_dupp:
        no_dupp += lett
print(no_dupp)