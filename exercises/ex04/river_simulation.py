from exercises.ex04.river import River

my_river = River(10, 2)


def view_river(self):
    print(f"~~~ Day {self.day}: ~~~")
    print(f"Fish population: {len(self.fish)}")
    print(f"Bear population: {len(self.bear)}")
