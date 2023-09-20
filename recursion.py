#global g
g = 10

def f(n):
  global g  # if not declared as global, local variable g will be created
  print("f start " + str(n))
  g += n
  print("f start g=" + str(g))
  if n == 0:
      return
  f(n-1)
  print("f end " + str(n))
  print("f end g=" + str(g))
  
g += 1
print("start")
f(3)
print("end g=" + str(g))
print("end")