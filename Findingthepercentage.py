n=int(input())
details_={}
for x in range(n):
   name,*line=input().split()
   scores=list(map(float,line))
   details_[name]=scores
   
query_name = input()
retrieve_=details_.get(query_name)
sum_=sum(retrieve_)/3
print('%.2f'%sum_)   #the %.2f is used to tell the print function to print
                       #two floating point values after .dot
