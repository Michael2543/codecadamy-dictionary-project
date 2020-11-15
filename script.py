# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def convert_str_into_float(lists):
  new_damages = []
  for entry in lists:
    if entry == "Damages not recorded":
      new_damages.append("Damages not recorded")
    elif "M" in entry:
      entry = entry [:-1]
      new_damages.append(float(entry) * 1000000)
    else:
      entry = entry[:-1]
      new_damages.append(float(entry) * 1000000000)  
  return new_damages

damages = convert_str_into_float(damages)

# write your construct hurricane dictionary function here:

#Solved this with a list comprehension.

def construct_hurricane(name, month, year, max_sustained_winds, areas_affected, damages, deaths):
  zipped_hurricanes = {name : {'Name' : name, 'Month' : month,'Year' : year, 'Max Sustained Wind' :  max_sustained_winds, 'Areas Affected' : areas_affected, 'Damages' : damages, 'Deaths' : deaths} for name, month, year, max_sustained_winds, areas_affected, damages, deaths in zip(name, month, year, max_sustained_winds, areas_affected, damages, deaths)}
  return(zipped_hurricanes)

#Test 
zipped_hurricanes = construct_hurricane(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# write your construct hurricane by year dictionary function here:


def sort_by_year(zipped_hurricanes):
  sorted_by_year = {}
  for element, value in zipped_hurricanes.items():
    value_as_list = []
    for key, value2 in value.items():
      value_as_list.append({key : value2})
    sorted_by_year[value.get("Year")] = value_as_list
  return sorted_by_year

print(sort_by_year(zipped_hurricanes))


# write your count affected areas function here:

def count_affected_areas(zipped_hurricanes):
  dict_with_count = {}
  for element, value in zipped_hurricanes.items():
    list_of_affected_areas = value.get("Areas Affected")
    for area in list_of_affected_areas:
      if area in dict_with_count:
        dict_with_count[area] += 1
      else:
        dict_with_count[area] = 1
  return dict_with_count

affected_areas = count_affected_areas(zipped_hurricanes)


# write your find most affected area function here:

def get_highest(affected_areas):
  highest_value = 0
  area_with_highest = ""
  dict_for_highest = {}
  for element, value in affected_areas.items():
    if value > highest_value:
      highest_value = value
      area_with_highest = element
  
  dict_for_highest[area_with_highest] = highest_value
  
  return dict_for_highest      

print(get_highest(affected_areas))


# write your greatest number of deaths function here:

def get_highest_death_toll(zipped_hurricanes):
  highest_value = 0
  hurricane_name = ""
  for key, value in zipped_hurricanes.items():
    if value["Deaths"] > highest_value:
      highest_value = value["Deaths"]
      hurricane_name = key
  return print(f"The Hurricane with the highest Death toll of {highest_value} was {hurricane_name}")

get_highest_death_toll(zipped_hurricanes)



# write your catgeorize by mortality function here:

def get_categorized_mortality (zipped_hurricanes):
  mortality_scale = {}
  for key, value in zipped_hurricanes.items():

    if value["Deaths"] <= 0:
      if "0" in mortality_scale:
        mortality_scale[0].append(value)
      else:
        mortality_scale["0"] = [value]


    elif value["Deaths"] > 0 and value["Deaths"] <= 100:
      if "1" in mortality_scale:
        mortality_scale["1"].append(value)
      else:
        mortality_scale["1"] = [value]


    elif value["Deaths"] > 100 and value["Deaths"] <= 500:
      if "2" in mortality_scale:
        mortality_scale["2"].append(value)
      else:
        mortality_scale["2"] = [value]


    elif value["Deaths"] > 500 and value["Deaths"] <= 1000:
      if "3" in mortality_scale:
        mortality_scale["3"].append(value)
      else:
        mortality_scale["3"] = [value]


    elif value["Deaths"] > 1000 and value["Deaths"] <= 10000:
      if "4" in mortality_scale:
        mortality_scale["4"].append(value)
      else:
        mortality_scale["4"] = [value]
    
    
    else:
      if "5" in mortality_scale:
        mortality_scale["5"].append(value)
      else:
        mortality_scale["5"] = [value]
  
  return mortality_scale

#Learned here that pre initialisating would safe a lot of time
print(get_categorized_mortality(zipped_hurricanes)["5"])





# write your greatest damage function here:

def get_greatest_damage(zipped_hurricanes):
  highest_damage = 0
  name_highest_damage = ""
  for key, value in zipped_hurricanes.items():
    if value["Damages"] == "Damages not recorded":
      continue
    elif value["Damages"] > highest_damage:
      highest_damage = value["Damages"]
      name_highest_damage = key
  
  hurricane_with_highest_damage = {name_highest_damage : highest_damage}
  return hurricane_with_highest_damage

print(get_greatest_damage(zipped_hurricanes))



# write your catgeorize by damage function here:

def categorize_by_damage(zipped_hurricanes):
  damage_scale = {}

  for key, value in zipped_hurricanes.items():

    if value["Damages"] == "Damages not recorded":
      continue
    
    
    elif value["Damages"] <= 0:
      if "0" in damage_scale:
        damage_scale["0"].append(value)
      else:
        damage_scale["0"] = [value]


    elif value["Damages"] > 0 and value["Damages"] <= 100000000:
      if "1" in damage_scale:
        damage_scale["1"].append(value)
      else:
        damage_scale["1"] = [value]


    elif value["Damages"] > 100000000 and value ["Damages"] <= 1000000000:
      if "2" in damage_scale:
        damage_scale["2"].append(value)
      else:
        damage_scale["2"] = [value]


    elif value["Damages"] > 1000000000 and value["Damages"] <= 10000000000:
      if "3" in damage_scale:
        damage_scale["3"].append(value)
      else:
        damage_scale["3"] = [value]


    elif value["Damages"] > 10000000000 and value["Damages"] <= 50000000000:
      if "4" in damage_scale:
        damage_scale["4"].append(value)
      else:
        damage_scale["4"] = [value]


    else:
      if"5" in damage_scale:
        damage_scale["5"].append(value)
      else:
        damage_scale["5"] = [value]
  return damage_scale

#Learned here that pre-initialisating would safe a lot of time
print(categorize_by_damage(zipped_hurricanes)["5"])

