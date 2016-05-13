name = "Sam"
age = 19
weight = 74
country = "South Africa"
race = "Black"
hair = "Blue"


print "My name is %s" %name
print "My age is %d" %age
print "My birth country is %s" %country

#function that returns a name arg.
def get_name(name):
    return name

print "This name must be printed - %s" %get_name("khaya")
