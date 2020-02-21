class Mark():
    def favoriteSoccerTeam(self):
        print("Mark's favorite soccer team is Barcelona")

    def favoriteFootballTeam(self):
        print("Mark's favorite team is the packers")


class Alex():
    def favoriteSoccerTeam(self):
        print("Alex's favorite soccer team is PSG")

    def favoriteFootballTeam(self):
        print("Mark's favorite team is the rams")


obj_mark = Mark()
obj_alex = Alex()
for name in (obj_mark, obj_alex):
    name.favoriteSoccerTeam()
    name.favoriteFootballTeam()

'This is an example of polymorphism'
