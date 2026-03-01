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
        print("Living room will be cleaned")

    def stop_cleaning(self):
        print(f"Living room is clean, , including {self.table} and {self.sofa} + {self.floor}")     

class BathRoom(House):
    def __init__(self, surface, year, bath, shower, floor, walls):
        super().__init__(surface, year)
        self.bath = bath
        self.shower = shower
        self.floor = floor
        self.walls = walls   

    def start_cleaning(self):
        print("Bath room will be cleaned")

    def stop_cleaning(self):
        print(f"Bath room is clean, including {self.walls}, {self.bath} and {self.shower}")                  

rooms = [
    LivingRoom("35m2", 2019, "table in wood", "sofa in white textile", "floor in wood"),
    BathRoom("12m2", 2019, "white bath", "no shower", "floor in white tiles", "walls in white tiles")
]

for room in rooms:
    print(f"Inspecting {room.surface} and floor to be cleaned: {room.floor} ({type(room).__name__})")
    room.start_cleaning()
    room.stop_cleaning()
    
#    if isinstance(room, House):
#       print(f"Inspecting {room.surface}")
#       room.start_cleaning()
#       room.stop_cleaning()
#   else:
#       raise Exception("Room in nog mentioned in the list")