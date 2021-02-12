i = 0 # Element
l = i + 1 # Element after i
mywords = ["Appolo", "Apple", "Appricot", "Durvian","Durtete", "Carrot",]
size=len(mywords)
print("Original: " , mywords)
for i in range (0, size):
    for l in range (i + 1, size):
        p=min(len(mywords[i]),len(mywords[l]))
        for k in range (0,p-1):
            if ord(mywords[i][k].lower()) < ord(mywords[l][k].lower()):
                break
            if ord(mywords[i][k].lower()) > ord(mywords[l][k].lower()):
                x = mywords[i]
                mywords[i] = mywords[l]
                mywords[l] = x
                break
        
print("Sorted:" , mywords)
