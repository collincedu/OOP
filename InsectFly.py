import InsectClass as I 

wings = int(input("how many wings does the isnect have?"))
legs = int(input("how many legs huh?"))


#this is creating an instance of the insect class
mosquito = I.Insect(2,4)
housefly = I.Insect(3,6)

mosquito.flight_length()
housefly.flight_length()

print("Mosquito flies", mosquito.get_miles(), "miles")
print("Housefly flies", housefly.get_miles(), "miles")