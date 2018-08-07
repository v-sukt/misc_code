"""The module has following classes:
- Room"""

class Room(object):
    '''Takes name and description of the object and initializes paths.\nProvides methods \n\t go(direction) and,\n\t add_paths(paths)''' 

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        return self.paths.update(paths)
