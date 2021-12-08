import statistics

record0 = {
    "name": "Dawid",
    "last_name": "Michalczyk",
    "address": "Warszawa",
    "gender": True,
    "age": 25
}
record1 = {"name" : "Grazyna", "last_name" : "Kula", "address" : "Wroclaw", "gender" : False, "age" : 50}
record2 = {"name" : "Jan", "last_name" : "Kowalski", "address" : "Warszawa", "gender" : True, "age" : 25}
record3 = {"name" : "Ada", "last_name" : "Kula", "address" : "Wroclaw", "gender" : False, "age" : 50}
record4 = {"name": "Bartłomiej", "last_name": "Nowak", "address": "Kopydłów", "gender": True, "age": 23}
record5 = {"name" : "Anna", "last_name" : "Kot" , "address" : "Katowice" , "gender" : False, "age" : 38}
record6 = {"name": "Paweł", "last_name":"Jarosiński", "address":"Warszawa", "gender": True, "age": 47}
record7 = {"name" : "Maciej", "last_name" : "Urbanski", "address" : "Lipowa", "gender" : True, "age" : 44}
record8 = {"name" : "Alojzy", "last_name" : "Popiołek", "address" : "Białystok", "gender" : True, "age" : 36}



def get_data():
    return [record0, record1, record2, record3, record4, record5, record6, record7, record8]

# pobiera wszystkihc uzytkownikow, ktore maja jedna z plci i adres
# def get_data_by_gender_and_address(db_table, gender=True, address='Warszawa'):
#     return [record for record in db_table if record["gender"] == gender and record["address"] == address]

get_data_by_gender_and_address_lambda = lambda data, gender=True, address='Warszawa' : [record for record in data if record["gender"] == gender and record["address"] == address]

# def get_data_by_age(db_table, low_tresh, high_tresh):
#     return [record for record in db_table if record["age"] >= low_tresh and record["age"] <= high_tresh]

get_data_by_age_lambda = lambda data, low_tresh, high_tresh: [record for record in data if record["age"] >= low_tresh and record["age"] <= high_tresh]
    
# def get_mean_age(db_table, name_starts_with, gender):
#     result = [record["age"] for record in db_table if record["name"][0] == name_starts_with and record["gender"] == gender]
#     return statistics.mean(result) if result else 0

get_mean_age_lambda = lambda data, name_starts_with, gender : \
    statistics.mean([record["age"] for record in data if record["name"][0] == name_starts_with and record["gender"] == gender]) \
        if [record["age"] for record in data if record["name"][0] == name_starts_with and record["gender"] == gender] else 0

print(get_data_by_gender_and_address_lambda(get_data()))
print(get_data_by_age_lambda(get_data(), 30, 40))
print(get_mean_age_lambda(get_data(), 'A', False))
