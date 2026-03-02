class House:
    def __init__(self, surface, year):
        self.surface = surface
        self.year = year

    def start_cleaning(self):
        print("House will be cleaned")

    def stop_cleaning(self):
        print("House is clean") 

class LivingRoom(House):
    def __init__(self, surface, year, table, sofa, floor):
        super().__init__(surface, year) 
        self.table = table
        self.sofa = sofa
        self.floor = floor

    def start_cleaning(self): # eerdere method van de parent wordt hier gespecifieerd en gebruikt als men de subclass tegenkomt
        print("Livingroom will be cleaned")

    def stop_cleaning(self):
        print(f"Livingroom is clean, including {self.table} and {self.sofa} + {self.floor} ---- from subclass livingroom")     

class BathRoom(House):
    def __init__(self, surface, year, bath, shower, floor, walls):
        super().__init__(surface, year)
        self.bath = bath
        self.shower = shower
        self.floor = floor
        self.walls = walls   

    def start_cleaning(self):
        print("Bathroom will be cleaned")

    def stop_cleaning(self):
        print(f"Bathroom is clean, including {self.walls}, {self.bath} and {self.shower} ---- from subclass bathroom")                  

rooms = [
    LivingRoom("35m2", 2019, "table in wood", "sofa in white textile", "floor in wood"),
    BathRoom("12m2", 2019, "white bath", "no shower", "floor in white tiles", "walls in white tiles")
]

for room in rooms:
    print('-' * 15)
    print(f"Inspecting {room.surface} and floor to be cleaned: {room.floor} ({type(room).__name__})") # kun hier kenmerken van de subclasses weergeven die verschillen?
    if isinstance(room, BathRoom):
        print(f"For the bathroom iinspect also: the {room.shower}, the {room.bath} and the {room.walls}")
    elif isinstance(room, LivingRoom):
        print(f"For the livingroom inspect also the {room.table} and the {room.sofa}")
    print('-' * 15)
    room.start_cleaning()
    print('-' * 8)
    room.stop_cleaning()
    print('-' * 8)
    
#    if isinstance(room, House):
#       print(f"Inspecting {room.surface}")
#       room.start_cleaning()
#       room.stop_cleaning()
#   else:
#       raise Exception("Room in nog mentioned in the list")