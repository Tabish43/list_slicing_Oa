cities = ["islamabad" , "lahore" , "karachi" , "peshawar" , "quetta"]
# print 4th city 
print ("Welcome to"  +  cities [3] )
# print 1st city 
print ("see beautiful city" + cities [0] )
# print 5th city 
print ("land of nature" + cities [4] )
# print 2nd city 
print ("place of chichore" + cities [1] )
# print 3rd city 
print ("heart of Pakistan" + cities [2] )
# for add in the last of list we use append function in list
cities.append ("hyderabad")
# the print to check command is right or wrong
print (cities)
# for insert at favorite place we use insert function in list
cities.insert(2, "rawalpindi")
# print to check the command
print (cities)
# for print from 3rd to 5th 
print (cities[2:5])
# for print till 3rd
print (cities[:3])
# for print next to 4th
print (cities[4:])
# for remove item from list we use del(delete) function
del cities [1]
# to check delete was done! or not?
print (cities)
# for remove to call the original name we use remove function
cities.remove ("quetta")
# to check remove work or not
print (cities)
# there's another method for remove to call key "pop function" 
cities.pop (2)
# print to check
print (cities)
# cities.insert(2, cities.pop(2))
# print (cities)


# End!!!!!!!!