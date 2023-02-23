class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, specie, name):
        if specie == "mammals":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, specie):
        if specie == "mammals":
            return f"Mammals in {self.name}: {self.mammals}\
                    Total animals: {Zoo.__animals}"

        elif species == "fish":
            return f"Fish in {self.name}: {self.fish}\
                                Total animals: {Zoo.__animals}"
        elif species == "birds":
            return f"Birds in {self.name}: {self.birds}\
                                Total animals: {Zoo.__animals}"


set_zoo_name = input()
count = int(input())

zoo = Zoo(set_zoo_name)
species = "mammal"
animal = "lion"
zoo.add_animal(species, animal)

print(f"{zoo.get_info(species)}")
