'''
def convert_time_to_hrs(mins, secs):
    hours = mins / 60 + secs / 60**2
    return hours

print(convert_time_to_hrs(120, 7200))
'''
#in the body of the function you can use print instead of return
#then it will act thusly

def convert_time_to_hrs(mins, secs):
    hours = mins / 60 + secs / 60**2
    print(hours)

convert_time_to_hrs(180, 7200)

#most times you want to return a value however

