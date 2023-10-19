#This is the terminal project for Codecademy

print("Welcome to Maze Game")
print("Dev, V. 0.0.3\n\n")

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
        self.dimension = self.dimension_calculator()
        
        
    def door_status_text(self, door):
        if door== 0:
           return "Door not opened yet."
        else:
           return "Door has already been opened. Leads to Rm:??"
  
    
    
    def backroom_number_calculator(self):
        if self.back_door==1:
            return 1
        else:
            return self.back_door.id
        
        
    def __repr__(self):
        info=''' ------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n'''
          
        info+="This is Maze Room #{mazenumber}.\n".format(mazenumber= self.id)
        info +="There is {prize} as the main item in the room.\n".format(prize= self.prize) 
        
        
        info+='''\nHere are the status of the doors: 
                                                    Room Number     : {room_number}
                                                    Left Door       : {left_door}
                                                    Front Door      : {front_door}
                                                    Right Door      : {right_door}
                                                    Room Dimension  : {dimension_number}
                                                    Back Door       : {parent_rm_number}
   
        '''.format(
            room_number= self.id, 
            left_door=self.door_status_text(self.left_door), 
            front_door = self.door_status_text(self.front_door),
            right_door= self.door_status_text(self.right_door),
            dimension_number=self.dimension,
            parent_rm_number= self.backroom_number_calculator()
        )
                  
        return info
        
    def dimension_calculator(self):
        #this will count how many generation this room is aka how many backdoors 
        back_tracker=0
        room_pointer=self
        while room_pointer.back_door != 1:
            back_tracker += 1
            room_pointer = room_pointer.back_door 
         
        return back_tracker 

            
        
#start the game, intro and first input?

# testmaze= MazeRoom(0)
# print(testmaze)
# print(testmaze)

print('''You have entered the multiverse maze, you will need to find the hidden treasure deep inside this maze. 
There are 4 doors in a room and each door will lead to a new room except the back door. 
You can go back and forth and try all the path you wish.''')

dimension_number = input("How many layers of Dimensions can you search?\n") 

input("Press Enter to Open the First Door\n") 

first_maze_door= MazeRoom(1)
sdsds_maze_door=MazeRoom(1)
sdddd= MazeRoom(1)

print("\nFirst Door opened! Good Luck")
print(first_maze_door)
print(sdsds_maze_door)
print(sdddd)

#starting iteration and game logic
current_room =first_maze_door



while current_room.prize == 0 :
    # tmp_left= current_room.left_door
    # tmp_front= current_room.front_door
    # tmp_right= current_room.right_door  
    # tmp_back= current_room.back_door
    
    #dooroptions = { 'a':left, 'w': front,'d' :right,'s': back} 
    
    print(current_room)
    print('''What door will you open?''')
    door_choice = input("Enter to Choose { a, w, d, s }")
    #if door_choice != "a" or door_choice
    
    
    
    current_room.prize=1