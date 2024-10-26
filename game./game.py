# asking names the player wants to use for themselves and characters and intoduce story, keep track of players alive state - ben 
user = input("Enter Your name: ")
print("Hello,", user, "Welcome to The Path! You will have to make the correct choices to beat the game.(If you mispell anything it will crash)")
joe = input("Enter the name for your friend: ")
jim = input("One more name: ")
isJoeAlive = True
isJimAlive = True
isGameOver = False
isJoeWith = True
youAlive = True
print("You,",joe,"and",jim, "are going camping, you are on your way to the cabin. It starts to storm, you hide in a cave but get lost! The storm has passed now. Try and get out.")
#asking what the options/directions you want to go (forest, mountain, river, graveyard, car) and the outcome-adele 
direction = input("You are deep in the forest now, which way do you go? (left or right)")
if direction == "right":
 print("You walk right. Turns out you are at a bottom of a cliff. Theres a rock wall, Do you want to try and climb it?")
else:
 print("You find a river, should you try and get some fish for food? ")

fall = input("yes or no: ")
if fall == "yes":
 print("OH NO!!", jim, "fell! You must keep going.")
 isJimAlive = False
else:
 print("You keep walking by")

print("You are very hungry. What should you eat?")
food = input("bugs or berries: ")
if food == "bugs": 
 print("It didnt taste good but, you arent hungry anymore.")
else:
 print("Yum! You are all full now, you found so many that you have extras that you store in your bag.")

print("You keep walking until night. You must sleep now. Where do you want to sleep?")
sleep = input("cave or tree: ")
if sleep == "cave":
 print("You slept very well")
else:
 print("You slept well")
 if food == "berries":
  print("but something ate your berries :(")

print("Its time to walk again. Do you want to build a raft to go down the stream, or walk up a mountian?")
trip = input("raft or walk: ")
if trip == "raft": 
 if isJimAlive == False:
  print("OH NO!", joe, "fell, You must keep going")
  isJoeAlive = False
  isJoeWith = False
 else:
  print("OH NO!", jim, "fell. You must keep going.")
  isJimAlive = False
else: 
 if isJimAlive == True:
  print("OH NO!", jim, "fell. You must keep going")
  isJimAlive = False
 print("You got to the top, and found a small town. You win!!! Good job", user)
 isGameOver = True

if isGameOver == False:
  berries = 0
  if food == "berries" and sleep == "cave":
    berries = 10
  print("You get off the raft. You find a berry bush. You gained 10 berries")
  berries = berries + 10
  print("you now have", berries)

#keep collecting berrys in the forest until you have over 25(while loop) -amanda
  while berries < 25:
    print("You should find more before night. Do you want to look for more to the left or the right?")
    lookForBerries = input("left or right: ")
    if lookForBerries == "left":
      print("You found 10 berries")
      berries = berries + 10
    else: 
      print("You found 5 berries")
      berries = berries + 5
  
  if isJoeAlive == True:
    print("You and",joe,"Get sick. Do you each eat half the berries or do you eat all of them?")
    share = input("eat half or all: ")
    if share == "all":
      isJoeAlive = False
      isJoeWith = False
      print("OH NO!", joe, "stays sick, and dies. You got better and found your way out. You win!!! ( but live with lefelong guilt of not saving",joe,")")
      isGameOver = True
    elif berries < 30: 
      print("You both stayed sick, and died. You lose")
      youAlive = False
      isJoeAlive = False 
      isJoeWith = False
      isGameOver = True
    else: 
      print("You and", joe, "both get better and escape. YOU WIN!")
  else:
    print("Congrats you survied! (a part of you dies here with", joe, "and", jim,")")
    

#if player says to continue playing, then go into the car to go to the seance to bring back friends at the graveyard-adele
  print("YAY! You get home safe")
  if isJoeAlive == False:
    print("You miss your friends...Should you bring them back")
  else:
    print("You and", joe, "miss", jim, "Should you bring them back?")
    
  sanoce = input("yes or no: ")
  if sanoce == "no":
    print("You live the rest of your life trumazized from the forest")
    isGameOver = True
  else:
    print("You have to do a sanoces. You get in your car to go to the graveyard.")

  joeComin = "no"

  if isGameOver == False:
    print("Your driving down a long street, it dark and the streets are empty.")
    if isJoeAlive == True: 
      print("Should you bring",joe,)
      joeComin = input("yes or no: ")
      if joeComin == "yes":
        print("You pick him up and keep driving.")
        isJoeWith = True
      else: 
        isJoeWith = False

    print("You drive to the graveyard to begin the Sanonce. As you drive you see something in you review mirror")

    if isJoeAlive == False:
      print("Its", joe, "and", jim)
    else:
      print("Its",jim)
    print("You get to the graveyard. Time to begin...you light the candeles and start to chant, something starts digging from the grave beneth you.")
  
    if isJoeAlive ==  True and joeComin == "no" and isJimAlive == False:
      print(jim, "rises from the ground. followd by them is a demon. The demon attacks you and", jim, "now jim isnt the olny ghost.", jim, "has to live with out either of you now. good job >:/")
      isGameOver = True
      youAlive = False
    elif isJoeAlive == True and joeComin == "yes" and isJimAlive == False:
      print(jim, "rises from the ground. followd by them, is a demon. The demon attacks.", joe, "fights back and kicks the demon back into the grave.",jim,"lives. GOOD JOB! You ALL get to live now. :D" )
      isGameOver = True
      youAlive = True
    else:
      print(jim, "and", joe, "rise from the ground. followd by them, is a demon. The demon attacks.", joe, "fights back and kicks the demon back into the grave. GOOD JOB! You ALL get to live now. :D")
      isGameOver = True 




