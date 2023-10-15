# This will be the main program for analysis of the several files related to natural disasters as found on "https://ourworldindata.org/".
# In this data set I hope to answer the following Questions within the context of the data itself.
# As context I want to parse through this data within the last decade.

# Major Questions: (see bottom)
# What is the average impact of natural disasters on a global scale, and what mitigation strategies might be best.
# Which countries need immediate attention regarding disaster managment?

# In order to answer those questions, let us ask some simpler questions to analyze these data sets and provde context for the answers below.

import pandas as pd

# Load the data from CSV files
economic_damages = pd.read_csv("economic-damages-from-natural-disasters-as-a-share-of-gdp.csv")
economic_damage_disaster = pd.read_csv("economic-damage-from-natural-disasters.csv")
death_data = pd.read_csv("number-of-deaths-from-natural-disasters.csv")
disaster_events = pd.read_csv("number-of-natural-disaster-events.csv")

# This will be useful later on in the program to analyze these questions. I will reiterate it several times for each data set
# In essence it boils the data down to a select decade, that being the last one. 
start_year = 2013
end_year = 2022
last_decade_economic = economic_damages[(economic_damages['Year'] >= start_year) & (economic_damages['Year'] <= end_year)]
last_decade_economic_disasters = economic_damage_disaster[(economic_damage_disaster['Year'] >= start_year) & (economic_damage_disaster['Year'] <= end_year)]
last_decade_death = death_data[(death_data['Year'] >= start_year) & (death_data['Year'] <= end_year)]
last_decade_disaster_events = disaster_events[(disaster_events['Year'] >= start_year) & (disaster_events['Year'] <= end_year)]


# Question 1:
# In order to assess the effectiveness of disaster management strategies, 
# we need to identify the country that has experienced the most damage as a percentage of their GDP, to understand the extreme effects
# which natural disasters can have on a given nation.
entity_damage_sum = last_decade_economic.groupby("Entity")[[
    "Total economic damages from natural disasters as a share of GDP - Drought",
    "Total economic damages from natural disasters as a share of GDP - Flood",
    "Total economic damages from natural disasters as a share of GDP - Earthquake",
    "Total economic damages from natural disasters as a share of GDP - Extreme weather",
    "Total economic damages from natural disasters as a share of GDP - Extreme temperature",
    "Total economic damages from natural disasters as a share of GDP - Volcanic activity",
    "Total economic damages from natural disasters as a share of GDP - Landslide",
    "Total economic damages from natural disasters as a share of GDP - Wildfire",
    "Total economic damages from natural disasters as a share of GDP - Glacial lake outburst",
    "Total economic damages from natural disasters as a share of GDP - Dry mass movement"
]].sum()

# Calcualte the total by suming up the columns.
entity_damage_sum['Total economic damages'] = entity_damage_sum.sum(axis=1)
entity_with_most_damages = entity_damage_sum['Total economic damages'].idxmax()
max_damages = entity_damage_sum['Total economic damages'].max()
print(f"The Country with the largest total in economic damages in the last decade is {entity_with_most_damages} with {max_damages:.2f} % of their GDP in total damages.")

# Question 2: 
# In order to assess the effectiveness of disaster management strategies, 
# we also need to identify the most most dangerous kind of disaster, the kind that takes away more lives than any other.

# Identify the natural disaster which occurs most frequently.
frequent_events = last_decade_disaster_events[last_decade_disaster_events['Entity'] != "All disasters"]
disaster_counts = frequent_events.groupby('Entity').count()
most_frequent_disaster = disaster_counts['Year'].idxmax()
frequency = disaster_counts['Year'].max()

print(f"The most frequently occurring natural disaster in the last decade is '{most_frequent_disaster}' with {frequency} occurrences.")

# Question 3:
# To understand the impact of natural disasters on human lives, 
# we should also analyze the number of deaths caused by these events. 
# Which country had the highest number of deaths due to natural disasters in the last decade, 
# and what were the primary disaster types responsible for these fatalities?

