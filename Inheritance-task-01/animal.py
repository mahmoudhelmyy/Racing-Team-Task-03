class Animal:
    def __init__(self, name, category, age):
    #Attributes or Properties of an Animal
        self.__name = name                      #Private Attributes
        self.__category = category
        self.__age = age
    #Getter Function
    def show_animal_details(self):
        print("The name of animal is", self.__name )                         #Get Your Animal Name
        print("The category of animal is", self.__category)                  #Know Your Animal Category
        print("The age of animal is", self.__age, "Years")                    #How Many Years the Animal has ?
                                                               
    def set_animal_details(self,setname):                           #Setter Function
        self.__name = setname

# Horse Properties
class horse(Animal):
    def __init__(self, name, category, age,speed,color):
        super().__init__(name, category, age)
        self.horse_speed = speed
        self.horse_color = color

    def show_horse_speed(self):
        print("The Horse Speed is", self.horse_speed, "km/h")
    def show_horse_color(self):                                                  #Getter Functions
        print("The Horse Color is", self.horse_color)

    def set_horse_speed(self,setspeed):
        self.horse_speed = setspeed                                             #Setter Functions

    def set_horse_color(self,setcolor):
        self.horse_color = setcolor

# Fish Properties
class Fish(Animal):
    def __init__(self, name, category, age, paws):
        super().__init__(name, category, age)
        self.number_of_fins = paws
        print("A fish has", self.number_of_fins, "fins")

#Horse Output
horse = horse("horse","Draught Horse",9,110,"Grey")
horse.show_animal_details()
horse.show_horse_color()
horse.show_horse_speed()
print("-----------------------------------------------------")

#Fish Output
fish = Fish("fish","bony fish", 10, 4)
fish.show_animal_details()

