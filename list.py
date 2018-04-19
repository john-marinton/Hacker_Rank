##Initialize your list and read in the value of  followed by  lines of commands
##where each command will be of the types listed above.
##Iterate through each command in order and perform the corresponding operation on your list.
##
##Input Format
##
##The first line contains an integer, , denoting the number of commands. 
##Each line  of the  subsequent lines contains one of the commands described above.


ilist=[]
N = int(input())
for i in range(N):
   s=input().split()
   cmd=s[0]
   if cmd=='insert':
      ilist.insert(int(s[1]),int(s[2]))
   elif cmd=='remove':
      ilist.remove(int(s[1])) 
   elif cmd=='append':
      ilist.append(int(s[1]))
   elif cmd=='sort':
      ilist.sort()   
   elif cmd=='pop':
      ilist.pop()
   elif cmd=='reverse':
      ilist.reverse()
   elif cmd=='print':
      print(ilist)   


        
