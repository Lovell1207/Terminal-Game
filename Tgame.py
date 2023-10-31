#This is the terminal project for Codecademy
import datetime
import random

print('''
 +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+
 |W|e|l|c|o|m|e| |t|o| |t|h|e| |M|a|z|e| |G|a|m|e|
 +-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+
''')
#print("Dev, V. 0.0.7\n\n")
print("Ver. 1.0\n\n")
    
#Class for each maze square
class MazeRoom:
    Totalrooms=0
    
    def __init__(self, back_door):
        self.back_door= back_door
        self.front_door =0
        self.right_door =0
        self.left_door=0
        self.prize = generate_prize(back_door, self.Totalrooms, max_rooms)
        MazeRoom.Totalrooms += 1
        self.id = MazeRoom.Totalrooms
        self.dimension = self.dimension_calculator() 
                 
    def door_status_text(self, door):
        if door== 0:
           return "Door not opened yet."
        else:
           return ("Leads to Rm:{id}.".format(id= door.id))
  
    def door_status_Isopen(self, door):
        if door== 0:
           return False
        else:
           return True    
    
    def backroom_number_calculator(self):
        if self.back_door==1:
            return 1
        else:
            return self.back_door.id
        
        
    def __repr__(self):
        info='''\n----------------------------------------------------------------------------------------------------------------------\n\n'''
          
        info+="This is Maze Room #{mazenumber}.\n".format(mazenumber= self.id)
        info +="There is {prize} as the main item in the room.\n".format(prize= self.prize) 
        
        if(self.dimension >= dimension_number):
            info+='''\nHere are the status of the doors: 
                                                        Room Number     : {room_number}
                                                        Left Door       : No Door present
                                                        Front Door      : No Door present
                                                        Right Door      : No Door present
                                                        Room Dimension  : {dimension_number}
                                                        Back Door       : {parent_rm_number}
       
            '''.format(
                room_number= self.id,
                dimension_number=self.dimension,
                parent_rm_number= self.backroom_number_calculator()
            )
            
        else:   
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

            
        
### function writing area 


def cross_check_input(user_input, list_to_check):
    #this function takes an input and checks with provided list if valid input and return a BOOL
    #print("in cross_check_input function.", list_to_check , type(list_to_check))     #TESTING Print statement
    for each_element in list_to_check:
        if user_input== each_element:
            return True
        
    return False

def input_to_int(input_var):
    try : 
        dimension_number = int(input_var)
    except:
       # print("conversion no good")
        dimension_number = 0    
    return dimension_number


def generate_prize(back_door, current_total_room, max_rooms):
    current_time = datetime.datetime.now()
    current_milisec= current_time.strftime('%f')
    #takes only the (current_milisec)    
    #calculates the max # of rooms
    
   # print(" in generate_prize function, max room calculates to", max_rooms)
    random.seed(current_milisec)
    r_number= random.randint(1,100)
    
    if (back_door == 1):
        return 0
    elif (current_total_room >= max_rooms-1):
        return 1
    elif (r_number >= 90):        
        return 1
    else:
        return 0
        
    return 0

#start the game, intro and first input

print('''You have entered the multiverse maze, you will need to find the hidden treasure deep inside this maze. 
There are 4 doors in a room and each door will lead to a new room except the back door. 
You can go back and forth and try all the path you wish.''')


dimension_input = input("How many layers of Dimensions can you search? Enter a number(1-3). \n")
dimension_number = input_to_int(dimension_input)
input_is_Valid= cross_check_input( dimension_number, [1,2,3])
while(input_is_Valid== False):    
    dimension_input = input("Invalid choice, please select a number between 1 to 3 \n")
    dimension_number = input_to_int(dimension_input)
    input_is_Valid = cross_check_input( dimension_number, [1,2,3])    
    
#calculates total possible rooms
max_rooms=0
for each_dimension in range(0,dimension_number+1):
    max_rooms += 3**each_dimension

input("Press Enter to Open the First Door\n") 

first_maze_door= MazeRoom(1)

print("\nFirst Door opened! Good Luck")

#starting iteration and game logic. passing the first "link"
#using current_room name as pointer to rooms
current_room =first_maze_door
print(current_room)


