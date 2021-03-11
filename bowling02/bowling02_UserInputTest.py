# bowling01 - User Input Testing
from bowling02_Classes import *

bd = BowlingData()

 #  out of lower and upper bounds, within bounds
print("Enter pins knocked down below 0, then above 10, then within bounds.")
bd.add_frame()

# out of lower and upper bounds, within bounds
bd.add_frame()

# restricted upper bound
bd.add_frame()

# reset
bd.reset()

# q to abort
bd.add_frame()


