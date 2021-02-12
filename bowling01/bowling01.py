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

from sys import exit
from bowling01_Functions import *

# Data structure to hold how many pins knocked down.
# Nested list. Each frame is length number of shots in that frame to be 
# deterimined by the data. The max number of shots is 2 for frames 1 
# through 9, and 3 for frame 10.
pinsKnockedDown = []

# Iterate through the frames and populate with performance data from user input
try:
    nFrames = 10
    for iFrame in range(1,nFrames+1):
        print(iFrame)
        shots = []
        # Frames 1 through 8 are in one class, Frame 9 is one class, Frame 10 is
        # in another. They are each treated differently.
        # Each frame has possibility for being strike, spare, or open.
        if iFrame < 10: 
            # First 9 frames
            shots.append(getUserInput(nFrames, iFrame, 1, 10))
            if shots[0] == 10: 
                # Strike, there is no second shot.
                print("Strike!")
            else: 
                # Open Frame or Spare, does not matter which until scoring.
                # Number of max pins to enter restricted since one shot already taken.
                # That is the sum of scores on an open frame must always be <= 10.
                shots.append(getUserInput(nFrames, iFrame, 2, 10 - shots[0]))
                if shots[0] + shots[1] == 10:
                    # Spare
                    print("Spare!")
                else:
                    # No spare so Open frame
                    print("Open Frame")
        else:
            # 10th Frame
            shots.append(getUserInput(nFrames, iFrame, 1, 10))
            if shots[0] == 10:
                # Strike, grants two more shots.
                print("Strike!")
                shots.append(getUserInput(nFrames, iFrame, 2, 10))
                if shots[1] == 10:
                    print("Strike!")
                shots.append(getUserInput(nFrames, iFrame, 3, 10))
                if shots[2] == 10:
                    print("Strike!:")
            else:
                # No strike on the first shot, spare possible
                shots.append(getUserInput(nFrames, iFrame, 2, 10-shots[0]))
                if shots[0] + shots[1] == 10:
                    # spare, grants one more shot.
                    shots.append(getUserInput(nFrames, iFrame, 3, 10))
                else:
                    # No spare means open frame, no third shot granted.
                    print("Open Frame")

        pinsKnockedDown.append(shots)
except Exception:
    print("User aborted.")
    raise


finalScore = getScore(pinsKnockedDown)

print("pinsKnockedDown = " + str(pinsKnockedDown))

print("finalScore = " + str(finalScore))


    








