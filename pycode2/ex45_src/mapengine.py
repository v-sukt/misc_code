"""The module has following classes:
Map: provides the game with the objects of the game Map
Engine: Executes the Scenes of the game till GameOver or till Finish/
"""
import scenes_location as scn

class Map(object):
    """ The Map class which has-a scenes dictionary with which initiates various scenes from the scene module
    Map has methods:
     - entry_scene : returns the object of the entry scene's class
     - next_scene : return the object of parameter's class"""

    scenes = {
      'walk_in_forest' : scn.WalkInForbiddenForest(),
      'talk_gwarp' : scn.TalkGwarp(),
      'dolores_office' : scn.DoloresOffice(),
      'hogwards_dormitory' : scn.HogartsDormitory(),
      'horsemen' : scn.HorseMen(),
      'lost_path' : scn.LostPath(),
      'finish' : scn.Finish(),
      'gameover' : scn.GameOver()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene):
        return Map.scenes.get(scene)

    def entry_scene(self):
        return self.next_scene(self.start_scene)


class Engine(object):

    def __init__(self, map_name):
        self.map_name = map_name

    def play(self):
        print "entered play"
        current_scene = self.map_name.entry_scene()
        
        while True:
            print "\n", "==o=="*5
            next_scene_name = current_scene.enter_scene()
            current_scene = self.map_name.next_scene(next_scene_name)