# This class represents bowling data from a round of bowling.
# The number of frames in the round can be specified. The default is 10.
# It is a container for bowling frames, and instances can add frames until
# the number of frames in the round are complete.
# It is considered complete when all frames for the round have been added.
# If complete, there is a method to retrieve the total score.
# There are also methods to print the scores from the frames to the console
# or an output file.
# An alternate way of adding a complete dataset is provided which requires
# no user input, but instead a nested list that contains score information.
class BowlingData:
    """This class represents bowling data from a round of bowling. The number of frames in the round can be specified. The default is 10. It is a container for bowling frames, and instances can add frames until the number of frames in the round are complete. It is considered complete when all frames for the round have been added. If complete, there is a method to retrieve the total score. There are also methods to print the scores from the frames to the console or an output file. An alternate way of adding a complete dataset is provided which requires no user input, but instead a nested list that contains score information.   """
    nFramesPerRound = 10
    def __init__(self):
        """This is the initializer for this class."""
        self.frames = []
        self.nFrames = 0
        self.scoreIndByFrame = []
        self.scores = []
        self.totalScore = 0
        self.complete = False
  
    def reset(self):
        self.__init__()

    def isComplete(self):
        return self.complete

    def addFrame(self):
        if self.complete:
            print("Cannot add another frame. Score information for all " + str(self.nFramesPerRound) + " frames is complete.")
        else:
            # Add new frame, check whether to add a regular frame or last frame object.
            if self.nFrames == BowlingData.nFramesPerRound - 1:
                newFrame = LastFrame(self.nFrames+1)
            else:
                newFrame = RegularFrame(self.nFrames+1)
            while not(newFrame.isComplete()):
                newFrame.addShot()
            self.frames.append(newFrame)
            self.nFrames += 1
            
            # update attributes scoreIndByFrame and scores
            frameShots = self.frames[-1].getShots()
            shotInd = [] 
            shotScores = []
            shotIndexStart = len(self.scores)
            for i in range(len(frameShots)):
                shotInd.append(shotIndexStart + i)
                shotScores.append(frameShots[i].getScore())
            self.scoreIndByFrame.append(shotInd) 
            self.scores.extend(shotScores)

            # If last frame was just added, compute the total score and set as complete.
            if self.nFrames == BowlingData.nFramesPerRound:
                self.totalScore = self.getTotalScore()
                self.complete = True
            

    def getTotalScore(self):
        # Computes the total score from the frame data.
        # Requires the data set to be complete or else returns 0.
        #---------------------------------------------------------------------------------#
        
        # Score the input. Scoring scheme for each frame depends on the frame as well as whether it was
        # a strike, spare, or open frame.
        totalScore = 0
        if self.complete:
            # Computes on completed data set only.
            for iFrame in range(1,self.nFrames+1):
                frameScore = 0
                # Frames 1 through 9 and frame 10 scored differently
                if iFrame <= 10:
                    # Frames 1 through 9
                    # If strike or a spare, add this shot plus next two shots to score.
                    # This is equivalent to how a strike is scored and a spare is scored.
                    shotIndex = self.scoreIndByFrame[iFrame - 1][0]
                    if self.scores[shotIndex] == 10 or (self.scores[shotIndex] + self.scores[shotIndex+1]) == 10:
                        # strike or spare
                        frameScore = sum(self.scores[shotIndex:shotIndex+3]) 
                    else:
                        # Open - add the 2 shots from the frame
                        frameScore = sum(self.scores[shotIndex:shotIndex+2])
                totalScore += frameScore
        else:
            # Returns zero on incomplete data set.
            totalScore = 0

        return totalScore

    def writeScoresToFile(self,fout):
        # Writes the scores to the file opened by fout. It will fail if fout is closed or read only or invalid.
        # If the data set is not complete, writes out what data is available.
        # Parameters:
        # fout - file object for the output
        #
        # Output will look something like:
        # Frame 01:  3  3
        # Frame 02:  1  4
        # Frame 03:  1  1
        # Frame 04:  1  1
        # Frame 05:  0  2
        # Frame 06: 10
        # Frame 07:  7  3
        # Frame 08:  4  3
        # Frame 09:  1  3
        # Frame 10:  0  0
        # Score: 62        
        #

        for i in range(self.nFrames):
            frameScoresStr = "" # string that will have the scores from the shots on each frame
            frameShots = self.frames[i].getShots()
            scoreType = self.frames[i].getScoreType()
            for j in range(len(frameShots)):
                shotScore = frameShots[j].getScore()
                frameScoresStr += str("{0:2d}".format(shotScore) + " ")
            frameScoresStr = frameScoresStr[:-1] # Clips the last space character
            if scoreType == "strike":
                frameScoresStr += "   "
            fout.write("Frame {0:02d}: ".format(i+1) + frameScoresStr + "   " + scoreType + "\n")
        fout.write("Total Score: " + str(self.getTotalScore()))

    def printScores(self):
        # Outputs the scores to the console.
        # If the data set is not complete, writes out what data is available.
        # Parameters:
        # fout - file object for the output
        #
        # Output will look something like:
        # Frame 01:  3  3
        # Frame 02:  1  4
        # Frame 03:  1  1
        # Frame 04:  1  1
        # Frame 05:  0  2
        # Frame 06: 10
        # Frame 07:  7  3
        # Frame 08:  4  3
        # Frame 09:  1  3
        # Frame 10:  0  0
        # Score: 62        
        #

        for i in range(self.nFrames):
            frameScoresStr = "" # string that will have the scores from the shots on each frame
            frameShots = self.frames[i].getShots()
            scoreType = self.frames[i].getScoreType()
            for j in range(len(frameShots)):
                shotScore = frameShots[j].getScore()
                frameScoresStr += str("{0:2d}".format(shotScore) + " ")
            frameScoresStr = frameScoresStr[:-1] # Clips the last space character
            if scoreType == "strike":
                frameScoresStr += "   "
            print("Frame {0:02d}: ".format(i+1) + frameScoresStr + "   " + scoreType)
        print("Total Score: " + str(self.getTotalScore()))

        def isComplete(self):
            return self.complete

        def getNumberOfFrames(self):
            return self.nFrames

    def loadScores(self,pkd):
        # Takes in a nested list that has scores for each frame. The list must be 
        # BowlingData.nFramesPerRound in length. Each element should be a list with the 
        # scores for each frame. [[3,4],[9,1],[10],...]
        # By loading the data this way, all frames are added at once and do not
        # require user input. This is useful for testing, but could be useful for scoring
        # data in general.
        # 
        # Could not think of a way to do this without directly
        # accessing the attributes of frame and shot objects
        nFrames = BowlingData.nFramesPerRound
        self.scoreIndByFrame = [[] for i in range(nFrames)]
        self.scores = []
        shotIndex = 0
        # iterate through all the shot scores frame by frame
        for i in range(len(pkd)):
            for j in range(len(pkd[i])):
                self.scoreIndByFrame[i].append(shotIndex)
                self.scores.append(pkd[i][j])
                shotIndex += 1
        self.nFrames = nFrames
        self.complete = True
        self.totalScore = self.getTotalScore()
        for i in range(nFrames):
            shotScores = pkd[i]
            frameNumber = i+1
            nShots = len(shotScores)
            if nShots == 1:
                scoreType = "strike"
            elif nShots == 2 and sum(shotScores) == 10:
                scoreType = "spare"
            else:
                scoreType = "open"
            
            shots = []
            for j in range(nShots):
                shotNumber = j+1
                pinsStandingBeforeShot = 10-shotScores[j]
                shot = BowlingShot(frameNumber,shotNumber,pinsStandingBeforeShot)
                shot.score = shotScores[j]
                shot.complete = True
                shots.append(shot)

            if i == nFrames-1:
                # Last frame
                frame = LastFrame(frameNumber)
            else:
                frame = RegularFrame(frameNumber)
            
            frame.scoreType = scoreType
            frame.shots = shots
            frame.nShots = nShots
            frame.complete = True

            self.frames.append(frame)
        


