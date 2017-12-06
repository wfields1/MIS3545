#creating a funciton always begin with def [space] function name
#function naming convention [verb_direct object]

def convert_mins_to_hrs(mins):
    #parameters go in the parentheis
    #always follow the function with a :
    hours = mins / 60
    #second line is output
    return hours
    #return denotes what you what you want to receive

def convert_secs_to_hrs(secs):
    hours = secs / 60**2
    return hours


print(convert_mins_to_hrs(360))
print(convert_secs_to_hrs(7200))
