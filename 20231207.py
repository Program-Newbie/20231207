class Sports:
    
    def __init__(self,name):
        self.name = name

    @property
    def sport_name(self):
        return self.name
    @sport_name.setter
    def sport_set(self,name):
        self.name = name

class On_Land(Sports) :
    def __init__(self,name,field):
        super().__init__(name)
        self.field = field

    @property
    def field_name(self):
        return self.field

class In_Water(Sports) :
    def __init__(self,name,field):
        super().__init__(name)
        self.field = field

    @property
    def field_name(self):
        return self.field

if __name__ == "__main__" :
    Ball = On_Land("baseball","Field")
    Boat = In_Water("Boat","Pacific")

    print(Ball.sport_name)
    print(Ball.field_name)
    print(Boat.sport_name)
    print(Boat.field_name)

    Ball.name = "ground"

    print(Ball.sport_name)
    print(Ball.field_name)
    print(Boat.sport_name)
    print(Boat.field_name)
    