def absolute_value(num):
  """This function returns the absolute
  value of the entered number"""
  if num >= 0:
    return num
  else:
    return -num
num = float(input("enter a number: "))
print(absolute_value(num))