# return a keyword argument time that prints a message indicating whether its morning, afternoon, or night based on the value

def time_of_day(time, message= ""):
    if 1 <= time <12:
         message = "Good morning"
    elif 13 <= time <17:
        message = "Good afternoon"
    elif 17 <= time <= 24:
         message = "Good evening"
    else:
        return "Invalid time"
    
    return f"{time}: {message}"
    
result_time = time_of_day(time=4)

print(result_time)