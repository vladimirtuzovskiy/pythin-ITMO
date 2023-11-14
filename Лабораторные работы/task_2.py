city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

max_population = 5  # Пороговое значение для населения

#num_cities = 0
#for city_dict in city_list:
#    if city_dict["population"] < max_population:
#        num_cities += 1

#print(f"Количество городов с население до 5 млн. жителей равно = {num_cities}")

list_cities = [city_dict for city_dict in city_list if city_dict["population"] < max_population]

print(f"Количество городов с население до 5 млн. жителей равно = {len(list_cities)}")

