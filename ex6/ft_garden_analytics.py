class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int) -> None:
        self.height += cm


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 status: str = "blooming") -> None:
        super().__init__(name, height, age)
        self.color = color
        self.status = status


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

class GardenManager():
	