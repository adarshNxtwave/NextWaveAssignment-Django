

class Animal:
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
    
    def grow(self):
        self.age_in_months = self.age_in_months + self.growwAge
        self.required_food_in_kgs = self.required_food_in_kgs + self.growwFood
    
    def make_sound(self):
        print(self.soundKeyword)
    
    def breathe(self):
        print(self.breatheKeyword)
    
    @staticmethod
    def validator(age_in_months,breed,required_food_in_kgs):
        if age_in_months != 1: # or self.required_food_in_kgs <= 0:
            return False
        return True

class Deer(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if not Animal.validator(age_in_months,breed,required_food_in_kgs):
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")

        super().__init__(age_in_months,breed,required_food_in_kgs)
        self.type = "deer"
        self.soundKeyword = "Buck Buck"
        self.breatheKeyword = "Breathe in air"
        self.growwAge = 1
        self.growwFood = 2

class Lion(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if not Animal.validator(age_in_months,breed,required_food_in_kgs):
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")

        super().__init__(age_in_months,breed,required_food_in_kgs)
        self.type = "Lion"
        self.soundKeyword = "Roar Roar"
        self.breatheKeyword = "Breathe in air"
        self.growwAge = 1
        self.growwFood = 4
    
    def hunt(self,zooObj):
        deleted = False
        for i in range(len(zooObj.animalArray) - 1, -1, -1):
            if zooObj.animalArray[i].type == 'deer':
                zooObj.animalArray.pop(i)
                deleted = True
                break
        if deleted == False:
            print("No deers to hunt")

class Shark(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if not Animal.validator(age_in_months,breed,required_food_in_kgs):
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")

        super().__init__(age_in_months,breed,required_food_in_kgs)
        self.type = "Shark"
        self.soundKeyword = "Shark Sound"
        self.breatheKeyword = "Breathe oxygen from water"
        self.growwAge = 1
        self.growwFood = 8
        

    def hunt(self,zooObj):
        deleted = False
        for i in range(len(zooObj.animalArray) - 1, -1, -1):
            if zooObj.animalArray[i].type == 'GoldFish':
                zooObj.animalArray.pop(i)
                deleted = True
                break
        if deleted == False:
            print("No GoldFish to hunt")

class GoldFish(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if not Animal.validator(age_in_months,breed,required_food_in_kgs):
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")

        super().__init__(age_in_months,breed,required_food_in_kgs)
        self.type = "GoldFish"
        self.soundKeyword = "Hum Hum"
        self.breatheKeyword = "Breathe oxygen from water"
        self.growwAge = 1
        self.growwFood = 0.2

class Snake(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if not Animal.validator(age_in_months,breed,required_food_in_kgs):
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")

        super().__init__(age_in_months,breed,required_food_in_kgs)
        self.type = "Snake"
        self.soundKeyword = "Hiss Hiss"
        self.breatheKeyword = "Breathe in air"
        self.growwAge = 1
        self.growwFood = 0.5
    
    def hunt(self,zooObj):
        deleted = False
        for i in range(len(zooObj.animalArray) - 1, -1, -1):
            if zooObj.animalArray[i].type == 'deer':
                zooObj.animalArray.pop(i)
                deleted = True
                break
        if deleted == False:
            print("No deers to hunt")

class Zoo():
    totalAnimal = 0

    @staticmethod
    def count_animals_in_all_zoos():
        print(Zoo.totalAnimal)

    @staticmethod
    def count_animals_in_given_zoos(a):
        ans = 0
        for i in range(0,len(a)):
            ans = ans + a[i].count_animals()
        print(ans)

    def __init__(self):
        self.reserved_food_in_kgs = 0
        self.animalArray = []
    
    def add_food_to_reserve(self,food):
        self.reserved_food_in_kgs = self.reserved_food_in_kgs + food
    
    def count_animals(self,):
        return len(self.animalArray)
    
    def add_animal(self,a):
        Zoo.totalAnimal = Zoo.totalAnimal + 1 
        self.animalArray.append(a)
    
    def feed(self,a):
        if self.reserved_food_in_kgs < a.required_food_in_kgs:
            print("Not Enough Food")
            return
        self.reserved_food_in_kgs = self.reserved_food_in_kgs - a.required_food_in_kgs
        a.grow()
    
    



# lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
# print(lion.age_in_months)
# print(lion.breed)
# print(lion.required_food_in_kgs)
# lion.grow()
# print(lion.required_food_in_kgs)
# print(lion.age_in_months)
# lion.make_sound() # Prints
# lion.breathe() # Prints


# shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
# print(shark.age_in_months)
# print(shark.breed)
# print(shark.required_food_in_kgs)
# shark.grow()
# print(shark.required_food_in_kgs)
# print(shark.age_in_months)
# shark.make_sound() # Prints
# shark.breathe() # Prints


# gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
# print(gold_fish.age_in_months)
# print(gold_fish.breed)
# print(gold_fish.required_food_in_kgs)
# gold_fish.grow()
# print(gold_fish.required_food_in_kgs)
# print(gold_fish.age_in_months)
# gold_fish.make_sound() # Prints
# gold_fish.breathe() # Prints

# snake = Snake(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=5)
# print(snake.age_in_months)
# print(snake.breed)
# print(snake.required_food_in_kgs)
# snake.grow()
# print(snake.required_food_in_kgs)
# print(snake.age_in_months)
# snake.make_sound() # Prints
# snake.breathe() # Prints

# zoo = Zoo()
# print(zoo.reserved_food_in_kgs)
# zoo.add_food_to_reserve(10000000)
# print(zoo.reserved_food_in_kgs)
# print(zoo.count_animals())

# gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
# zoo.add_animal(gold_fish)
# print(zoo.count_animals())
# print(zoo.reserved_food_in_kgs)
# zoo.feed(gold_fish)
# print(zoo.reserved_food_in_kgs)
# print(gold_fish.age_in_months)


# nehru_zoological_park = Zoo()
# zoo.add_food_to_reserve(10000000)
# lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
# nehru_zoological_park.add_animal(lion)
# print(nehru_zoological_park.count_animals())
# Zoo.count_animals_in_all_zoos()
# Zoo.count_animals_in_given_zoos([zoo])

# deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# nehru_zoological_park.add_animal(deer)
# print(nehru_zoological_park.count_animals())
# lion.hunt(nehru_zoological_park)
# print(nehru_zoological_park.count_animals())
# lion.hunt(nehru_zoological_park)
