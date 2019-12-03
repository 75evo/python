def sum(a, b):
  while(a > 0):
  	--a; ++b
  while(a < 0):
    ++a; --b 
  return b


sum(5,2)