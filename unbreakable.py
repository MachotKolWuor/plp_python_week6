from safe_tools import safe_divide,safe_number,get_field
# 1.Demo that division never crashes
print("Safe divide 10/2:", safe_divide(10,2))
print("Safe divide 10/2:", safe_divide(10,0))

# 2. Unbreakable input loop
print("\nEnter number(type quit to stop):")
while True:
    text = input("Number: ")
    if text.lower() == "quit":
        break
    num = safe_number(text)
    print("You entered:", num)

    if num != "Not a number":
        print("10 divided by it is:", safe_divide(10,num))

# 3. Demo that dict lookup never crashes
learner = {"name": "Amina", "score": 92}
print("\nScore is:", get_field(learner, "score"))
print("Email is:", get_field(learner, "email"))

print("\nProgram ended safely - never crashed")