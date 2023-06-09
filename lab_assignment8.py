words = []
with open("file.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
most_common = counts.most_common(3)
print(most_common)


#other programm
# file = open("gfg.txt","r")
# frequent_word = ""
# frequency = 0 
# words = []
 
# for line in file:
     
#     line_word = line.lower().replace(',','').replace('.','').split(" "); 
     
   
#     for w in line_word: 
#         words.append(w); 
         

# for i in range(0, len(words)): 
     
    
#     count = 1; 
     
    
#     for j in range(i+1, len(words)): 
#         if(words[i] == words[j]): 
#             count = count + 1; 
 

#     if(count > frequency): 
#         frequency = count; 
#         frequent_word = words[i]; 
 
# print("Most repeated word: " + frequent_word)
# print("Frequency: " + str(frequency))
# file.close();