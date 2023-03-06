class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, specie, name):
        if specie == "mammal":
            self.mammals.append(name)
        elif specie == "fish":
            self.fishes.append(name)
        elif specie == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, specie):
        result = ""
        if specie == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"

        elif specie == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"

        elif specie == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


set_zoo_name = input()
zoo = Zoo(set_zoo_name)
count = int(input())

for i in range(count):
    command = input().split()
    species = command[0]
    animal = command[1]
    zoo.add_animal(species, animal)

index = input()
print(zoo.get_info(index))
