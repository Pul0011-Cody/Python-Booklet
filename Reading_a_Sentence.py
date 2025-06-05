# Gets the sentence
sentence = input("Write your sentence here")
numberA = 0
numberE = 0
numberI = 0
numberO = 0
numberU = 0
# Counts the amount of a, e, i, o, u
for letter in sentence:
    if letter =="a":
        numberA +=1
    if letter =="e":
        numberE +=1
    if letter =="i":
        numberI +=1
    if letter =="o":
        numberO +=1
    if letter =="u":
        numberU +=1
# Prints the amounts
print("The number of a's in the sentence is:", numberA)
print("The number of e's in the sentence is:", numberE)
print("The number of i's in the sentence is:", numberI)
print("The number of o's in the sentence is:", numberO)
print("The number of u's in the sentence is:", numberU)