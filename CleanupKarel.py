from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to pick up all beepers from the first row of any sized world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
#move forward and check if there is a beeper
    hunt();


def hunt():
   while front_is_clear():
     move();
     if beepers_present():
         pick_beeper();

        

    
def catch():
    pick_beeper();
#it should pick up the beeper if there is   



# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Cleanup2.w')
