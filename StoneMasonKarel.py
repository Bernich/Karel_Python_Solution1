from PuzzleKarel import face_east
from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #Starts by filling the column
    fill_column();
    horizontal_direction();
   
   
    while front_is_clear():
        next_column();
        descend_column();
        fill_column();
    
        if facing_south():
            ascend_column();
        elif facing_east():
             fill_column();
        elif facing_south():
             ascend_column();
             fill_column();

    

#fill the columns if facing north
def fill_column():
     if facing_east():
      turn_left();
     while front_is_clear():
        if no_beepers_present():
           put_beeper();
        move();
#manouvre to the right position
def horizontal_direction():
    turn_left();
    turn_left();
    turn_left();
#move to the next column
def next_column():
    while front_is_clear():
        move();
        turn_left();
        if front_is_clear():
            horizontal_direction();
        
           
# def descend_column():
#    if facing_north(): 
#     face_south();
#     if no_beepers_present():
#         put_beeper();
#         while front_is_clear():
#             move();
#             if no_beepers_present():
#              put_beeper();
def descend_column():
   if facing_north(): 
    face_south();

    if no_beepers_present():
        put_beeper();
        while front_is_clear():
            move();
            if no_beepers_present():
             put_beeper();

def ascend_column():
    if no_beepers_present():
        put_beeper()
    look_up();
    while front_is_clear():
        move();
    horizontal_direction();

def look_up():
     turn_left();
     turn_left();

def face_south():
    turn_left();
    turn_left();      
   


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('SampleQuad1.w')

#This code also works but because of the DRY principle i preferred going with the other one also
 #Secondry stage
    # next_column();
    # descend_column();
    # ascend_column();
    #tetiary stage
    # next_column();
    # descend_column();
    # fill_column();
    # ascend_column();


    #Final stage
    # next_column();
    # descend_column();
    # fill_column();