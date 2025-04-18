# Assuming the Pet class has already been defined as above

# Create a pet object
my_pet = Pet("Charlie")

# Check initial status
my_pet.get_status()

# Feed the pet
my_pet.eat()

# Let the pet sleep
my_pet.sleep()

# Let the pet play
my_pet.play()

# Train the pet with a new trick
my_pet.train("roll over")
my_pet.train("fetch")

# Try teaching a duplicate trick
my_pet.train("roll over")

# Show all learned tricks
my_pet.show_tricks()

# Final status
my_pet.get_status()
