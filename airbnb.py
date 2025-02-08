"""airbnb listing activity and metrics in NYC, NY for 2019"""
from tkinter.messagebox import ABORT

#read data
import pandas as pd

#visualize data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#configure visualizations
plt.rcParams['figure.figsize'] = [8,4]
sns.set_theme(style = "darkgrid")

listings = pd.read_csv("/Users/hostname/Downloads/PROJECTS/AB_NYC_2019.csv")
print(listings.shape) #obtain the shape of the dataset
#print(listings.head(4))


#explore data
#print(listings.columns) to get column names

groupbyneighbourhood = listings.groupby(['neighbourhood'],as_index= False)['id'].count() 
#counting each time a neighbourhood shows

print(groupbyneighbourhood)
top10= groupbyneighbourhood.sort_values(['id'],ascending=False).head(10)
print("____________________") 
print(top10)


#visualization
sns.barplot(data=top10,y="neighbourhood",x='id').set_title('Top 10 Bookings')
plt.show() 
