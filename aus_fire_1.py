import plotly
import json
import csv
from datetime import datetime

in_file = 'MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2019331.txt'

with open(in_file) as x:
    read_file = csv.reader(x)
    header_row = next(read_file)

    dates, bright,lons,lats = [],[],[],[]

    row = 0

    for row in read_file:
        brights = float(row[2])
        date = datetime.strptime(row[5], '%Y-%m-%d')

        dates.append(date)
        lons.append(row[1])
        lats.append(row[0])
        bright.append(brights)


from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

data = [{'type': 'scattergeo', 
    'lon': lons, 'lat': lats, 
    'marker': 
        {'color': bright, 
        'colorbar': 
            {'title': 'Brightness'}}}]


my_layout = Layout(title="Australian Wildfires")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='australian_fires.html')