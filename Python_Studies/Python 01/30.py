## sort() method = used with lits
# sort() function = used with iterables


##LEVEL 1
#students = ["Breno", "Farias", "Isac", "Dornelas"]
#students.sort()
##students = ("Breno", "Farias", "Isac", "Dornelas")

#sorted_students = sorted(students, reverse=True)

#for i in sorted_students:
    #print(i)

### LEVEL 2

#students = [("Breno", "F", 56),
            #("Farias", "A", 34), 
            #("Isaac", "B", 45), 
            #("Carbono", "C", 96), 
            #("Dornelles", "D", 20)]

#grade = lambda grades:grades[1] 
age = lambda ages:ages[2]
#students.sort(key=age,)
#for i in students:
    #print(i)

### USING TUPLES

students = (("Breno", "F", 56),
            ("Farias", "A", 34), 
            ("Isaac", "B", 45), 
            ("Carbono", "C", 96), 
            ("Dornelles", "D", 20))

sorted_students = sorted(students,key=age)
for i in students:
    print(i)