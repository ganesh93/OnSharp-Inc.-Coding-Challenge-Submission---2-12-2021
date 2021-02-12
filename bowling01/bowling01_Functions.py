#------------------------------------------------------------------------------------#
def getUserInput(nFrames,frame,shot,maxPins):
    # Prompts the user for the number of pins kncocked down on a particular frame and shot.
    # Returns an integer value representing the number of pins knocked down as entered by the user.
    # Parameters:
    # nFrames - number of frames
    # frame - which frame, 1 to nFrames
    # shot - which shot, 1 to 3
    # maxPins - restricts the maximum pins to enter as knocked down. Takes a value between 0 and 10.

    # Guards on parameters
    if frame < 1 or frame > nFrames:
        raise Exception("Error: getUserInput 'frame' out of bounds.")
    if shot < 1 or shot > 3:
        raise Exception("Error: getUserInput 'shot' out of bounds.")
    if maxPins < 0 or maxPins > 10:
        raise Exception("Error: getUserInput 'maxPins' out of bounds")

    # Prompts until a valid input is entered. Range is 0 to maxPins pins. 
    validInput = False
    x = ""
    while not validInput:
        x = input("Frame " + str(frame) + " Shot " + str(shot) + ": ")
        if x == "q":
            raise Exception("Error: User abort.")
        else:
            # input should be an integer value within bounds
            try:
                if int(x) >= 0 and int(x) <= maxPins:
                    validInput = True
                else:
                    print("Invalid input, please try again.")
            except ValueError:
                    print("Invalid input, please try again.")
    return int(x)

def getScore(pkd):
    # Scored the bowling data stored in scoreCard
    # pkd - shot scores organized by frame. Nested list. List with nFrame number 
    #       of list elements. Each elent is a list of integers representing the 
    #       scores for the shots taken in that frame.    
    #---------------------------------------------------------------------------------#
    
    # Score the input. Scoring scheme for each frame depends on the frame as well as whether it was
    # a strike, spare, or open frame.
    nFrames = 10
    frameShotInd,shotScores = refactorData(pkd)
    totalScore = 0
    for iFrame in range(1,nFrames+1):
        frameScore = 0
        # Frames 1 through 9 and frame 10 scored differently
        if iFrame <= 10:
            # Frames 1 through 9
            # If strike or a spare, add this shot plus next two shots to score.
            # This is equivalent to how a strike is scored and a spare is scored.
            shotIndex = frameShotInd[iFrame - 1][0]
            if shotScores[shotIndex] == 10 or (shotScores[shotIndex] + shotScores[shotIndex+1]) == 10:
                # strike or spare
                frameScore = sum(shotScores[shotIndex:shotIndex+3]) 
            else:
                # Open - add the 2 shots from the frame
                frameScore = sum(shotScores[shotIndex:shotIndex+2])
        totalScore += frameScore
    
    return totalScore


def writePinsDownData(fout, pkd):
    # This function outputs to the file specified by fout the data in pkd (pins knocked down).
    # Parameters:
    # fout - file handle for the output
    # pkd - shot scores organized by frame. Nested list. List with nFrame number 
    #       of list elements. Each elent is a list of integers representing the 
    #       scores for the shots taken in that frame.
    nFrames = 10
    for iFrame in range(1,nFrames+1):
        framePinCountStr = ""
        frameShots = pkd[iFrame-1]
        for iShot in range(1,len(frameShots)+1):
            framePinCountStr += str("{0:2d}".format(frameShots[iShot-1]) + " ")
        framePinCountStr = framePinCountStr[:-1] # Clips the last space character
        fout.write("Frame {0:02d}: ".format(iFrame) + framePinCountStr + "\n")


def refactorData(pkd):
    # Returns a tuple with data in a different format which simplifies the 
    # scoring logic.
    # Paramters:
    # pkd - shot scores organized by frame. Nested list. List with nFrame number 
    #       of list elements. Each elent is a list of integers representing the 
    #       scores for the shots taken in that frame.
    #
    # Return Values:
    # shotIndByFrame - List of lists. Stores an index for each shot taken on
    #                  each frame. List is nFrames in length. Each element is
    #                  a list of indices that correspond to each shot taken in
    #                  frame. The index refers to anotbher list that has all
    #                  scores for every shot taken.
    # shotScores - A list of pins knocked down for every shot taken in order
    #              from first to last. There is no frame information here.
    nFrames = 10
    shotIndByFrame = [[] for i in range(nFrames)]
    shotScores = []
    shotIndex = 0
    # iterate through all the shot scores frame by frame
    for i in range(len(pkd)):
        for j in range(len(pkd[i])):
            shotIndByFrame[i].append(shotIndex)
            shotScores.append(pkd[i][j])
            shotIndex += 1
    return shotIndByFrame,shotScores

# ------------------------------------------------------------------------------------------#