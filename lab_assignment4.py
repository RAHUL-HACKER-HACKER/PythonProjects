script=input("enter your script:")
count=1
for i in script:
    if i==" ":
        count+=1
        print()
    else:
        print(i,end="")
print("\nnumber of word:",count)




#or

# asking for user input
search_word_count = input('Enter the word: ')

# opening text file in read only mode
file = open("file.txt", "r")

# reading data of the file
read_data = file.read()

# converting data in lower case and the counting the occurrence 
word_count = read_data.lower().count(search_word_count)

# printing word and it's count
print(f"The word '{search_word_count}' appeared {word_count} times.")