import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

def print_formatted(number):
   
   for i in range(1,number+1):
##      logging.debug(i)
      print('{} {} {} {}'.format(str(i),str(oct(i)[2:]),str(hex(i)[2:].upper()),str(bin(i)[2:]).rjust(2)),sep=' ')
##      logging.debug(print('{}\t{}\t{}\t{}'.format(str(i),str(oct(i)),str(hex(i)),str(bin(i)))))
print_formatted(2)                                    


            
