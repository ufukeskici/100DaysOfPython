def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while at_goal() == False:
    if wall_on_right() == False:
        turn_right()
        move()
    elif wall_in_front() == False:
        move()
    else:
        turn_left()
