#!/usr/bin/env python3

def searchPerson(database, pan_no) :
    for i in range(len(database)):
        if( database[i].pan_no == pan_no ) :
            return (people[i],i)

def sortPerson(database, sort_param) :
    l = len(database)

    param = {
        "name" : "name",
        "age" : "age",
        "pan_no" : "pan_no",
        "sex" : "sex",
        "address" : "address",
        "ph_no" : "ph_no"
    }
    # print(param[sort_param])
    # print(param.get(sort_param))

    for i in range(l):
        for j in range(l-i-1):
            if (database[j].pan_no > database[j+1].pan_no ) :
                database[j],database[j+1] = database[j+1],database[j]
    return (database)


class Person :
    """
    docstring for Person
    """
    def __init__(self, name, age, pan_no, sex, address, ph_no) :
        # super(ClassName, self).__init__()
        self.name = name
        self.age = int(age)
        self.pan_no = int(pan_no)
        self.sex = sex
        self.address = address
        self.ph_no = int(ph_no)

    def __str__(self) :
        if (self.sex == "M") :
           gender = "Male" 
        else :
           gender = "Female" 

        return (" %-20s \t %010d \n %-20s \t %s \n %-20s \t %010d \n"%(self.name, self.ph_no, self.age, self.address, gender, self.pan_no) )

    def setPerson(self, name, age, pan_no, sex, address, ph_no) :
        # super(ClassName, self).__init__()
        self.name = name
        self.age = int(age)
        self.pan_no = int(pan_no)
        self.sex = sex
        self.address = address
        self.ph_no = int(ph_no)

p = Person("Aditya Agarwal",12,123456,"M","Agra",9911502984)

population = int(input("Enter the number of People : "))
people = [True]*population
for i in range((population-1)):
    people[i] = p

people[i+1] = Person("Aditya ",12,123,"M","Agra",9911502984)
people[0] = Person("Aditya ",12,12345,"M","Agra",9911502989)

people[0].setPerson("Aditya ",12,12345890,"M","Agra",9911502989)



print("Mock Details For %d People Filled !\n"%(population))

# searched = searchPerson(people, 123)
# print (searched[0])
# print (" at " + str(searched[1]) + " position ")

people = sortPerson(people, "pan_no")
for i in range((population)):
    print (people[i])
print ("-"*70)

# if( database[i].param[sort_param] >= database[i+1].param[sort_param]) :
#     database[i].param[sort_param] , database[i+1].param[sort_param] = database[i+1].param[sort_param] , database[i].param[sort_param]