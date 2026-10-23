newTuple = ("Mahadi","Hasan","x","Sonom","Sultan",)

a=list(newTuple)
a.append("Jim")
a[2]="Mithu"
newTuple=tuple(a)



print(newTuple)
print(type(newTuple))