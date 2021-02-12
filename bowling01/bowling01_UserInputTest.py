# bowling01 - User Input Testing
from io import RawIOBase
from bowling01_Functions import *

nFrames = 10

# getUserInput - out of lower and upper bounds, within bounds
print("Enter pins knocked down below 0, then above 10, then within bounds.")
frameNumber = 5
shotNumber = 2
pinsStanding = 10
x = getUserInput(nFrames, frameNumber, shotNumber, pinsStanding)
print(x)

# getUserInput - out of lower and upper bounds, within bounds
print("Enter 0,1,2,3,4,5,6,7,8,9,10 for 11 total entries.")
for i in range(11):
    frameNumber = i%10 + 1
    shotNumber = 1
    pinsStanding = 10
    x = getUserInput(nFrames, frameNumber, shotNumber, pinsStanding)
print(x)

# getUserInput - restricted upper bound from number of pins left
print("Enter pins knocked down between 5 and 10. Then enter a value between 0 and 4.")
frameNumber = 7
shotNumber = 1
pinsStanding = 4
x = getUserInput(nFrames, frameNumber, shotNumber, pinsStanding)
print(x)

# getUserInput - out of lower and upper bound
print("Enter any non-integer string and not the letter 'q'. Then enter a number within bounds.")
frameNumber = 8
shotNumber = 2
pinsStanding = 10
x = getUserInput(nFrames, frameNumber, shotNumber, pinsStanding)
print(x)

# getUserInput - q to abort
try:
    print("Enter q to abort.")
    frameNumber = 9
    shotNumber = 1
    pinsStanding = 10
    x = getUserInput(nFrames, frameNumber, shotNumber, pinsStanding)
except Exception:
    print("User aborted.")
    raise


