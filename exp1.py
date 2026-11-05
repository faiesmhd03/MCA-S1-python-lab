string1=input("Enter Your String : ")
new=string1[0]+string1[1:].replace(string1[0],"$")
print(f"String with all occurances are $ except first character :\n{new}")
swap2ends=string1[-1]+string1[1:-1]+string1[0]
print(f"String With first and last character exchanged : \n{swap2ends}")