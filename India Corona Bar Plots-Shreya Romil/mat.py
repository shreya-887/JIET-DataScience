import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px




#For Reading CSV Database Files
covid19_df = pd.read_csv("./datasets/covid_19_india.csv")
covid19_df.head()
covid19_df_latest = covid19_df[covid19_df['Date']=="16/06/20"]
covid19_df_latest.head()


#Interactive Graph of Confirmed Cases
covid19_df_latest = covid19_df_latest.sort_values(by=['Confirmed'], ascending = True)
plt.figure(figsize=(30,15), dpi=240)
dbar = px.line(covid19_df_latest,x="Confirmed",y="State/UnionTerritory",color="Confirmed",title="layout.hovermode='closest' (the default)")
dbar.update_traces(mode = "markers+lines")
dbar.show()
plt.ylabel('Number of Maximum Confirmed Cases', size = 12)
plt.title('States with maximum confirmed cases', size = 16)
plt.show()



#Interactive Graph of Deaths
covid19_df_latest = covid19_df_latest.sort_values(by=['Confirmed'], ascending = True)
plt.figure(figsize=(30,15), dpi=240)
dbar = px.line(covid19_df_latest,x="Deaths",y="State/UnionTerritory",color="Confirmed",title="layout.hovermode='closest' (the default)")
dbar.update_traces(mode = "markers+lines")
dbar.show()
plt.ylabel('Number of Maximum Deaths', size = 12)
plt.title('States with maximum Deaths', size = 16)
plt.show()


#Interactive Graph of Recovered
covid19_df_latest = covid19_df_latest.sort_values(by=['Confirmed'], ascending = True)
plt.figure(figsize=(30,15), dpi=240)
dbar = px.line(covid19_df_latest,x="Cured",y="State/UnionTerritory",color="Confirmed",title="layout.hovermode='closest' (the default)")
dbar.update_traces(mode = "markers+lines")
dbar.show()
plt.ylabel('Number of Maximum Recoveries', size = 12)
plt.title('States with maximum Recoveries', size = 16)
plt.show()




#Bar Graph of Confirmed
covid19_df_latest = covid19_df_latest.sort_values(by=['Confirmed'])
plt.figure(figsize=(15,10), dpi=120)
dbar = plt.barh(covid19_df_latest['State/UnionTerritory'][:35], covid19_df_latest['Confirmed'][:35],
        align='center' ,color= ['yellow'], edgecolor='white')

plt.ylabel('Number of Confirmed Cases', size = 12)
plt.title('States with maximum Confirmed Cases', size = 16)
plt.show()


#Bar Graph of Deaths
covid19_df_latest = covid19_df_latest.sort_values(by=['Deaths'])
plt.figure(figsize=(15,10), dpi=120)
dbar = plt.barh(covid19_df_latest['State/UnionTerritory'][:35], covid19_df_latest['Deaths'][:35],
        align='center' ,color= ['red'], edgecolor='red')

plt.ylabel('Number of Deaths', size = 12)
plt.title('States with maximum deaths', size = 16)
plt.show()

#Bar Graph of Recovered Patients
covid19_df_latest = covid19_df_latest.sort_values(by=['Cured'])
plt.figure(figsize=(15,10), dpi=120)
dbar = plt.barh(covid19_df_latest['State/UnionTerritory'][:35], covid19_df_latest['Deaths'][:35],
        align='center' ,color= ['green'], edgecolor='red')

plt.ylabel('Number of Recovered Patients', size = 12)
plt.title('States with maximum Recovered Patients', size = 16)
plt.show()

