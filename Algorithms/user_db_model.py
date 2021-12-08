from statistics import mean

record0 = {
    "name": "Dawid",
    "last_name": "Michalczyk",
    "address": "Warszawa",
    "gender": True,
    "age": 25
}
record1 = {"name" : "Grazyna", "last_name" : "Kula", "address" : "Wroclaw", "gender" : False, "age" : 50}
record2 = {"name" : "Jan", "last_name" : "Kowalski", "address" : "Warszawa", "gender" : True, "age" : 25}
record3 = {"name" : "Grazyna", "last_name" : "Kula", "address" : "Wroclaw", "gender" : False, "age" : 50}
record4 = {"name": "Bartłomiej", "last_name": "Nowak", "address": "Kopydłów", "gender": True, "age": 23}
record5 = {"name" : "Anna", "last_name" : "Kot" , "address" : "Katowice" , "gender" : False, "age" : 38}
record6 = {"name": "Paweł", "last_name":"Jarosiński", "address":"Warszawa", "gender": True, "age": 47}
record7 = {"name" : "Maciej", "last_name" : "Urbanski", "address" : "Lipowa", "gender" : True, "age" : 44}
record8 = {"name" : "Alojzy", "last_name" : "Popiołek", "address" : "Białystok", "gender" : True, "age" : 36}

db_table = [record0, record1, record2, record3, record4, record5, record6, record7, record8]

# for record in db_table:
#     if record["gender"] == True and record["address"] == "Warszawa":
#         print(record)  

men_in_warsaw = [record for record in db_table if record["gender"] and record["address"] == "Warszawa"]
print(men_in_warsaw)

age_30_to_40 = [record for record in db_table if record["age"] >= 30 and record["age"] <= 40]
print(age_30_to_40)


# avg_age_where_name_like_A = [record["age"] for record in db_table if record["name"][0] == "A" and record["gender"] == False]
avg_age_where_name_like_A = [record["age"] for record in db_table if record["name"][0] == "A" and not record["gender"]]
print(avg_age_where_name_like_A)

avg_ages = mean(avg_age_where_name_like_A)
print(avg_ages)
