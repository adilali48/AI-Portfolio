print("===== AI Calculator =====")

num1 = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
num2 = float(input("Enter Second Number: "))

if operator == "+":
    print("Answer =", num1 + num2)

elif operator == "-":
    print("Answer =", num1 - num2)

elif operator == "*":
    print("Answer =", num1 * num2)

elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Answer =", num1 / num2)

else:
    print("Invalid Operator")