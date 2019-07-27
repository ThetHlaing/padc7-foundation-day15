#Open the file
handle = open('./data/quotes.txt','r')
print(type(handle))
#Create a Dictionary
counts = dict()

#Read the opened text file line by line
for line in handle:
    print(line)
    #Split the string by space
    words = line.split()    
    for word in words:
        #Add the count in if the key is already existed
        #Insert 1 if the words haven't existed before
        counts[word] = counts.get(word,0) + 1
        
print(counts)

# Ref:
# Dictionary : https://www.geeksforgeeks.org/python-dictionary/
