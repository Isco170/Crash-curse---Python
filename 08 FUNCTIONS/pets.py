
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Positional arguments
# describe_pet('hamster', 'harry')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')


