#Task
#You are given an immutable string, and you want to make changes to it.


def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    return ''.join(l)
   
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

 

