class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    total = 0
    plant_data = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    print("=== Plant Factory Output ===")
    for data in plant_data:
        new_plant = Plant(data[0], data[1], data[2])
        print(f"Created: {new_plant.name} "
              f"({new_plant.height} cm, {new_plant.age} days)")
        total += 1
    print()
    print(f"Total plants created: {total}")
