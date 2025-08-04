#take user input
a = input("enter a word : ")
#program to check break keyword
for i in a: #iterate for loop
    if (i == 'a'): #condition 1
        #display result
        print("the letter a has been found")
        break
    else:
        #display result
        print("couldn't find a")