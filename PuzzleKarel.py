from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
  #find the beeper
    locate_beeper()
  #Get on route
    enter_the_net()
  #Beeper placement on an empty spot
    insert_beeper() 
  #Go home to the initial postion
    face_west()
  #Get en route home facing east
    go_home()
  
#takes the beeper home 
def go_home():
    for i in range(2):
        move()
    face_east()
    back_to_sender()

#falls back to the sender
def  back_to_sender():
    for i in range(3):
        move()
    face_west()

#changes direction to east 
def face_east():
   for i in range(3):
       turn_left()

#changes direction to west 
def face_west():
   for i in range(2):
       turn_left()

#moves and drops the beeper
def insert_beeper():
    move()
    put_beeper()

#goes in the tunnel  
def enter_the_net():
    move()
    turn_left()
    move()

#Gets the beeper
def locate_beeper():
    for i in range(2):
      move()
    pick_beeper()
    




# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Puzzle.w')
