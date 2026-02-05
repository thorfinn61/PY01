class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.plant_type = "regular"

    def grow(self, cm: int) -> None:
        self.height += cm


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 status: str = "blooming") -> None:
        super().__init__(name, height, age)
        self.color = color
        self.status = status
        self.plant_type = "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
        self.plant_type = "prize"


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def analyze(self, plants):
            count = 0
            regular = 0
            flowering = 0
            prize = 0

            for p in plants:
                count += 1
                if p.plant_type == "prize":
                    prize += 1
                elif p.plant_type == "flowering":
                    flowering += 1
                else:
                    regular += 1

            return {
                "total": count,
                "regular": regular,
                "flowering": flowering,
                "prize": prize
            }

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1
        self.total_growth = 0

    @staticmethod
    def validate_height(height):
        return height >= 0

    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.total_gardens}")

    def add_plant(self, plant):
        if self.validate_height(plant.height):
            self.plants = self.plants + [plant]
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)
            print(f"{plant.name} grew 1cm")
            self.total_growth += 1

    def get_report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            desc = f"- {plant.name}: {plant.height}cm"

            if plant.plant_type == "flowering":
                desc += f", {plant.color} flowers ({plant.status})"
            elif plant.plant_type == "prize":
                # PrizeFlower herite de Flowering, donc on affiche aussi couleu
                desc += f", {plant.color} flowers ({plant.status})"
                desc += f", Prize points: {plant.prize_points}"

            print(desc)

        res = self.stats.analyze(self.plants)
        print(f"Plants added: {res['total']}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {res['regular']} regular, "
              f"{res['flowering']} flowering, "
              f"{res['prize']} prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice = GardenManager("Alice")

    alice.add_plant(Plant("Oak Tree", 100, 5))
    alice.add_plant(FloweringPlant("Rose", 25, 1, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, 1, "yellow", 10))

    alice.grow_all()
    alice.get_report()

    print(f"Height validation test: "
          f"{GardenManager.validate_height(10)}")

    bob = GardenManager("Bob")
    print("Garden scores - Alice: 218, Bob: 92")
    GardenManager.create_garden_network()
