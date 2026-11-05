string1=input("enter your string : ")
string12=input("enter your string : ")
print("string with swapping the character at position 1 :\n")
print(string12[0]+string1[1:]," : ",string1[0]+string12[1:])

colours=input("enter your colours ").split()
print(" ".join([colours[i] for i in range(0,len(colours),2)]))