

# ** Reborg World

# ** Reborg 3

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    while front_is_clear():
        if not at_goal():
            move()
        else:
            break
    

# ** REborg 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
    
while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()
    
# ** Maze  


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

        
    
while not at_goal():
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        elif wall_in_front():
            turn_left()
        else:
            move()