while current_room.prize == 0 :
        
    dooroptions = { "a":"left", "w":"front" , "d":"right", "s": "back", "g":"Give Up"} 
    
    #print(current_room) #will print at end
    print('''What door will you open?''')
    
    #DOOR INPUT VALIDATION AND CHECK section
    door_choice_input = input("Enter to Choose. {options} \n".format(options=dooroptions))     
    #check input fuction
    input_is_Valid = cross_check_input(door_choice_input, dooroptions.keys())     
    #print("returned", input_is_Invalid) # was testing function return    
    while(input_is_Valid == False) :    
        door_choice_input = input("Incorrect option, please choose between:{options}\n".format(options= list(dooroptions.keys())))
        input_is_Valid = cross_check_input(door_choice_input, dooroptions.keys())
    
    #give up?
    if (door_choice_input =="g"):
        print("You have given up!\n")
        break
    
    #now open the door
    if(door_choice_input=="s"):
        if (current_room.back_door== 1):            
            print("You are currently in the First Room, There is no going back!")                       
        else :            
            current_room = current_room.back_door
            print("Back Door Opened")
            #pointer takes old room
    
    if(door_choice_input=="a"):
        if (current_room.door_status_Isopen(current_room.left_door)==True):            
            print(current_room.door_status_text(current_room.left_door))
            print("Entering Room: {id}".format(id = current_room.left_door.id))
            current_room = current_room.left_door
                        
        else :
            if(current_room.dimension >= dimension_number):
                print("You are currently in the highest Dimension chosen at start, please go back and try another room! \n")
                continue
            else:  
                current_room.left_door= MazeRoom(current_room)
                current_room = current_room.left_door
                print("Left Door Opened")
            #pointer takes new room
            
    if(door_choice_input=="w"):
        if (current_room.door_status_Isopen(current_room.front_door)==True):            
            print(current_room.door_status_text(current_room.front_door))
            print("Entering Room: {id}".format(id = current_room.front_door.id))
            current_room = current_room.front_door
                        
        else :
            if(current_room.dimension >= dimension_number):
                print("You are currently in the highest Dimension chosen at start, please go back and try another room! \n")
                continue
            else:
                current_room.front_door= MazeRoom(current_room)
                current_room = current_room.front_door
                print("Front Door Opened")
                #pointer takes new room
    
    if(door_choice_input=="d"):
        if (current_room.door_status_Isopen(current_room.right_door)==True):            
            print(current_room.door_status_text(current_room.right_door))
            print("Entering Room: {id}".format(id = current_room.right_door.id))
            current_room = current_room.right_door
                        
        else :
            if(current_room.dimension >= dimension_number):
                print("You are currently in the highest Dimension chosen at start, please go back and try another room! \n")
                continue
            else:
                current_room.right_door= MazeRoom(current_room)
                current_room = current_room.right_door
                print("Right Door Opened")
                #pointer takes new room
    
   # print('''\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n''')
    print(current_room)
    #current_room.prize = 0

#check win status
if (current_room.prize == 1):
    print(''' 
$$\     $$\                         $$\      $$\                     
\$$\   $$  |                        $$ | $\  $$ |                    
 \$$\ $$  /$$$$$$\  $$\   $$\       $$ |$$$\ $$ | $$$$$$\  $$$$$$$\  
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |$$  __$$\ $$  __$$\ 
   \$$  / $$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |$$ /  $$ |$$ |  $$ |
    $$ |  $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |$$ |  $$ |$$ |  $$ |
    $$ |  \$$$$$$  |\$$$$$$  |      $$  /   \$$ |\$$$$$$  |$$ |  $$ |
    \__|   \______/  \______/       \__/     \__| \______/ \__|  \__| ''')
    
    #calculating win ratio
    print("You found the Prize in Room: {current} out of {maxnumber} rooms. With a 10% finding chance, your luck chance is:{luck} %"
    .format(
     current= current_room.id,
     maxnumber= max_rooms,
     luck= (((max_rooms-current_room.id)/max_rooms)*100-10)
    
    ))

#finishing touches
print('''\nThank you for playing the maze game. Play again and test your luck anytime!''')