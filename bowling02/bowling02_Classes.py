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
    """This class represents bowling data from a round of bowling. The number of frames in the round can be
    specified. The default is 10. It is a container for bowling frames, and instances can add frames until the number
    of frames in the round are complete. It is considered complete when all frames for the round have been added. If
    complete, there is a method to retrieve the total score. There are also methods to print the scores from the
    frames to the console or an output file. An alternate way of adding a complete dataset is provided which requires
    no user input, but instead a nested list that contains score information. """
    n_frames_per_round = 10

    def __init__(self):
        """This is the initializer for this class."""
        self.frames = []
        self.n_frames = 0
        self.score_ind_by_frame = []
        self.scores = []
        self.total_score = 0
        self.complete = False
  
    def reset(self):
        self.__init__()

    def is_complete(self):
        return self.complete

    def add_frame(self):
        if self.complete:
            print("Cannot add another frame. Score information for all " + str(self.n_frames_per_round) + "frames is "
                                                                                                          "complete.")
        else:
            # Add new frame, check whether to add a regular frame or last frame object.
            if self.n_frames == BowlingData.n_frames_per_round - 1:
                new_frame = LastFrame(self.n_frames + 1)
            else:
                new_frame = RegularFrame(self.n_frames + 1)
            while not(new_frame.is_complete()):
                new_frame.add_shot()
            self.frames.append(new_frame)
            self.n_frames += 1
            
            # update attributes score_ind_by_frame and scores
            frame_shots = self.frames[-1].get_shots()
            shot_ind = []
            shot_scores = []
            shot_index_start = len(self.scores)
            for i in range(len(frame_shots)):
                shot_ind.append(shot_index_start + i)
                shot_scores.append(frame_shots[i].get_score())
            self.score_ind_by_frame.append(shot_ind)
            self.scores.extend(shot_scores)

            # If last frame was just added, compute the total score and set as complete.
            if self.n_frames == BowlingData.n_frames_per_round:
                self.total_score = self.get_total_score()
                self.complete = True
            

    def get_total_score(self):
        # Computes the total score from the frame data.
        # Requires the data set to be complete or else returns 0.
        #---------------------------------------------------------------------------------#
        
        # Score the input. Scoring scheme for each frame depends on the frame as well as whether it was
        # a strike, spare, or open frame.
        total_score = 0
        if self.complete:
            # Computes on completed data set only.
            for iFrame in range(1, self.n_frames + 1):
                frame_score = 0
                # Frames 1 through 9 and frame 10 scored differently
                if iFrame <= 10:
                    # Frames 1 through 9
                    # If strike or a spare, add this shot plus next two shots to score.
                    # This is equivalent to how a strike is scored and a spare is scored.
                    shot_index = self.score_ind_by_frame[iFrame - 1][0]
                    if self.scores[shot_index] == 10 or (self.scores[shot_index] + self.scores[shot_index+1]) == 10:
                        # strike or spare
                        frame_score = sum(self.scores[shot_index:shot_index+3])
                    else:
                        # Open - add the 2 shots from the frame
                        frame_score = sum(self.scores[shot_index:shot_index+2])
                total_score += frame_score
        else:
            # Returns zero on incomplete data set.
            total_score = 0

        return total_score

    def write_scores_to_file(self, fout):
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

        for i in range(self.n_frames):
            frame_scores_str = "" # string that will have the scores from the shots on each frame
            frame_shots = self.frames[i].get_shots()
            score_type = self.frames[i].get_score_type()
            for j in range(len(frame_shots)):
                shot_score = frame_shots[j].get_score()
                frame_scores_str += str("{0:2d}".format(shot_score) + " ")
            frame_scores_str = frame_scores_str[:-1] # Clips the last space character
            if score_type == "strike":
                frame_scores_str += "   "
            fout.write("Frame {0:02d}: ".format(i+1) + frame_scores_str + "   " + score_type + "\n")
        fout.write("Total Score: " + str(self.get_total_score()))

    def print_scores(self):
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

        for i in range(self.n_frames):
            frame_scores_str = ""  # string that will have the scores from the shots on each frame
            frame_shots = self.frames[i].get_shots()
            score_type = self.frames[i].get_score_type()
            for j in range(len(frame_shots)):
                shot_score = frame_shots[j].get_score()
                frame_scores_str += str("{0:2d}".format(shot_score) + " ")
            frame_scores_str = frame_scores_str[:-1] # Clips the last space character
            if score_type == "strike":
                frame_scores_str += "   "
            print("Frame {0:02d}: ".format(i+1) + frame_scores_str + "   " + score_type)
        print("Total Score: " + str(self.get_total_score()))

        def is_complete(self):
            return self.complete

        def get_number_of_frames(self):
            return self.n_frames

    def load_scores(self, pkd):
        # Takes in a nested list that has scores for each frame. The list must be 
        # BowlingData.nFramesPerRound in length. Each element should be a list with the 
        # scores for each frame. [[3,4],[9,1],[10],...]
        # By loading the data this way, all frames are added at once and do not
        # require user input. This is useful for testing, but could be useful for scoring
        # data in general.
        # 
        # Could not think of a way to do this without directly
        # accessing the attributes of frame and shot objects
        n_frames = BowlingData.n_frames_per_round
        self.score_ind_by_frame = [[] for i in range(n_frames)]
        self.scores = []
        shot_index = 0
        # iterate through all the shot scores frame by frame
        for i in range(len(pkd)):
            for j in range(len(pkd[i])):
                self.score_ind_by_frame[i].append(shot_index)
                self.scores.append(pkd[i][j])
                shot_index += 1
        self.n_frames = n_frames
        self.complete = True
        self.total_score = self.get_total_score()
        for i in range(n_frames):
            shot_scores = pkd[i]
            frame_number = i+1
            n_shots = len(shot_scores)
            if n_shots == 1:
                score_type = "strike"
            elif n_shots == 2 and sum(shot_scores) == 10:
                score_type = "spare"
            else:
                score_type = "open"
            
            shots = []
            for j in range(n_shots):
                shot_number = j+1
                pins_standing_before_shot = 10-shot_scores[j]
                shot = BowlingShot(frame_number, shot_number, pins_standing_before_shot)
                shot.score = shot_scores[j]
                shot.complete = True
                shots.append(shot)

            if i == n_frames-1:
                # Last frame
                frame = LastFrame(frame_number)
            else:
                frame = RegularFrame(frame_number)
            
            frame.scoreType = score_type
            frame.shots = shots
            frame.nShots = n_shots
            frame.complete = True

            self.frames.append(frame)
        

