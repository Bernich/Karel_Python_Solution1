from PuzzleKarel import face_east
from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #Karel starts by placeing a beeper
    put_beeper();
    #Repeats somes movements(functions) till the condition turns false
    while front_is_clear():
      climb();
      put_beeper();
       
     
          
#this is Karels's ramp climbing process
def climb():
  if beepers_present:
    move();
    turn_left();
    move();
    right_direction();
    move();
    

def movement():
   if front_is_clear():
     move();
     move();
   

  
#Turns into the right direction     
def right_direction():
    turn_left();
    turn_left();  
    turn_left();
                                                                    
                                                                  



        


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('RampKarel1.w')
