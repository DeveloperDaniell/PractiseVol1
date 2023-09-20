def f(n):
  print("f start " + str(n))
  if n == 0:
      return
  f(n-1)
  print("f end " + str(n))
 
print("start")
f(3)
print("end")