# This class represents a bowling shot. It contains a score attribute which is initially zero, and
# a method to retrieve user input to record the score for the shot.
class BowlingShot:
    def __init__(self, frame_number, shot_number, pins_standing_before_shot) -> None:
        self.n_frames = BowlingData.n_frames_per_round  # number of frames in round
        self.frame_number = frame_number  # which frame, 1 to n_frames
        self.shot_number = shot_number  # which shot, 1 to 3
        self.pins_standing_before_shot = pins_standing_before_shot  # the number of pins standing when shot taken
        self.score = 0  # the number of pins knocked down after shot taken
        self.complete = False

        # Guards on attributes
        if frame_number < 1 or frame_number > self.n_frames:
            raise Exception("Error: BowlingShot->getUserInput() 'frame_number' out of bounds.")
        if shot_number < 1 or shot_number > 3:
            raise Exception("Error: BowlingShot->getUserInput() 'shot' out of bounds.")
        if pins_standing_before_shot < 0 or pins_standing_before_shot > 10:
            raise Exception("Error: BowlingShot->getUserInput() 'pins_standing_before_shot' out of bounds")

    def set_score(self, score):
        self.score = score
        self.complete = True
    
    def get_score(self):
        if self.complete:
            return self.score
        else:
            raise Exception("Error: BowlingShot->get_score - data for shot not recorded yet.")

    def get_score_from_user(self):
        # Prompts the user for the number of pins knocked down on a particular frame and shot.
        # Returns an integer value representing the number of pins knocked down as entered by the user.
        # Parameters:
        # n_frames - number of frames
        # frame - which frame, 1 to n_frames
        # shot - which shot, 1 to 3
        # maxPins - restricts the maximum pins to enter as knocked down. Takes a value between 0 and 10.

        # Prompts until a valid input is entered. Range is 0 to pins_standing_before_shot pins.
        valid_input = False
        x = ""
        while not valid_input:
            x = input("Frame " + str(self.frame_number) + " Shot " + str(self.shot_number) + ": ")
            if x == "q":
                raise Exception("Error: User abort.")
            else:
                # input should be an integer value within bounds
                try:
                    if 0 <= int(x) <= self.pins_standing_before_shot:
                        valid_input = True
                    else:
                        print("Invalid input, please try again.")
                except ValueError:
                        print("Invalid input, please try again.")
        self.score = int(x)
        self.complete = True      

    def is_complete(self):
        return self.complete


