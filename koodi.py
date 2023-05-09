#*****************************************************  

# Ratkaisu koodit Minecraft Education lessonille
#       "PYTHON 101 WITH MAKECODE - LESSON 4"

# @author tekija: (ensimmäisen version tekija, VL)

# @since pvm: 9.5.2023

# @version versio: 1.0 

# muutos: (nimikirjaimet omat nimikirjaimet)  

#*****************************************************/ 

# Tehtävä nr.1
    # Tässä pitää saada kaikki eläimet listassa oikeaan paikkaan

location1 = world(-2, 40, -11)
location2 = world(-2, 40, -5)
location3 = world(-8, 40, -0)
location4 = world(-13, 40, -5)
location5 = world(-13, 40, -11)

# list of animals 
My_list = [COW, PIG, SHEEP, HORSE, RABBIT]

# spawn the first mob from the list at location1
mobs.spawn(My_list[0], location1)

# spawn the second mob from the list at location4
mobs.spawn(My_list[1], location4)

# spawn the third mob from the list at location2
mobs.spawn(My_list[2], location2)

# spawn the fourth mob from the list at location5
mobs.spawn(My_list[3], location5)

# spawn the fifth mob from the list at location3
mobs.spawn(My_list[4], location3)

#______________________________________________#

# Tehtävä nr.2
    # Tässä pitää antaa koirille ruokaa dietin mukaan

# Koira nr.1
Bone = world(-21, 45, -31)
Beef = world(-21, 45, -29)
Chicken = world(-21, 45, -27)
Biscuit = world(-21, 45, -25)
Vitamins = world(-21, 45, -23)

Dog_Food = [Bone, Beef, Chicken, Biscuit, Vitamins]

blocks.place(REDSTONE_BLOCK, Dog_Food[0])
blocks.place(REDSTONE_BLOCK, Dog_Food[1])
blocks.place(REDSTONE_BLOCK, Dog_Food[2])
blocks.place(REDSTONE_BLOCK, Dog_Food[3])

# Koira nr.2
Bone = world(-21, 45, -31)
Beef = world(-21, 45, -29)
Chicken = world(-21, 45, -27)
Biscuit = world(-21, 45, -25)
Vitamins = world(-21, 45, -23)

Dog_Food = [Bone, Beef, Chicken, Biscuit, Vitamins]

blocks.place(REDSTONE_BLOCK, Dog_Food[0])
blocks.place(REDSTONE_BLOCK, Dog_Food[1])
blocks.place(REDSTONE_BLOCK, Dog_Food[2])
blocks.place(REDSTONE_BLOCK, Dog_Food[3])
blocks.place(REDSTONE_BLOCK, Dog_Food[4])

# Koira nr.3
Bone = world(-21, 45, -31)
Beef = world(-21, 45, -29)
Chicken = world(-21, 45, -27)
Biscuit = world(-21, 45, -25)
Vitamins = world(-21, 45, -23)

Dog_Food = [Bone, Beef, Chicken, Biscuit, Vitamins]

blocks.place(REDSTONE_BLOCK, Dog_Food[0])
blocks.place(REDSTONE_BLOCK, Dog_Food[2])
blocks.place(REDSTONE_BLOCK, Dog_Food[3])
blocks.place(REDSTONE_BLOCK, Dog_Food[4])

#______________________________________________#

# Tehtävä nr.3
    # Tässä pitää valita oikea kissa listasta

# Osa 1
Cat_Names = ["Smokey", "Oreo", "Sammy", "Patch", "Princess", "Shadow"]

player.say(Cat_Names[4])

# Osa 2
Cat_Names = ["Smokey", "Oreo", "Sammy", "Patch", "Princess", "Shadow"]

# Sort the names alphabetically in the list
Cat_Names.sort()

player.say(Cat_Names[3])

# Osa 3
Cat_Names = ["Smokey", "Oreo", "Sammy", "Patch", "Princess", "Shadow"]

# Sort the names alphabetically in the list
Cat_Names.sort()

# Reverse the list
Cat_Names.reverse()

player.say(Cat_Names[3])

#______________________________________________#