import random

class Person:
    def __init__(self, name):

        # WRITE your implementation of this function here

        pass
        self.name = name
        self.infected = False

    def __str__(self):

        # WRITE your implementation of this function here

        pass
        return "{name} - infected: {status}".format(name = self.name, status = self.infected)

class Town:
    def __init__(self, initial_population):

        # WRITE your implementation of this function here

        pass
        people_list = []
        for i in range(initial_population):
            person = Person("Person #<{number}>".format(number = i))
            people_list.append(person)
        self.people = people_list
        self.day = 0

    def tick(self, healChance, spread_chance_multiplier):
        # WRITE the code to call the appropriate function for each activity

        # Heal people
        self.heal(healChance)   #call the heal method, as the method is the class method, so we need a "self" to implement it.

        # Calculate the risk of a healthy person getting infected
        infect_chance = self.calculate_chance_to_infect(spread_chance_multiplier)  #by using "calculate_chance_to_infect", we can use the result as a parameter for other functions

        # Infect people
        self.infect(infect_chance) #from the result, we can use the "infect_chance" variable to implement infect or use the variable for further operation


        # Increment day counter
        self.day += 1      
        pass

    def heal(self, heal_chance):
        """Iterates over all infected people and heals them given heal_chance
        heal_chance = 0.6
        有百分之 40 的可能性 不能被治愈
        随机的情况下  取 [0.6,1]  0.4

        """

        # WRITE your implementation of this function here
        flag = 0 # 被治愈的人数
        infected_count = self.count_infected_people()
        for i in range(infected_count):
            x = random.random() # 随机生成数 [0-1]
            if x <= heal_chance:
                self.people[infected_count-1-flag].infected = False
                flag += 1




        

    def count_infected_people(self):
        """Returns the number of infected people"""

        # WRITE your implementation of this function here
        count = 0
        for person in self.people:
            if person.infected:
                count += 1
        return count

        pass

    def calculate_chance_to_infect(self, spread_chance_multiplier):
        """Returns the chance for a healthy person to be infected"""

        # WRITE your implementation of this function here
        return self.count_infected_people()*spread_chance_multiplier/len(self.people)

        pass

    def infect(self, infect_chance):
        """Iterates over all healthy people and infects them given infect_chance"""
        
        # WRITE your implementation of this function here
        healthy_count = len(self.people) - self.count_infected_people()
        infect_num = self.count_infected_people()
        flag = 0 # infect people
        for i in range(healthy_count):
            x = random.random()
            if x <= infect_chance:
                self.people[infect_num + flag].infected = True
                flag += 1



        pass

    def report(self):
        """Prints out a report of the current state as laid out in specification"""

        # WRITE your implementation of this function here

        print("Day {day_number}: Infected: {infected_number} / {size}".format(day_number = self.day,
         infected_number = self.count_infected_people(), size = len(self.people)))
        
        pass


def main():
    # Don't touch this line!
    random.seed(int(input("Enter seed: ")))   #this is used to generate the random number 

    # WRITE your implementation of this function here
    init_population = int(input("Enter number of people in town: "))
    heal_chance = float(input("Enter the heal chance: "))
    spread_chance_multiplier = float(input("Enter the spread chance multiplier: "))
    init_infected = int(input("Enter the initial number of infected people: "))
    days = int(input("Enter the number of days to simulate: "))
    town = Town(init_population)
    for i in range(init_infected):
        town.people[i].infected = True

    for i in range(days):
        town.tick(heal_chance, spread_chance_multiplier)
        town.report()




# DO NOT TOUCH THIS!
if __name__ == "__main__":
    main()