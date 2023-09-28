"""
Name: Christopher Bucsa
"""

"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")
# Your code goes here:
#1a
def my_avg(someList):
    n = len(someList)
    mySum = 0
    for e in range(n):
        mySum = mySum + someList[e] 
    average = mySum / n 
    return average 
#1b
import random
random.seed(123)
#Storing integers in a list will be easier, although not asked by question.
randList = []
for e in range(1000):
    randInt = random.randint(-10,10)
    randList.append(randInt) 
#1c 
listAverage = my_avg(randList) 
print("Average of the 1000 randomly generated \nnumbers with values ranging "
      "from -10 to 10 is:",listAverage)
#We're summing up a mixture of positive and negative numbers, thus the sum will
#constantly fluctuate between positive and negative.  It will be no where close 
#to the number 1000, which is the number of elements in the list. Thus, since 
#we have a small numerator and a significantly larger denominator, the average 
#will be an extremely small number.  So, yes, the "-0.143" result makes sense 
"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")
# Your code goes here:
def find_sequence(fileName,string):
    locations = []
    with open(fileName,"r",encoding="utf-8") as file:# If I don't include encoding argument(from Google) I get this error: 'charmap' codec can't decode byte 0x9d in position 619: character maps to <undefined>
        for line in file:
            index = line.find(string) #returns -1 if not found
            if index != -1:
                locations.append(index) 
    return locations

print(len(find_sequence("war_and_peace.txt","you know"))) 
print(len(find_sequence("war_and_peace.txt","I am not")))

"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")
# Your code goes here:
#3a
myFile = open("/Users/bucsa/Desktop/cds-230/ProblemSets/ProblemSet4/war_and_peace.txt", encoding = "utf-8")
contents = myFile.readlines() 
#3b
content_length = len(contents) 
print("There are ", content_length, " lines in the war_and_peace.txt file")
#3c
myFile.seek(0) # Move pointer ot beginning of file  
count = 0
for line in myFile: 
    if line != "\n":
        count = count + 1
print("There are ", count, "non-empty lines in the file") 
#3d
myFile.seek(0) # Move pointer to beginning of file
count2 = 0
for line in myFile: 
    index2 = line.find("Hippolyte")
    if index2 != -1:
        count2 = count2 + 1
print("The word Hippolyte appears ", count2, "times throughout the file")
myFile.close() 

"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4:\n",40*"-")
# Your code goes here:
def data(fileName):
    with open(fileName,"r",encoding="utf-8") as newFile:
        data = newFile.read() 
    return data
#4a
data_len = len(data("dna.txt"))
#4b
file_string = data("dna.txt") 
a = file_string.count("a") 
c = file_string.count("c")
g = file_string.count("g")
t = file_string.count("t") 
#4c
sum_of_nucleotides = a + c + g + t 
difference = data_len - sum_of_nucleotides 
#4d
unique_letters = set(file_string)
#4e
errors = []
for e in unique_letters:
    if e.lower() not in {"a","c","g","t"}:
        errors.append(e)
#4f
occurences = {"a":a, "c":c, "g":g, "t":t, "errors":len(errors)}
for e in occurences: 
    print(f"{e}: {occurences[e]}")



