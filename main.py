
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature):
  #MY CODE IS HERE
  if temperature < 100.4:
    return False
  else:
    return True

# Get temperature from user and convert to float
temp = float(input("Please input a temperature\n>>> "))
if check_fever(temp):
  print("You have a fever.")
else:
  print("You don't have a fever.")