# This class represents a bowling frame. It is a parent class for two derived classes, RegularFrame and LastFrame.
# It is a container for bowling shots.
class BowlingFrame:
    def __init__(self, frame_number) -> None:
        self.frameNumber = frame_number
        self.scoreType = "" # Open, Spare, or Strike as defined in requirements. For tenth frame, Strike takes precedence over spare.
        self.shots = [] # List of BowlingShots in order of occurence for this frame.
        self.nShots = 0
        self.complete = False # when the frame is complete this is true. All the scores for the shots taken on the frame have been collected.

    def add_shot(self):
        pass
     
    def get_shots(self):
        return self.shots

    def get_number_of_shots(self):
        return self.nShots

    def is_complete(self):
        return self.complete
    
    def get_score_type(self):
        return self.scoreType


# This class represents frames in which there are two shots possible.
class RegularFrame(BowlingFrame):
    def __init__(self, frame_number) -> None:
        super().__init__(frame_number)

    def add_shot(self):
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
                pins_standing_before_shot = 10
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pins_standing_before_shot)
                shot.get_score_from_user()
                self.shots.append(shot)
                if shot.get_score() == 10:
                    print("Strike!")
                    self.scoreType = "strike"
                    self.complete = True
            elif self.nShots == 1:
                # one shot taken already
                pins_standing_before_shot = 10-self.shots[0].get_score()
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pins_standing_before_shot)
                shot.get_score_from_user()
                self.shots.append(shot)
                if self.shots[0].get_score() + self.shots[1].get_score() == 10:
                    print("Spare!")
                    self.scoreType = "spare"
                else:
                    print("Open.")
                    self.scoreType = "open"
                self.complete = True



class LastFrame(BowlingFrame):
    """This class represents the last frame in which there are three shots possible."""
    def __init__(self, frame_number) -> None:
        super().__init__(frame_number)

    def add_shot(self):
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
                pins_standing_before_shot = 10
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pins_standing_before_shot)
                shot.get_score_from_user()
                self.shots.append(shot)
                if shot.get_score() == 10:
                    print("Strike!")
                    self.scoreType = "strike"
            elif self.nShots == 1:
                # one shot taken already
                # if first shot was a strike, pins reset.
                if self.shots[0].get_score() == 10:
                    pins_standing_before_shot = 10
                else:
                    pins_standing_before_shot = 10-self.shots[0].get_score()
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pins_standing_before_shot)
                shot.get_score_from_user()
                self.shots.append(shot)
                if shot.get_score() == 10:
                    print("Strike!")
                elif self.shots[0].get_score() + self.shots[1].get_score() == 10:
                    print("Spare!")
                    self.scoreType = "spare"
                elif self.shots[0].get_score() + self.shots[1].get_score() < 10:
                    print("Open.")
                    self.scoreType = "open"
                    self.complete = True
            elif self.nShots == 2:
                # two shots taken already
                # this means a strike or spare must have been scored
                # and so the pins must be reset
                pins_standing_before_shot = 10
                self.nShots += 1
                shot = BowlingShot(self.frameNumber, self.nShots, pins_standing_before_shot)
                shot.get_score_from_user()
                self.shots.append(shot)
                if shot.get_score() == 10:
                    print("Strike!")
                else:
                    print("Open.")
                
                self.complete = True