# For this I have to exclude some locations from the data. The data is too broad in some regards, so I excluded the following:
# If you want to add these back in, just add them by erasing them.
# I also use this later on.
excluded_locations = ['World', 'Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'High-income countries', 'Low-income countries', 'Lower-middle-income countries', 'Upper-middle-income countries', 'European Union (27)']

last_decade_death_exclusive = last_decade_death[~last_decade_death['Entity'].isin(excluded_locations)]
grouped = last_decade_death_exclusive.groupby('Entity').agg({
    'Total deaths - Drought': 'sum',
    'Total deaths - Flood': 'sum',
    'Total deaths - Earthquake': 'sum',
    'Total deaths - Extreme weather': 'sum',
    'Total deaths - Extreme temperature': 'sum',
    'Total deaths - Volcanic activity': 'sum',
    'Total deaths - Landslide': 'sum',
    'Total deaths - Wildfire': 'sum',
    'Total deaths - Glacial lake outburst': 'sum',
    'Total deaths - Dry mass movement': 'sum',
    'Total deaths - Fog': 'sum'
})

# Calculate the total deaths for each country
grouped['Total deaths'] = grouped.sum(axis=1)
country_with_highest_deaths = grouped['Total deaths'].idxmax()
highest_death_count = grouped['Total deaths'].max()
primary_disaster_types = grouped.loc[country_with_highest_deaths].drop(['Total deaths'])

print(f"\nCountry with the highest number of deaths: {country_with_highest_deaths}")
print(f"Total deaths in the last decade: {highest_death_count}")
print("Primary disaster types responsible for these fatalities:")
print(primary_disaster_types.sort_values(ascending=False).to_string())

# Question 4:
# To better understand the average impact of natural disasters on a global scale, 
# let's calculate the average number of natural disaster events that occurred annually in the last decade. 

avg_events_per_year = last_decade_disaster_events["Number of reported natural disasters"].mean()
rounded_avg = round(avg_events_per_year)
print(f"\nThe average number of natural disaster events per year in the last decade is approximately {rounded_avg} events.")

# Question 5:
# To identify the countries that need immediate attention in terms of disaster management, 
# let's sort the countries based on the total number of deaths caused by natural disasters in the last decade. 

# Had some issues regarding the sort_values needed to make a copy here - fixed the issue.
last_decade_death_copy = last_decade_death.copy()
last_decade_death_copy = last_decade_death_copy[~last_decade_death_copy['Entity'].isin(excluded_locations)]

# Sort the countries based on the total number of deaths
deaths_columns = ["Total deaths - Drought", "Total deaths - Flood", "Total deaths - Earthquake", "Total deaths - Extreme weather",
                  "Total deaths - Extreme temperature", "Total deaths - Volcanic activity", "Total deaths - Landslide",
                  "Total deaths - Wildfire", "Total deaths - Glacial lake outburst", "Total deaths - Dry mass movement", "Total deaths - Fog"]

# Calculate the total number of deaths by summing all the death columns for each country
last_decade_death_copy['Total Deaths'] = last_decade_death_copy[deaths_columns].sum(axis=1)
sorted_death_data = last_decade_death_copy.groupby("Entity")["Total Deaths"].sum().sort_values(ascending=False)

# Countries with the highest death toll
top_countries = sorted_death_data.head(5)
# Countries with the lowest death toll
bottom_countries = sorted_death_data.tail(5)

print("\nCountries with the highest death toll:")
print(top_countries.to_string())
print("\nCountries with the lowest death toll:")
print(bottom_countries.to_string())

# Answer to Major Question 1:
# I would say that the effects are obvious. Discplacement. Economic Damage. Death. Recovery Time. All are factors in the analysis of natural disasters.
# I think in this analysis one of the reasosn that you see more deaths from flooding and more droughts occuring is because these occur more, though in the 
# data, deaths from earthquakes and volcanic activity is major, it jut isn't frequent, which is of note. So I would say in order to best prepare for 
# future such events, countries will need to take steps to ensure protection against flooding and drought. Both the watery extremes as they seem to happen
# the most and cause the most death. For more isolated events such as earthquakes and volcanos, certain steps will also need to be taken, but should be of
# lower priority.

# Answer to Major Question 2:
# As demonstrated by our analysis in the first question and 5th, Dominica had about 368 % of their total GDP represented in damages caused by natural disasters.
# That was only in the last decade alone. I would say that countries taht need our immediate attention are those whose damages from natural disasters
# exceed about 75 % GDP. The odds of them recovering on their own are not high when it goes above this points, as they can't producce enough to meet 
# the environmental demand, let alone their own citizens. Some other nations of note which might require relief are third world nations (excluded beacuse of the broadness in this data set)
# or developing countries such as India. Other nations such as Italy France, and Spain might also require aid from time to time based on current circumstances.