# This class represents a bowling shot. It contains a score attribute which is initially zero, and
# a method to retrieve user input to record the score for the shot.
class BowlingShot:
    def __init__(self, frameNumber, shotNumber, pinsStandingBeforeShot) -> None:
        self.nFrames = BowlingData.nFramesPerRound # number of frames in round
        self.frameNumber = frameNumber # which frame, 1 to nFrames
        self.shotNumber = shotNumber # which shot, 1 to 3
        self.pinsStandingBeforeShot = pinsStandingBeforeShot # the number of pins standing when shot taken
        self.score = 0 # the number of pins knocked down after shot taken
        self.complete = False

        # Guards on attributes
        if frameNumber < 1 or frameNumber > self.nFrames:
            raise Exception("Error: BowlingShot->getUserInput() 'frameNumber' out of bounds.")
        if shotNumber < 1 or shotNumber > 3:
            raise Exception("Error: BowlingShot->getUserInput() 'shot' out of bounds.")
        if pinsStandingBeforeShot < 0 or pinsStandingBeforeShot > 10:
            raise Exception("Error: BowlingShot->getUserInput() 'pinsStandingBeforeShot' out of bounds")

    def setScore(self,score):
        self.score = score
        self.complete = True
    
    def getScore(self):
        if self.complete:
            return self.score
        else:
            raise Exception("Error: BowlingShot->getScore - data for shot not recorded yet.")

    def getScoreFromUser(self):
        # Prompts the user for the number of pins kncocked down on a particular frame and shot.
        # Returns an integer value representing the number of pins knocked down as entered by the user.
        # Parameters:
        # nFrames - number of frames
        # frame - which frame, 1 to nFrames
        # shot - which shot, 1 to 3
        # maxPins - restricts the maximum pins to enter as knocked down. Takes a value between 0 and 10.

        # Prompts until a valid input is entered. Range is 0 to pinsStandingBeforeShot pins. 
        validInput = False
        x = ""
        while not validInput:
            x = input("Frame " + str(self.frameNumber) + " Shot " + str(self.shotNumber) + ": ")
            if x == "q":
                raise Exception("Error: User abort.")
            else:
                # input should be an integer value within bounds
                try:
                    if int(x) >= 0 and int(x) <= self.pinsStandingBeforeShot:
                        validInput = True
                    else:
                        print("Invalid input, please try again.")
                except ValueError:
                        print("Invalid input, please try again.")
        self.score = int(x)
        self.complete = True      

    def isComplete(self):
        return self.complete



