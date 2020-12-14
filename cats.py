# Goal is to build a system in which there are specific rules and there are rules of how those roles interact. These rules were designed by one of more people on a team.

# How to create a class:
# Describe the system (what belongs to all things in the class)
# Pick out the nouns ()
# Pick out the verbs (These are the the methods, the things this thing can do! Have the appropriate behaviors)


class Cat:
    # CLASS ATTRIBUTE - Applies to all cats!
    species = "Mammal"

    # INSTANCE ATTRIBUTE - Different for each INSTANCE of cat
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # INSTANCE METHOD - Different for each INSTANCE of cat
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)


gus = Cat("Gus", 10)
beans = Cat("Beans", 11)

print(gus.description())
print(beans.description())
