import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt




fp = r'india-polygon.shp'
map_df = gpd.read_file(fp)
map_df.head()
data_df = pd.read_csv(r'covid_19_india.csv')
data_df.rename(columns={'State/UnionTerritory': 'st_nm'},inplace=True)
data_df.head() #check the head of the file

merged= map_df.merge(data_df, on = 'st_nm', how = 'left')
merged.head()

fig, ax = plt.subplots(1, figsize=(25, 15))
ax.axis('off')
ax.set_title('Total COVID-19 Confirmed Cases', fontdict={'fontsize': '25', 'fontweight' : '20'})

#Plotting the map using the data
merged.plot(column='Confirmed',cmap='YlOrRd', linewidth=1.5, ax=ax, edgecolor='0', legend=True,markersize=[39.739192, -104.990337])

plt.show()






merged= map_df.merge(data_df, on = 'st_nm', how = 'left')
merged.head()

fig, ax = plt.subplots(1, figsize=(25, 15))
ax.axis('off')
ax.set_title('Total COVID-19 Deaths', fontdict={'fontsize': '25', 'fontweight' : '20'})

#Plotting the map using the data
merged.plot(column='Cured',cmap='YlOrRd', linewidth=1.5, ax=ax, edgecolor='0', legend=True,markersize=[39.739192, -104.990337])

plt.show()


merged= map_df.merge(data_df, on = 'st_nm', how = 'left')
merged.head()

fig, ax = plt.subplots(1, figsize=(25, 15))
ax.axis('off')
ax.set_title('Total COVID-19 Cured Cases', fontdict={'fontsize': '25', 'fontweight' : '20'})

#Plotting the map using the data
merged.plot(column='Cured',cmap='YlOrRd', linewidth=1.5, ax=ax, edgecolor='0', legend=True,markersize=[39.739192, -104.990337])

plt.show()