# This class represents a bowling frame. It is a parent class for two derived classes, RegularFrame and LastFrame.
# It is a container for bowling shots.
class BowlingFrame:
    def __init__(self,frameNumber) -> None:
        self.frameNumber = frameNumber
        self.scoreType = "" # Open, Spare, or Strike as defined in requirements. For tenth frame, Strike takes precedence over spare.
        self.shots = [] # List of BowlingShots in order of occurence for this frame.
        self.nShots = 0
        self.complete = False # when the frame is complete this is true. All the scores for the shots taken on the frame have been collected.

    def addShot(self):
        pass
     
    def getShots(self):
        return self.shots

    def getNumberOfShots(self):
        return self.nShots

    def isComplete(self):
        return self.complete
    
    def getScoreType(self):
        return self.scoreType


# This class represents frames in which there are two shots possible.
class RegularFrame(BowlingFrame):
    def __init__(self, frameNumber) -> None:
        super().__init__(frameNumber)

    def addShot(self):
        # Creates the shot, gets user to score the shot, and adds it to the list of shots.
        # If the first shot is a strike, it marks it as complete with one shot.
        # If the first shot is not a strike, then it remains incomplete and open for another shot.
        # If the second shot gets the rest of the pins, it is a spare, otherwise open.
        # Upon the second shot, it is marked as complete. 
        # The user is given feedback about the type of the frame when it is determined, open, strike, or spare.
        if self.complete:
            print("Cannot add a shot to this frame. This frame is complete.")
        else:
            if self.nShots == 0:
                # no shots have been taken yet this frame
                pinsStandingBeforeShot = 10
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pinsStandingBeforeShot)
                shot.getScoreFromUser()
                self.shots.append(shot)
                if shot.getScore() == 10:
                    print("Strike!")
                    self.scoreType = "strike"
                    self.complete = True
            elif self.nShots == 1:
                # one shot taken already
                pinsStandingBeforeShot = 10-self.shots[0].getScore()
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pinsStandingBeforeShot)
                shot.getScoreFromUser()
                self.shots.append(shot)
                if self.shots[0].getScore() + self.shots[1].getScore() == 10:
                    print("Spare!")
                    self.scoreType = "spare"
                else:
                    print("Open.")
                    self.scoreType = "open"
                self.complete = True

# This class represents the last frame in which there are three shots possible.
class LastFrame(BowlingFrame):
    def __init__(self, frameNumber) -> None:
        super().__init__(frameNumber)

    def addShot(self):
        # Creates the shot, gets user to score the shot, and adds it to the list of shots.
        # If the first shot is a strike, it marks it as incomplete with two shots following, and pins are reset.
        # If the first shot is not a strike, then it remains incomplete and open for another shot for a possible spare.
        # If the second shot gets the rest of the pins for a spare, or a second strike, it is reset for another shot.
        # If neither a spare or strike occurs on the first two shots, the frame is complete and marked as open.
        # If there is a third shot, whatever the outcome, the frame is marked as complete.
        # The user is given feedback about the type of the frame when it is determined, open, strike, or spare.
        if self.complete:
            print("Cannot add a shot to this frame. This frame is complete.")
        else:
            if self.nShots == 0:
                # no shots have been taken yet this frame
                pinsStandingBeforeShot = 10
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pinsStandingBeforeShot)
                shot.getScoreFromUser()
                self.shots.append(shot)
                if shot.getScore() == 10:
                    print("Strike!")
                    self.scoreType = "strike"
            elif self.nShots == 1:
                # one shot taken already
                # if first shot was a strike, pins reset.
                if self.shots[0].getScore() == 10:
                    pinsStandingBeforeShot = 10
                else:
                    pinsStandingBeforeShot = 10-self.shots[0].getScore()
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pinsStandingBeforeShot)
                shot.getScoreFromUser()
                self.shots.append(shot)
                if shot.getScore() == 10:
                    print("Strike!")
                elif self.shots[0].getScore() + self.shots[1].getScore() == 10:
                    print("Spare!")
                    self.scoreType = "spare"
                elif self.shots[0].getScore() + self.shots[1].getScore() < 10:
                    print("Open.")
                    self.scoreType = "open"
                    self.complete = True
            elif self.nShots == 2:
                # two shots taken already
                # this means a strike or spare must have been scored
                # and so the pins must be reset
                pinsStandingBeforeShot = 10
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pinsStandingBeforeShot)
                shot.getScoreFromUser()
                self.shots.append(shot)
                if shot.getScore() == 10:
                    print("Strike!")
                else:
                    print("Open.")
                
                self.complete = True

