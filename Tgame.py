#This is the terminal project for Codecademy

print("okokok")

print("Welcome to Maze Game")
print("Dev, V. 0.0.1")

#working on the class for each maze square

class MazeRoom:
    Totalrooms=0
    
    def __init__(self, back_door):
        self.back_door= back_door
        self.front_door =0
        self.right_door =0
        self.left_door=0
        self.prize =0
        MazeRoom.Totalrooms += 1
        self.id = MazeRoom.Totalrooms
        
    def __repr__(self):
        info="This is Maze Room mazenumber"
    
#start the game?