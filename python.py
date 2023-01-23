import math
import time

global text_delay
text_delay = 0.5

stats_array = ["Strength","Speed","Endurance","Agility","Intellengence","Luck"]
selected_character_stats = ["0","0","0","0","0","0"]
elf_stats = ["4","8","5","6","4","3"]
wizard_stats = ["3","3","5","5","10","4"]
archer_stats = ["5","3","8","6","5","3"]
berserker_stats = ["9","6","3","5","4","3"]

print ""

print "Character list: Elf  Wizard  Archer  Berserker"

character = raw_input("Select character: ")

if(character == "Elf" or character == "elf"):
      selected_character_stats[0] = elf_stats[0]
      selected_character_stats[1] = elf_stats[1]
      selected_character_stats[2] = elf_stats[2]
      selected_character_stats[3] = elf_stats[3]
      selected_character_stats[4] = elf_stats[4]
      selected_character_stats[5] = elf_stats[5]

if(character == "Wizard" or character == "wizard"):
      selected_character_stats[0] = wizard_stats[0]
      selected_character_stats[1] = wizard_stats[1]
      selected_character_stats[2] = wizard_stats[2]
      selected_character_stats[3] = wizard_stats[3]
      selected_character_stats[4] = wizard_stats[4]
      selected_character_stats[5] = wizard_stats[5]

if(character == "Archer" or character == "archer"):
      selected_character_stats[0] = archer_stats[0]
      selected_character_stats[1] = archer_stats[1]
      selected_character_stats[2] = archer_stats[2]
      selected_character_stats[3] = archer_stats[3]
      selected_character_stats[4] = archer_stats[4]
      selected_character_stats[5] = archer_stats[5]

if(character == "Berserker" or character == "berserker"):
      selected_character_stats[0] = berserker_stats[0]
      selected_character_stats[1] = berserker_stats[1]
      selected_character_stats[2] = berserker_stats[2]
      selected_character_stats[3] = berserker_stats[3]
      selected_character_stats[4] = berserker_stats[4]
      selected_character_stats[5] = berserker_stats[5]

print ""
print "Strength:",selected_character_stats[0]
print "Speed:",selected_character_stats[1]
print "Endurance:",selected_character_stats[2]
print "Agility:",selected_character_stats[3]
print "Intellengence:",selected_character_stats[4]
print "Luck:",selected_character_stats[5]

int_stats = [0,0,0,0,0,0]

int_stats[0] = int(selected_character_stats[0])
int_stats[1] = int(selected_character_stats[1])
int_stats[2] = int(selected_character_stats[2])
int_stats[3] = int(selected_character_stats[3])
int_stats[4] = int(selected_character_stats[4])
int_stats[5] = int(selected_character_stats[5])

damage = int(int_stats[0]*1.25)+(int_stats[3]/2)+(int_stats[4]*0.75)
print "Damage",damage

max_hits = int(int_stats[2]+1)
print "Max Hits:",max_hits

attack_speed = int(((int_stats[1]/2)+(int_stats[3]/2)))
print "Attack Speed:",attack_speed

print ""

def intro():
      print "------------------------"
      print "Welcome to the Castle"
      print "  Be prepared to fight  "
      print "       Do not die       "
      print "------------------------"


#Building the rooms
def build_rooms(north_room,east_room,south_room,west_room,current_room):

      print ""
      print "You have entered the",current_room
      print ""
      #Great Hall Room
      if(current_room == 'Great Hall'):
         north_room = 'Bedroom'
         east_room = 'Dungeon'
         south_room = 'Library'
         west_room = 'Cellar'
         
      #Dungeon Room
      if(current_room == 'Dungeon'):
         north_room = 'none'
         east_room = 'none'
         south_room = 'Gallery'
         west_room = 'Great Hall'
         
      #Library Room
      if(current_room == 'Library'):
         north_room = 'Great Hall'
         east_room = 'Gallery'
         south_room = 'none'
         west_room = 'Dining Hall'
         
      #Celler Room
      if(current_room == 'Cellar'):
         north_room = 'none'
         east_room = 'Great Hall'
         south_room = 'Dining Hall'
         west_room = 'none'
         
      #Gallery Room
      if(current_room == 'Gallery'):
         north_room = 'Dungeon'
         east_room = 'none'
         south_room = 'none'
         west_room = 'Library'

      #Dining Hall Room
      if(current_room == 'Dining Hall'):
         north_room = 'Cellar'
         east_room = 'Library'
         south_room = 'none'
         west_room = 'none'

      #Bedroom Room
      if(current_room == 'Bedroom'):
         north_room = 'none'
         east_room = 'none'
         south_room = 'Great Hall'
         west_room = 'none'

      direction_question = raw_input("What direction do you want to go?(North,East,South,West) ")
      
      if(direction_question == 'North' or direction_question == 'north'):
            if(north_room == 'none'):
                  current_room = current_room
                  print "No room in that direction"
                  build_rooms('','','','',current_room)
            else:
                  build_rooms('','','','',north_room)
                  
      elif(direction_question == 'East' or direction_question == 'east'):
            if(east_room == 'none'):
                  current_room = current_room
                  print "No room in that direction"
                  build_rooms('','','','',current_room)
            else:
                  build_rooms('','','','',east_room)
                  
      elif(direction_question == 'South' or direction_question == 'south'):
            if(south_room == 'none'):
                  current_room = current_room
                  print "No room in that direction"
                  build_rooms('','','','',current_room)
            else:
                  build_rooms('','','','',south_room)
                  
      elif(direction_question == 'West' or direction_question == 'west'):
            if(west_room == 'none'):
                  current_room = current_room
                  print "No room in that direction"
                  build_rooms('','','','',current_room)
            else:
                  build_rooms('','','','',west_room)
                  
      else:
            current_room = current_room
            print "No room in that direction"
            build_rooms('','','','',current_room)

intro()
build_rooms('','','','','Great Hall')
         
         
      
