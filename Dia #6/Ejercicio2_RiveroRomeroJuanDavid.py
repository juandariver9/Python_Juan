#def negate(num):
#    return -num
#
#def large_num(num):
#    res = (num > 1000)
#    
#negate(b)
#neg_b =num
#print 'b:', b, 'neg_b:', neg_b
#
#big = large_num(b)
#print 'b is big:', big
#
#Se asigna un valor a la variable "b"
#Se usa la función "negate y se asigna a "neg_b"
#La estructura del print esta incorrecta ya que deberia llevar parentesis
#la segunda funcion se le agrega el retorno 
#----------------------------------
def negate(num):
    return -num

def large_num(num):
    res = (num > 1000)
    return res  

b = 1200  

neg_b = negate(b)  
print('b:', b, 'neg_b:', neg_b)  

big = large_num(b)
print('b is big:', big)
