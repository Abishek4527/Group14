"""Group Name: [HIT137 group 14] 
Assignment2_question3
Group Members: 
[MUSKANPREET KAUR] - [S384001] 
[ARASHDEEP KAUR] - [S384121]
[ABISHEK KANDEL] - [S387576] 
[DAKSH JULKA] - [S384122] """


import turtle

print("The input should be in the following ranges.")
print("Branch angle range= 15 to 45")
print("Branch length 100 to 300")
print("Recursion Depth = 4 to 8")
print("Branch Length reduction factor = 0.5 to 0.8")

def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor):
    
#Recursive function to draw a tree pattern using turtle graphics.
    
    if depth == 0:
        return
    
    # Making the colour of starting branch and other branches different.
    if depth == recursion_depth:  
        turtle.color("brown")
    else:  
        turtle.color("green")

    # Draw the current branch
    turtle.pensize(depth)
    turtle.forward(branch_length)

    # Drawing left branch and returning to the original position
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.right(left_angle)  

    # Right branch
    turtle.right(right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.left(right_angle)  

    # Move back to the original position
    if depth != recursion_depth:
        turtle.backward(branch_length)

# Functions to validate integer and float input with range
def get_float_input_with_range(message, min_value, max_value):
    while True:
        try:
            value = float(input(message))
            if value < min_value or value > max_value:
                raise ValueError(f"Value must be between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input! {e}")


def get_int_input_with_range(message, min_value, max_value):
    while True:
        try:
            value = input(message)
            if not value.isdigit():
                raise ValueError("Recursion depth must be a whole number.")
            value = int(value)
            if value < min_value or value > max_value:
                raise ValueError(f"Value must be between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input! {e}")

# Getting user inputs with proper error handling
left_angle = get_float_input_with_range("Enter the left branch angle: ", 15, 45)
right_angle = get_float_input_with_range("Enter the right branch angle: ", 15, 45)
starting_branch_length = get_float_input_with_range("Enter the starting branch length: ", 100, 300)
recursion_depth = get_int_input_with_range("Enter the recursion depth: ", 4, 8)
branch_length_reduction_factor = get_float_input_with_range("Enter the branch length reduction factor: ", 0.5, 0.8)

# Seting up the turtle environment
turtle.speed("fastest")
turtle.left(90)  
turtle.penup()
turtle.goto(0, -200)  # Start at the bottom of the screen
turtle.pendown()

# Drawing tree
draw_tree(starting_branch_length, left_angle, right_angle, recursion_depth, branch_length_reduction_factor)
turtle.hideturtle()
turtle.done()