#normal integer type
cars = 100
print "cars is of type: ", type(cars)
#floating point because of the decimal
space_in_car = 4.0
print "space_in_car is of type: ", type(space_in_car)
passengers = 100
drivers = 30

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
print "carpool_capacity is of type: ", type(carpool_capacity)
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, " cars available."
print "The are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

print "Hi %s, welcome to python." % "Khaya"
