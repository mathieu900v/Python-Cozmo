import sqlite3
import random
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

who_is_tapped = -1
tapote = False

def on_cube_tapped(event, *, obj, tap_count, tap_duration, **kw): 
   global tapote
   global who_is_tapped


   tapote = True
   #print("patape " + str(obj.object_id))
   who_is_tapped = obj.object_id-1

def myfunction():
  return 0.1

def quizz (robot: cozmo.robot.Robot):
    # Connectez- vous à la base de données.
    connection = sqlite3.connect('./game_bdd/quizz.db')
    cubes = [robot.world.get_light_cube(LightCube1Id), robot.world.get_light_cube(LightCube2Id), robot.world.get_light_cube(LightCube3Id)]
    global tapote
    find=False

    #age = int(input("Entre ton age !"))
    age = 10
    try:
        cur = connection.cursor()
        cur.execute("SELECT * FROM Questions where niveau <=" + str(age))

        
        cubes[0].set_lights(cozmo.lights.red_light) 
        cubes[1].set_lights(cozmo.lights.green_light) 
        cubes[2].set_lights(cozmo.lights.blue_light) 
        robot.add_event_handler(cozmo.objects.EvtObjectTapped,on_cube_tapped)
        rows = cur.fetchall()
        random_question_row = random.randint(0,len(rows)-1)

        question = rows[random_question_row][2] # la question

        reponse_entier = rows[random_question_row][3] # toutes les réponses
        reponse_tab = reponse_entier.split(';')
        
      
        reponse_final = reponse_tab[0] # la bonne réponse
        print(reponse_tab)
        random.shuffle(reponse_tab)
        print(reponse_tab)

        #shuffle(list)

        #print(question)
        robot.say_text(str(question)).wait_for_completed()
        robot.say_text("Cube rouge : " + str(reponse_tab[0])).wait_for_completed()
        robot.say_text("Cube vert : " + str(reponse_tab[1])).wait_for_completed()
        robot.say_text("Cube bleu : " + str(reponse_tab[2])).wait_for_completed()
        
        while(not find):
            while(not tapote):
                pass
            print("Cube tapped")
            tapote = not tapote 
            print("tape " + str(who_is_tapped))
            if(reponse_tab[who_is_tapped] == reponse_final):
                robot.say_text("Bravo tu as trouvé !").wait_for_completed()
                find=True
            else:
                robot.say_text("Faux. Essaie encore").wait_for_completed()


        robot.say_text(str(reponse_final)).wait_for_completed()

            #for row in rows:
            #   print(row)

    finally:
        # Closez la connexion (Close connection).
        connection.close()

cozmo.run_program(quizz)