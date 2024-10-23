
class Animals:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
        self.diet = diet

    def eat(self):
        print(f"{self.name} is eating {self.diet}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")

    def move(self):
        print(f"{self.name} is moving around.")



class Reptiles(Animals):
    def __init__(self, name, age, weight, habitat, diet, scales_type):
        super().__init__(name, age, weight, habitat, diet)
        self.scales_type = scales_type

    def crawl(self):
        print(f"{self.name} is crawling.")

    def shed_skin(self):
        print(f"{self.name} is shedding its skin.")

    def bask_in_sun(self):
        print(f"{self.name} is basking in the sun.")

    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")



snake = Reptiles("Snake", 5, 2, "Forest", "Carnivore", "Smooth")
lizard = Reptiles("Lizard", 3, 0.5, "Desert", "Insectivore", "Rough")
turtle = Reptiles("Turtle", 100, 150, "Ocean", "Herbivore", "Hard")



class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet, strength):
        super().__init__(name, age, weight, habitat, diet)
        self.strength = strength

    def run(self):
        print(f"{self.name} is running.")

    def hunt(self):
        print(f"{self.name} is hunting.")

    def nurture_young(self):
        print(f"{self.name} is nurturing its young.")

    def communicate(self):
        print(f"{self.name} is communicating with others.")



lion = Mammals("Lion", 8, 190, "Savannah", "Carnivore", "Very strong")
elephant = Mammals("Elephant", 25, 5000, "Savannah", "Herbivore", "Extremely strong")
kangaroo = Mammals("Kangaroo", 5, 70, "Outback", "Herbivore", "Strong legs")



class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name
        self.ticket_price = ticket_price
        self.animal_performer = animal_performer
        self.tickets_sold = 0

    def perform_show(self):
        print(f"{self.animal_performer.name} is performing in the show '{self.show_name}'.")

    def display_info(self):
        print(f"Show Name: {self.show_name}")
        print(f"Ticket Price: {self.ticket_price}$")
        print(f"Animal Performer: {self.animal_performer.name}")
        self.animal_performer.make_sound()

    def sell_ticket(self, quantity):
        self.tickets_sold += quantity
        print(f"Sold {quantity} tickets.")

    def calculate_revenue(self):
        revenue = self.tickets_sold * self.ticket_price
        print(f"Total revenue: {revenue}$")



lion_show = ZooShow("The Mighty Lion", 20, lion)
lion_show.display_info()
lion_show.sell_ticket(100)
lion_show.calculate_revenue()
lion_show.perform_show()

