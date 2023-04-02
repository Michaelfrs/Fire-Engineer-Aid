# This is to calculate the friction loss formula

print("Hose coeffiecients: 1 3/4 in = 15.5, 2 1/2 in = 2, 3 in = 0.8, 5 in = 0.08")

coefficient = float(input("What is your hose coefficient? "))
gpm = int(input("What is the GPM of your nozzle? "))
length = int(input("What is the length of the hose? "))
nozzle_pressure = int(input("What is the nozzle pressure? "))

friction_loss = coefficient * (gpm / 100)**2 * (length / 100) + nozzle_pressure

print("Your pump pressure for this hose is", friction_loss)