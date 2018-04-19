def split_and_join(line):
    a=line.split(" ")
    return '-'.join(a)        #join method is used to join value with a specified
                                 #character mentioned in the single quote


line = input()
result = split_and_join(line)
print(result)    
