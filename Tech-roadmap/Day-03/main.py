age = 18
if age >= 18:
    print("You are an Adult")
score = 40
if score >= 50:
    print("You passed")
else:
    print("Failure")
for i in range(1,6):
    print(i)
print("====Jarvis Access System====")
name = input("What is your name ?")
Age = int(input("How old are you ?"))
Role = input("what is your role? ")

if age >18:
    print(f"Welcome {name}, Standard access granted")
elif Role == "admin":
    print(f"welcome {name}, Full access granted")
else:
    print(f"Sorry {name}, you cannot access the site")