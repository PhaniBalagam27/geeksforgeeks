### https://ide.geeksforgeeks.org/K74MoW4p81
### Maximum length of consecutive 1’s in a binary string in Python 

def maxConsecutive1(input):
    count  = 0 
    res = 0
    for i in range(len(input)):
        if input[i] == '0':
            count = 0
        else:
            count += 1
            res = max(res,count)
            
    print(res)



# Driver program 
if __name__ == "__main__": 
    input = '11000111101010111'
    maxConsecutive1(input)
