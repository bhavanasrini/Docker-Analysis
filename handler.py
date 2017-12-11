import sys
def fact(n):
       if n == 1: 
	 return 1
       else: 
	 return n*fact(n-1)
def handle(req):
       n = int(req)
       output = []
       output.append(str(fact(n)))
       print(', '.join(output))
