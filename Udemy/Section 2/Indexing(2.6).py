c = 'Hi, there!'

print(c[4])
print(c[-1])
print(c[0:1])
#splitting is limited by the upper bound, if you want Hi you must include c[O:2]
print(c[0:2])
#you can shortcut by doing c[:2] which is like doing [0:2]
print(c[:2])
#also able to do everything after the index by doin [4:]
print(c[4:])
#works witht the negative as well
print(c[-6:-1])
print(c[-6:])

