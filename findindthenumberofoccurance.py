#In this challenge, the user enters a string and a substring. You have to print the number of times,
#that the substring occurs in the given string.
#String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):   
   for i in range(0,len(string)):
      result+=string.count(sub_string)
      
   return result 


string = input().strip()
sub_string = input().strip()  
count = count_substring(string, sub_string)
print(count)
