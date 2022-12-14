# imports
from fuzzify import *
from ascii_art import washing_machine_art as art

# washing parameters
def compute_washing_parameters(type_of_dirt, degree_of_dirt):

    if type_of_dirt < 0.0 or type_of_dirt > 100.0:
        raise Exception("Invalid Type of Dirtiness: %lf" % type_of_dirt)
    if degree_of_dirt < 0.0 or type_of_dirt > 100.0:
        raise Exception("Invalid Degree of Dirtiness: %lf" % degree_of_dirt)

    type_fuzzy = fuzzify_laundry(type_of_dirt, degree_of_dirt)

    return type_fuzzy


if __name__ == "__main__":
    type_of_dirt = float(input("Enter Type of Dirt [0-100]: "))
    degree_of_dirt = float(input("Enter Degree of Dirtiness [0-100]: "))
    washing_time = round(compute_washing_parameters(type_of_dirt, degree_of_dirt), 2)
    print(f"{art}\nTime required to wash is {washing_time} minutes.\n")
