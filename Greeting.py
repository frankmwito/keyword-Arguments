# return a greeting message with name and age as key word arguments

def greeting(name, age, message = "Hello"):
    return f"{message} {name} you are {age}"

message1 = greeting(name = "Frank", age=22)

print(message1)