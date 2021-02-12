# This program takes user input for one round of bowling.
# The user is prompted for how many pins they knock down
# on each shot of each frame. If they get all 10 pins down 
# on the first shot, then then it continues for input on the
# next frame. Feedback is given on whether the frame was a
# strike, spare, or open frame. The second shot is limited
# to how many pins remain after the first shot in a frame.
# If an invalid input is given, either out of bounds numeric
# value or a string that is not a number, it will prompt you 
# to re-enter that value. If the user enters "q", the program
# is aborted through a raised exception.
#
# Once the values for all 10 frames have been entered, 
# the total score is computed and printed.
#----------------------------------------------------------#

from bowling02_Classes import *

bd = BowlingData()
try:
    while not(bd.isComplete()):
        bd.addFrame()
except Exception:
    print("User aborted.")
    raise

print("\n\n")
bd.printScores()






    








