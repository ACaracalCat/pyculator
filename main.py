# Hypothesis: This code is gonna be terrible
# Result: It was terrible, but works

import random

question = 0


print("Pyculator")
print("")
print("[1] - Easy Quiz")
print("[2] - Hard Quiz")
print("")
choice = input("Enter your choice: ")

if choice == "1":
  print("-------------------------")
  print("Pyculator Quiz")
  while True:
    print("")

    operator = random.randint(1,2)

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    if operator == 1:
      operator = "+"
    elif operator == 2:
      operator = "-"

    question += 1
    print(f"Question {question}: {num1} {operator} {num2}")

    if operator == "+":
      answer = num1 + num2
    elif operator == "-":
      answer = num1 - num2
    else:
      answer = 0

    print("")
    try:
      answered = float(input("Enter your answer: "))
    except ValueError:
      print("Invalid input. Enter a number.")
      answered = 9999
    print("")

    if answered == answer:
      print("Correct!")
    else:
      print("Wrong!")
else:
  print("-------------------------")
  print("Hard Pyculator Quiz")
  while True:
    print("")

    operator = random.randint(1,4)

    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    if operator == 1:
      operator = "+"
    elif operator == 2:
      operator = "-"
    elif operator == 3:
      operator = "*"
    elif operator == 4:
      operator = "/"

    question += 1
    print(f"Question {question}: {num1} {operator} {num2}")

    if operator == "+":
      answer = num1 + num2
    elif operator == "-":
      answer = num1 - num2
    elif operator == "*":
      answer = num1 * num2
    elif operator == "/":
      answer = num1 / num2
    else:
      answer = 0

    print("")
    try:
      answered = float(input("Enter your answer: "))
    except ValueError:
      print("Invalid input. Enter a number.")
      answered = 9999999999999999999999
    print("")

    if answered == answer:
      print("Correct!")
    else:
      print("Wrong!")
