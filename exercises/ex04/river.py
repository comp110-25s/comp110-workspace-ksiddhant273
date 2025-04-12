"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bear: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
            # Filter out fish older than 3
            surviving_fish = [fish for fish in self.fish if fish.age <= 3]
            self.fish = surviving_fish
            
            surviving_bears = [bear for bear in self.bears if bear.age <= 5]
            self.bears = surviving_bears
    
    def remove_fish(self, amount: int):
        i = 0
        for fish in self.fish:
            if i < amount:
                self.fish.pop()
                i += 1
            else:
                return None
    
    def bears_eating(self):
        for bear in self.bears:
                if len(self.fish) >= 3:
                    bear.eat(3)
                    self.remove_fish(3)

    def check_hunger(self):
        surviving_bear = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bear = surviving_bear

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        self.bears_eating()
        
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        
        self.repopulate_fish()
        if len(self.fish) > 1:
           num_pairs = len(self.fish) // 2
           new_fish = [Fish() for fish in range(num_pairs * 4)]
           self.fish.extend(new_fish)
       
        self.repopulate_bears()
        if len(self.bears) > 1:
            num_pairs = len(self.bear) // 2
            new_bear = [Bear() for bear in range(num_pairs)]
            self.bear.extend(new_bear)
        self.view_river()

    def one_river_week(self):
    for i in range(7):
        self.one_river_day()
