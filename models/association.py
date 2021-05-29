class Football_Association:
    __name__ = None
    __id__ = None

    def __init__(self, name, id=None):
        self.__name__ = name
        self.__id__ = id
        
    def get_id(self):
        return self.__id__
    
    def set_id(self, id):
        self.__id__ = id
   
    def set_name(self, new_name):
        self.__name__ = new_name
 
    def get_name(self):
        return self.__name__
