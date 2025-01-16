import turtle

print("For proper tree like stucture the input values should be in follwing ranges")
print("Branch angle range= 15 to 45")
print("Branch length 100 to 300")
print("Recursion Depth = 4 to 8")
print("Branch Length reduction factor = 0.5 to 0.8")

def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor,original_depth):
    
#Recursive function to draw a tree pattern using turtle graphics.
    
    if depth == 0:
        return
    
    # Making the colour of starting branch and other branches different.
    if depth == original_depth:  
        turtle.color("brown")
    else:  
        turtle.color("green")

    # Draw the current branch
    turtle.pensize(depth)
    turtle.forward(branch_length)

    # Drawing left branch and returning to the original position
    turtle.left(left_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor,original_depth)
    turtle.right(left_angle)  

    # Right branch
    turtle.right(right_angle)
    draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor,original_depth)
    turtle.left(right_angle)  

    # Move back to the original position
    if depth != original_depth:
        turtle.backward(branch_length)

# Getting user inputs
left_angle = float(input("Enter the left branch angle: "))
right_angle = float(input("Enter the right branch angle: "))
starting_branch_length = float(input("Enter the starting branch length: "))
recursion_depth = float(input("Enter the recursion depth: "))
branch_length_reduction_factor = float(input("Enter the branch length reduction factor: "))

# Set up the turtle environment
turtle.speed("fastest")
turtle.left(90)  
turtle.penup()
turtle.goto(0, -200)  # Start at the bottom of the screen
turtle.pendown()

# Drawing tree
draw_tree(starting_branch_length, left_angle, right_angle, recursion_depth, branch_length_reduction_factor,recursion_depth)
turtle.hideturtle()
turtle.done()