# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc...)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("@passw0rd", "abc123", "guest")
logins_dates = ["1/1/2021","1/2/2021",'1/3/2021']

users = zip(usernames, passwords, logins_dates)

for i in users:
    print(i)



#users = dict(zip(usernames, passwords))

#print(type(users))

#for key,value in users.items():
    #print(key+" : "+value)