##Can you do it using only arithmetic operations, a single for loop and print statement?
##
##Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
##
##Note: Using anything related to strings will give a score of .


for i in range(1,int(input())):
    print(i*(10**i -1)//9)             #//: divide with integral result (discard remainder)
             


                                  #explanation

                                   # if 2 comes in
                                   # In print 2*(10**2 -1)//9
                                   #           2*(100-1)//9
                                              # 2*(99)//9
                                               # 2*(11)
                                                #22
