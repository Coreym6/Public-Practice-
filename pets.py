#generic information to take in info about a pet
# Path: pets.py 
class Owner : # will likely re order this to the beginning of the program 
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.address = input("Enter your address: ")
        self.phone_number = input("Enter your phone number: ")
        self.owner_information = [] # This is the list of dogs that the owner has
        self.owner_information.append(self.name) # check this line because I'm not sure if it's correct 
    '''Matrix = []
    for i in range(4):
        Matrix.append([])
        for j in range(4):
            Matrix[i].append(j)
            Print(Matrix[i][j], end = " ")'''
    #def dog_information(self):
    # https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/

    def dog_information(self):
        self.dog_name = input("Enter the name of your dog: ")
        self.dog_breed = input("Enter the breed of your dog: ")
        self.dog_age = int(input("Enter the age of your dog: "))
        self.dog_weight = int(input("Enter the weight of your dog: "))
        self.dog_height = int(input("Enter the height of your dog: "))
        self.dog_vaccination = input("Enter the vaccination history of your dog: ") # Edit some of these questions 
        self.dog_information.append(self.dog_name)
        self.dog_information.append(self.dog_breed)
        self.dog_information.append(self.dog_age)
        self.dog_information.append(self.dog_weight)
        self.dog_information.append(self.dog_height)
        self.dog_information.append(self.dog_vaccination)
        print(self.dog_information)
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
        #print("Your dog is a {} and is {} years old".format(self.dog_breed, self.dog_age))
    # this is just an general idea, Could I possibly take in factors of the input and have the program guess what dog it is based if say "weight is between 20-30 pounds" and "height is between 10-15 inches" and "age is between 1-3 years old" and "vaccination history is up to date" then it would be a "pug" or something like that.
    #SORT THE ABOVE LIST INFORMATION BY AGE, WEIGHT, HEIGHT, VACCINATION HISTORY, BREED, NAME, ETC.
    def cat_information(self):
        self.cat_question = input("Do you have a cat? ")
        if self.cat_question == "no":
            print("You don't have a cat")
            return
        else:
            print("You have a cat")
            print("What is the name of your cat?")
            self.cat_name = input("Enter the name of your cat:")
            self.cat_breed = input("Enter the breed of your cat: ")
            self.cat_age = int(input("Enter the age of your cat: "))
            self.cat_weight = int(input("Enter the weight of your cat: "))
            self.cat_height = int(input("Enter the height of your cat: "))
            self.cat_vaccination = input("Enter the vaccination history of your cat: ")

    # Add a combined list function to this Owner class

class Dog:
     
    dog = True
    dog_information = [] # This is the master list of all the dogs information that will be stored in the program 
Owner = input("do you have a dog?")
if Owner == "yes":
    print("Oh that's nice what dog do you have?")
    # Ask how many dogs the person has
num_dogs = int(input("How many dogs do you have? "))

    # If the person has more than 1 dog, ask for each individual name
if num_dogs > 1:
        dog_names = []
        for i in range(num_dogs):
            dog_name = input("Enter the name of dog {}: ".format(i+1))
            dog_names.append(dog_name)
        
        # Print the names of the dogs
        print("The names of your dogs are:")
        for name in dog_names:
            print(name)
#Array list order,1. dog name 2. owner name 3. dog breed, 4.dog age, 5. dog weight and height, 6. number of years owned, 7. vacination history 
    # If the person has 1 dog, print the name of the dog
            # ask about the 
def dog_breed():
    breed_list = [] 
    dog_breed = input("what breed is your dog(s)?")
    breed_list.append(dog_breed)


def dog_age():
    # add an age for the dog(s)
    #add something for the dogs to be assigned to the list of names in "dog_names"
    dog_age = int(input("how old is your dog(s)?"))
    age_list = []
    for dog_age in range(1, 12):
        print("awesome they're still very young")
        if dog_age > 4 & dog_age < 10:#might have to redo the range for this statement
            print("Ah man that's a good age for a dog"+ "how long have you had them for?")
            owner_time = int(input("how long have you had them for?"))
        else: print()
        if owner_time > 1 & owner_time < 3:
                print("What kennel or where did you get them from?")
                kennel = input("Where did you get them from?")
                print("Oh that's nice I've heard of them before")
        else:
                print("That's a very long time to have that dog for")
                kennel = input("Where did you get them from?")
            
    '''if dog_age > 1 & dog_age <6:
        print("That's awesome how long ")
    else:
        print("Oh that's nice what dog do you have") '''

def combined_description():
    print("Your dog(s) is/are a {} and is/are {} years old".format(dog_breed, dog_age))
    # this is good for right now. 

#implement the sorting algorithms that I had in mind for the program. Definitly a sort is needed, possibly by age, alphabetically sort by the breed, list it out
def list_dogs():
    print("The names of your dogs are:")
    for name in dog_names:
        print(name)
def sort_lineup_dogs():
    print("this is a place holder for the sort function") 

'''if dog == true:
    print("Oh that's nice what dog do you have") '''
# actually I just thought about it, what if I do cats and dogs. I could do a so