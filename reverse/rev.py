
def reverse(x):

 if x > 0:
  a = int(str(x)[::-1])
 if x <= 0:
  #a = -1*int(str(x*-1)[::-1])            
  a = -1*int(str(x)[::-1])            
 if a < -2**31 or a > 2**31-1:
  return 0
 return a

print(reverse(-7654))
