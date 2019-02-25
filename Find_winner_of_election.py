/ *
https://ide.geeksforgeeks.org/j1iwOp2hYI
*/

from collections import Counter

def winner(input):
    my_dict = {}
    for i in range(len(input)):
        my_dict[input[i]] = input.count(input[i])
    
    dict  = {}
    
    for value  in my_dict.values():
        dict[value] = [] 
        
    for (key,value) in my_dict.items():
        dict[value].append(key)
        
    
    print(dict)
    
    maxVote = sorted(dict.keys(),reverse=True)[0] 
    
     # check if more than 1 candidates have same  
     # number of votes. If yes, then sort the list 
     # first and print first element 
    if len(dict[maxVote])>1: 
        print(sorted(dict[maxVote])[0])
    else: 
        print(dict[maxVote][0])
    

   

if __name__ == "__main__":
    input = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie', 
'john','johnny','jamie','johnny','john'] 
    winner(input) 
