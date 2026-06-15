class Fly:
    def fly(self):
        print("Flying")


class Swim:
    def swim(self):
        print("Swimming")


class Duck(Fly, Swim):
    pass

duck = Duck()
duck.fly()
duck.swim()


class Run:
    def run(self):
        print("Running")


class Athlete(Fly, Run):
    pass

athlete = Athlete()
athlete.fly()
athlete.run()