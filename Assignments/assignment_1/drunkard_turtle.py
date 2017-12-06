def drunkard_walk(x, y, n):
    """
    x, y: the original location
    n: the number of intersections(steps)
    return the distance after n intersections(steps) from the origin
    """
    directions = ['forward', 'backward', 'left', 'right']
    for single_decision in range(n):
        random_direction = random.choice(directions)
        print("The drunk's number " + str(single_decision+1) + " decision was to take a 'step' " + random_direction)
        
        turtle.pendown()  
    
        if random_direction == 'forward':
            turtle.setheading(0)
            turtle.forward(50)
            y += 1
        if random_direction == 'backward':
            turtle.setheading(180)
            turtle.forward(50)
            y -= 1
        if random_direction == 'left':
            turtle.setheading(270)
            turtle.forward(50)
            x -= 1
        if random_direction == 'right':
            turtle.setheading(90)
            turtle.forward(50)
            x += 1

    print("The drunkard started from (%d,%d)." % (x, y))
    z = abs(x) + abs(y)
    x = str(x)
    y = str(y)
    print("After", n, "intersections, he managed to go all the over to  (", x, ",",y,")", ". He is " +  str(z) + " steps from home.")
    turtle.done()

drunkard_walk(0,0, 50)