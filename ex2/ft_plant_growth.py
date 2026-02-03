class Plant:
    def __init__(self, name, height, plant_age):
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth = 0

    def grow(self):
        self.height += 1
        self.growth += 1

    def age(self):
        self.plant_age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


if __name__ == "__main__":
    day = 1
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    while day < 7:
        rose.grow()
        rose.age()
        day += 1
    if day == 7:
        print("=== Day 7 ===")
        rose.get_info()
        print(f"Growth this week: +{rose.growth}cm")
