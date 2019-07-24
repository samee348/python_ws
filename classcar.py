class car:
    def __init__(self,regno,no_gears):
        self.regno = regno
        self.no_gears = no_gears
        self.is_started = False
        self.c_gear = 0
    def start(self):
        if self.is_started:
            print(f"Car with regno {self.regno} is already started....")
        else:
            print(f"car with regno {self.regno} started....")
            self.is_started = True
    
    def stop(self):
        if self.is_started:
            print(f"car with regno {self.regno} stopped....")
            self.is_started = False
        else:
            print(f"Car with regno {self.regno} already stopped....")


    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.no_gears:
                self.c_gear+=1
                print(f"car with regno {self.regno} changed gear....{self.c_gear}")
            else:
                print(f"car with regno {self.regno} is already in top gear....")
        else:
            print(f"You cannot change the gear....")
        