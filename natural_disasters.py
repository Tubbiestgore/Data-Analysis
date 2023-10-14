# This will be the main program for analysis of the "natural-disasters.csv" file.
# In this data set I hope to answer the following Questions within the context of the data itself.

# Approximatly how many disasters on average happen per year?
# On average how many people die per year?
# What is the deadliest ype of disaster?
# In the last decade, how many have been made homeless because of disasters?
# 


# From those questions we can begin to answer the following major questions:
# What country is in most need of economic aid or preventative aid for disasters?
# How can we prepare for the worst kind of disaster?



import pandas as pd
data_frame = pd.read_csv("natural-disasters.csv")

# First we want to know what year does the data set begins at, and what year does it ends.
# We do this with .min, and .max. Also as a note, the data set increments by decade.
start_year = data_frame['Year'].min()
end_year = data_frame['Year'].max()
print(f"The dataset begins in the year {start_year} and ends in the year {end_year}.")

# We also want to know what kind of disasters the data set includes. Unfortunatly for this dataset
# it isn't included as a variables, so I have gone in and done that myself.
disasters = ["Drought", "Earthquake", "Storms", "Fog", "Floods", "Mass Movement", "Volcanic Activity",
             "Landslides", "Wildfires", "Extreme Temepratures", "Glacial Lake Outbursts"]
print("\nDisasters in this DataSet:")
for disaster in disasters:
    print(disaster)
print('\n')
   
# On average, how many disasters are there per year? We accomplish that with this data set by taking the entities
# which are the reporting nations. Then we group that by year, count it all up, and then average it using mean.
# We then need to divide that number by 10 to isolate year from decade.
avg_num_disasters_per_year = data_frame.groupby('Year')['Entity'].count().mean()
avg_year_disasters = avg_num_disasters_per_year / 10
rounded_avg_disasters = round(avg_year_disasters)
print(f'Average Number of Disasters Per Year: {rounded_avg_disasters}')

# On average, how many people die per year from disasters. 
# To do this, we isolate the number of deaths from disasters, take the sum of those deaths per year, find the averge
# then we again need to round and divide to isolate the approximate number.
avg_num_deaths_per_year = data_frame.groupby('Year')['Number of deaths from disasters'].sum().mean()
avg_year_deaths = avg_num_deaths_per_year / 10
rounded_avg_deaths = round(avg_year_deaths)
print(f'Average Number of Deaths Per Year From Disasters: {rounded_avg_deaths}\n')

# The method I choose to demonstrate .sort, and in order to determine which disaster is the deadliest, is to sum all of
# the disaster deaths into a list, and then use sort to determine which is the largest, and also to demonstrate its functionality.
# From this we can determine what disaster type has been the deadliest since 1900.
total_disaster_deaths_list = []

total_disaster_deaths_list.append(round(data_frame['Number of deaths from drought'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from earthquakes'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from volcanic activity'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from storms'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from floods'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from mass movements'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from fog'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from wildfires'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from landslides'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from extreme temperatures'].sum()))
total_disaster_deaths_list.append(round(data_frame['Number of deaths from glacial lake outbursts'].sum()))

print("Unsorted total deaths for each disaster type:")
print(total_disaster_deaths_list)
print('\n')

# Use sort to bring the most deaths to the top, and previous list to determine which disaster it is.
total_disaster_deaths_list.sort() 

print("Sorted total deaths for each disaster type:")
print(total_disaster_deaths_list)
print('\n')


# Now we want to isolate the number of people made homeless in the 2010-2019 decade.
# To do this we will use similiar aggregate sums with the added condition of it being within the specified timeframe.
data_in_2010s = data_frame[(data_frame['Year'] >= 2010) & (data_frame['Year'] <= 2019)]
total_homeless_2010 = data_in_2010s['Number of people left homeless from disasters'].sum()
rounded_homeless_2010 = round(total_homeless_2010)
print(f"Within the 2010 decade (2010-2019), a total of {rounded_homeless_2010} people have been made homeless.")

