# This will be the main program for analysis of the "natural-disasters.csv" file.
# In this data set I hope to answer the following Questions within the context of the data itself.

# Approximatly how many disasters on average happen per year?
# On Average how many people die per year?

# From those questions we can begin to answer the following major questions:


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
print(f'Average Number of Deaths Per Year From Disasters: {rounded_avg_deaths}')