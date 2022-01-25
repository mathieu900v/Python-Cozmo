import random
import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import radians, degrees, distance_mm, speed_mmps

tapote = False
find = False
who_is_tapped = -1
born_inf = 0
born_sup = 100
choice = random.randint(born_inf,born_sup)


def on_cube_tapped(event, *, obj, tap_count, tap_duration, **kw):
   global tapote
   global who_is_tapped


   tapote = True
   who_is_tapped = obj.object_id


def cozmo_program(robot: cozmo.robot.Robot):
    global tapote
    global choice
    global find
    global born_inf
    global born_sup

    find = False
    cube1 = robot.world.get_light_cube(LightCube1Id)  # il ressemble à un trombonne
    cube2 = robot.world.get_light_cube(LightCube2Id)  # il ressemble à une lampe ou un coeur
    cube3 = robot.world.get_light_cube(LightCube3Id)  # il ressemble aux lettres ab sur un T

    # cube2 : bleu
    # cube1 : vert
    # cube0 : rouge

    cube1.set_lights(cozmo.lights.red_light) # red
    cube2.set_lights(cozmo.lights.green_light)
    cube3.set_lights(cozmo.lights.blue_light)

    robot.add_event_handler(cozmo.objects.EvtObjectTapped, on_cube_tapped)
    # robot.say_text("Fait moi deviner un nombre").wait_for_completed()
    # robot.say_text("Le cube rouge le nombre est plus petit").wait_for_completed()
    # robot.say_text("Le cube bleu le nombre est plus grand").wait_for_completed()
    # robot.say_text("Le cube vert j'ai gagné").wait_for_completed()
    while not find:
        robot.say_text(str(choice)).wait_for_completed()
        
        while(not tapote):
            pass
        print("Cube tapped")   
        tapote = not tapote
        
        #object_id 0 = plus petit
        #object_id 1 = good
        #oject_id 2 = plus grand
        if who_is_tapped == 1:
            find = True
        elif who_is_tapped == 2:
            born_inf = choice
            choice = random.randint(born_inf,born_sup)
        elif who_is_tapped == 0:
            born_sup = choice
            choice = random.randint(born_inf,born_sup)
        if born_sup == born_inf:
            born_inf = 0
            born_sup = 100
    
    robot.say_text("J'ai trouvé" + str(choice)).wait_for_completed()


        
        
cozmo.run_program(cozmo_program)