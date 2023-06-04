def func(arg):
  print(arg)

arg=input("Input > ")
func(arg)

# This works for all data types, but it sends a traceback error if you pass no argument.
# It also sends an error if you pass more than 1 argument.