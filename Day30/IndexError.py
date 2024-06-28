fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
      fruit = fruits[index]
      print(fruit + " pie")
    except IndexError:
      print("Fruit pie")

# 🚨 Do not change the code below
make_pie(4)

#input - ["Apple", "Pear", "Orange"]