# Bowling01 Scoring Tests
from bowling01_Functions import *
from random import randint,seed


seed(99) # Change this seed to produce different test cases.

nTestCases = 15
t = [[] for i in range(nTestCases)]

# get_score Frames 1 to 9, 9 cases with 10th frame score always zero
# 0) All Open
for iFrame in range(9):
    a = randint(0,9) # first shot
    b = randint(0,10-a-1) # 2nd shot, upper bound to preclude spare
    t[0].append([a,b])
t[0].append([0,0])

# 1) 1 Strike
t[1] = t[0].copy()
t[1][randint(0,8)] = [10]

# 2) 1 Spare
t[2] = t[0].copy()
a = randint(0,9) # first shot
t[2][randint(0,8)] = [a, 10-a] 

# 3) 2 consecutive strikes
t[3] = t[0].copy()
ind = randint(0,7)
t[3][ind] = [10]
t[3][ind+1] = [10]

# 4) 2 consecutive spares 
t[4] = t[0].copy()
a = randint(0,9) # first shot first frame
b = randint(0,9) # first shot second frame
ind = randint(0,7)
t[4][ind] = [a, 10-a] 
t[4][ind+1] = [b, 10-b]

# 5) 3 consecutuve strikes
t[5] = t[0].copy()
ind = randint(0,6)
t[5][ind] = [10] # first frame
t[5][ind+1] = [10] # second frame
t[5][ind+2] = [10] # third frame

# 6) 3 consecutive spares
t[6] = t[0].copy()
a = randint(0,9) # first shot first frame
b = randint(0,9) # first shot second frame
c = randint(0,9) # first shot third frame
ind = randint(0,7)
t[6][ind] = [a, 10-a] 
t[6][ind+1] = [b, 10-b]
t[6][ind+2] = [c, 10-c]

# 7) strike then spare
t[7] = t[0].copy()
a = randint(0,10)
ind = randint(0,7)
t[7][ind] = [10] # first frame
t[7][ind+1] = [a,10-a] # second frame

# 8) spare then strike
t[8] = t[0].copy()
a = randint(0,10)
ind = randint(0,7)
t[8][ind] = [a,10-a] # first frame
t[8][ind+1] = [10] # second frame

# get_score Frame 10, 3 cases, frames 1 through 9 are open and zero
# 9) 10th Frame Open, 2 shots, < 10 total
t[9] = [[0,0] for i in range(9)]
a = randint(0,9) # first shot
b = randint(0,10-a-1) # second shot, upper bound to make sure it is not a spare
t[9].append([a,b])

# 10) 10th Frame spare + 1 shot
t[10] = [[0,0] for i in range(9)]
a = randint(0,9) # first shot
t[10].append([a,10-a,randint(0,10)])

# 11) 10th Frame strike + 2 shots
t[11] = [[0,0] for i in range(9)]
t[11].append([10,randint(0,10), randint(0,10)])

#---#

# get_score 2 cases, all strikes and all spares
# 12) all strikes
t[12] = [[10] for i in range(10)]

# 13) all spares
for iFrame in range(10):
    a = randint(0,9) # first shot
    t[13].append([a,10-a])

#---#

# 14) all random open, spare, or strike
for iFrame in range(10):
    a = randint(0,10) # first shot
    b = randint(0,10-a) # second shot
    if a == 10:
        t[14].append([a]) # strike
    else:
        t[14].append([a,b]) # open or spare



testCaseStr = ["0: all open",
                "1: 1 strike",
                "2: 1 spare",
                "3: 2 consecutive strikes",
                "4: 2 consecutive spares",
                "5: 3 consecutive strikes",
                "6: 3 consecutive spares",
                "7: strike then spare",
                "8: spare then strike",
                "9: open, 2 shots, < 10 total",
                "10: spare + 1 shot",
                "11: strike + 2 shots",
                "12: all strikes",
                "13: all spares",
                "14: all random"
                ]


with open("bowling01_test_output.txt",'w') as f:
    f.write("Frames 1 to 9, Last Frame 0: 9 test cases\n")
    f.write("10th Frame testing: 3 test cases\n")
    for iTestCase in range(nTestCases):
        f.write(testCaseStr[iTestCase] + "\n")
    f.write("\n\n")
    for iTestCase in range(nTestCases):
        pkd = t[iTestCase]
        f.write("Test Case " + testCaseStr[iTestCase] + "\n")
        writePinsDownData(f,pkd)
        f.write("Score: " + str(getScore(pkd)))
        f.write("\n----------------------------------\n")
