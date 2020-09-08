from random import randint
from time import sleep
from sys import exit
from utils import Speech2Intent
from constants import *

speech2intent = Speech2Intent(wit_access_token)

print("You are a pokemon trainer with your charmander on an island.")
sleep(1)
print("However, you are trapped on this island.")
sleep(1)
print("If you complete the quest, your Charmander will have enough experince to become")
sleep(1)
print("a Charizard. Then, you will find a master ball and be able to catch Mewtwo,")
sleep(1)
print("who is nearly unseen.")
sleep(1)
print("First, you must battle 20 different pokemon.")
battlesDone = 0

while battlesDone < 20:
    choosePokemon = randint(1,15)

    if choosePokemon == 1:
        spawn = ' Pidgey'
        shp = 14
        satk = 9
        sdef = 10
   
    if choosePokemon == 2:
        spawn = ' Rattata'
        shp = 16
        satk = 8
        sdef = 10
  
    if choosePokemon == 3:
        spawn = ' Zubat'
        shp = 15
        satk = 7
        sdef = 8
  
    if choosePokemon == 4:
        spawn = ' Caterpie'
        shp = 14
        satk = 9
        sdef = 5
    
    if choosePokemon == 5:
        spwan = ' Spearow'
        shp = 14
        satk = 9
        sdef = 7
    
    if choosePokemon == 6:
        spawn = ' Weedle'
        shp = 15
        satk = 9
        sdef = 8
  
    if choosePokemon == 7:
        spawn = ' Paras'
        shp = 14
        satk = 8
        sdef = 7
  
    if choosePokemon == 8:
        spawn = ' Magikarp'
        shp = 13
        satk = 10
        sdef = 9
  
    if choosePokemon == 9:
        spawn = ' Eevee'
        shp = 15
        satk = 9
        sdef = 10
  
    if choosePokemon == 10:
        spawn = ' Krabby'
        shp = 16
        satk = 9
        sdef = 10

    if choosePokemon == 11:
        spawn = ' Jigglypuff'
        shp = 15
        satk = 9
        sdef = 10
  
    if choosePokemon == 12:
        spawn = ' Clefairy'
        shp = 15
        satk = 8
        sdef = 9

    if choosePokemon == 13:
        spawn = ' Pidgeotto'
        shp = 17
        satk = 8
        sdef = 11
  
    if choosePokemon == 14:
        spawn = ' NidoranF'
        shp = 16
        satk = 8
        sdef = 9

    if choosePokemon == 15:
        spawn = ' NidoranM'
        shp = 15
        satk = 8
        sdef = 10



    while Php >0 and shp >0:
        choice = ('invalid')
        while choice != ('fight'):
            print(('What will you do against the'+ spawn+ '?'))
            for choice in choices:
                print(choice)
            sleep(1)
            ####
            choice = speech2intent.recognize_speech('game_choice.wav')
            ####
            if choice == ('fight'):
                print (choices[0])
                print ('Alright charmander! Lets do this!')
            if choice == ('run'):
                print (choices[1])
                print(('You attempt to flee, but the '+ spawn+ ' hits charmander anyway, knocking him out in one blow.'))
                print ('You are out of revives.  Please insert $.50 to play again.')
                Php =0
                exit(0)
            if choice == ('analyze'):
                print (choices[2])
                print ('Charmanders stats:')
                print(('Attack = ' +str(Patk)+ '   Defense = ' +str(Pdef)+ '   Health = ' +str(Php)+ '     Gold = ' +str(Pgold) ))
                print(('The wild' + spawn+' has stats of:'))
                print(('Attack = ' +str(satk)+ '   Defense = ' +str(sdef)+ '   Health = ' +str(shp) ))
            if choice == ('heal'):
                print (choices[3])
                print ("You can choose to either pay 500 gold and get a guarranteed heal, or take your chances with berries. Note- berries CAN kill you. (Pick 'pay' or 'berries')")
                sleep(.5)
                print ("And don't abuse the healing system, you can't get higher than 30 Hp.")
                if Php > 30:
                  print("No HP for you.")
                print("Will you take your chances with berries, or pay 500 gold?")
                ####
                heal = speech2intent.recognize_speech('heal_choice.wav')
                ####
                if heal == ("heal_berries"):
                  healing = randint(1,20)
                  if healing < 11:
                    print("You got real lucky, kid. + 5 hp")
                    Php = Php + 5
                  if healing > 11:
                    print("You lost 5 HP...")
                    Php = Php - 5
                  
                if heal == ("heal_pay"):
                  if Pgold < 500:
                    print ("You don't have the money to pay for it.")
                  if Pgold > 500:
                    Pgold == Pgold - 500
                    print('+5 HP. You have '+(int(Pgold))+' remaining.')
                    Php == Php + 5
                  if Pgold > 500 and Php > 30:
                    print ("You reached the maximum health.")
                    
                    
                    
                  
            if choice ==('fight'):
                Pattroll = randint(1,20)
                if Pattroll >= sdef:
                    damage = randint(2,8)
                    print('Charmander, use ember! ' + spawn+ ' took ' +str(damage)+ ' damage!')
                    shp =  shp - damage
                if Pattroll < sdef:
                    print ('The flame missed!')

                if shp >0:
                    Sattroll = randint(1,20)
                    if Sattroll >= Pdef:
                        damage = randint (2,7)
                        print('The ' +spawn+ ' hits charmander for ' +str(damage)+ '!')
                        Php = Php - damage
                    if Sattroll < Pdef:
                        print ('Charmander dodged the attack!')
            if Php <=0:
                print('Charmander fainted, and the '+ spawn+ ' has knocked him out.')
                battlesDone = 0
            if shp <=0:
                reward = randint(200,900)
                print('You win! For your troubles, you find ' +str(reward)+ ' PP.')
                Pgold = Pgold + reward
                Php = 25
                print ('You find an Oran berry tree and are able to heal.')
                battlesDone += 1
                print('You are on battle number' + str(battlesDone)+', so keep having fun there.')
                break
            
            
            
            
    if battlesDone == 20:
        print("Woah! Charmander is evolving!")
        sleep(3)
        print(" Charmander evolved into charizard! Awesome!")
        print("You find a master ball and catch the legendary pokemon, mewtwo.")
        print(" You fly off the island with charizard, and are greeted home as a hero.")
        print(" The end!")
        print("Thanks for playing!")