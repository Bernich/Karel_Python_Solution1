from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #Karel Fill the line with beepers 
    lenght = total_steps();
    drop = int(lenght);
    turn_around();
    for i in range(drop):
       put_beeper();
       move();
       if front_is_blocked():
           turn_around();
           
    



def turn_around():
    turn_left();
    turn_left();
def total_steps():
    width = 1;
    while front_is_clear():
        move();
        width +=1;
    return width;
    


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
