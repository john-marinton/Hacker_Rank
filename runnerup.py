list1_=[]
for x in range(int(input())):
    rinput_= int(input())
    list1_.append(rinput_)
set_=set(list1_)
list2_=list(set_)
max_=list2_.remove(max(list2_))

print(max(list2_))


   
   
