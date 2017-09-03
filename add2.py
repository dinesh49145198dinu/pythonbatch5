def sum(a,b):
    s=a+b
    return s 
def read():
    return int(input('enter a value\n')) 
a=read() 
b=read() 
r=sum(a,b)
print('sum 0f {0}+{1}={2}'.format(a,b,r))
