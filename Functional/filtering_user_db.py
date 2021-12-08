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
record3 = {"name" : "Grazyna", "last_name" : "Kula", "address" : "Wroclaw", "gender" : False, "age" : 50}
record4 = {"name": "Bartłomiej", "last_name": "Nowak", "address": "Kopydłów", "gender": True, "age": 23}
record5 = {"name" : "Anna", "last_name" : "Kot" , "address" : "Katowice" , "gender" : False, "age" : 38}
record6 = {"name": "Paweł", "last_name":"Jarosiński", "address":"Warszawa", "gender": True, "age": 47}
record7 = {"name" : "Maciej", "last_name" : "Urbanski", "address" : "Lipowa", "gender" : True, "age" : 44}
record8 = {"name" : "Alojzy", "last_name" : "Popiołek", "address" : "Białystok", "gender" : True, "age" : 36}



def get_data():
    return [record0, record1, record2, record3, record4, record5, record6, record7, record8]

# pobiera wszystkihc uzytkownikow, ktore maja jedna z plci i adres
def get_data_by_gender_and_address(db_table, gender=True, address='Warszawa'):
    return [record for record in db_table if record["gender"] == gender and record["address"] == address]

def get_data_by_age(db_table, low_tresh, high_tresh):
    return [record for record in db_table if record["age"] >= low_tresh and record["age"] <= high_tresh]
    
def get_mean_age(db_table, name_starts_with, gender):
    result = [record["age"] for record in db_table if record["name"][0] == name_starts_with and record["gender"] == gender]
    return statistics.mean(result) if result else 0

gender = True
address = "Warszawa"
low_tresh = 20
high_tresh = 40
name_starts_with = 'A'
gender = False

def get_data_by_gender_and_address_filter(record):
    global gender, address
    return record["gender"] == gender and record["address"] == address

def get_data_by_age_filter(record):
    global low_tresh, high_tresh
    return record["age"] >= low_tresh and record["age"] <= high_tresh
    
def get_mean_age_filter(record):
    global name_starts_with, gender
    female = record["name"][0] == name_starts_with and record["gender"] == gender
    result = female['age']
    return statistics.mean(result)
    
    # record["age"] for record in db_table if record["name"][0] == name_starts_with and record["gender"] == gender
db_table = get_data()
#user list sorted by last name

def sort_by_last_name(record):
    return record['last_name']
    
print(sorted(db_table, key = sort_by_last_name))

#user listed sorted by age and gender

def sort_by_age_and_gender(record):
    return record['gender'], record['age']

print(sorted(db_table, key = sort_by_age_and_gender))

# print(get_data_by_gender_and_address(db_table, False, 'Katowice'))
# print(get_data_by_age(db_table, 20, 30))
# print(get_mean_age(db_table, 'A', False))

# f = filter(get_mean_age_filter, get_data())
# print(*f)

