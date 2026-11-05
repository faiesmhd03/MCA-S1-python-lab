colourlist1=["red","green","blue","orange",]
colourlist2=["black","blue","white"]
print(set(colourlist1)-set(colourlist2))
print(set(colourlist1).difference(colourlist2))

l1=[]
print("list empty " if len(l1)==0 else "list not empty")