from bokeh.io import curdoc, output_notebook, output_file, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, Slider, HoverTool
from bokeh.palettes import brewer
from bokeh.layouts import widgetbox, row, column
import pandas as pd
import geopandas as gpd
import json
import bokeh
import os

# return df with year matched
def read_file(yr):
    base_dir = 'data'
    file_yr = str(yr)+'.csv'
    file_path = os.path.join(base_dir, file_yr)
    df = pd.read_csv(file_path)

    return df

df_2015 = read_file(2015)
df_2016 = read_file(2016)
df_2017 = read_file(2017)
df_2018 = read_file(2018)
df_2019 = read_file(2019)
df_lst = [df_2015, df_2016, df_2017, df_2018, df_2019]

# gdf file generated
shapefile = 'data/countries_110m/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
# Countries Dictionary
countries_dict = {'Czechia': 'Czech Republic', 'Democratic Republic of the Congo':'Congo (Kinshasa)',
 'Northern Cyprus':'North Cyprus', 'Republic of Serbia':'Serbia', 'Republic of the Congo': 'Congo (Brazzaville)',
 'Somaliland':'Somaliland region', 'United Republic of Tanzania': 'Tanzania','United States of America' :'United States',
 }
gdf['country'] = gdf['country'].replace(countries_dict, regex=True)


#Define function that returns json_data for year selected by user.
def json_data(selectedYear):
    df_idx = int(selectedYear)-2015
    df_yr = df_lst[df_idx]
    df_yr_proc = df_yr[['Country', 'Happiness_Score']]
    merged = gdf.merge(df_yr_proc, left_on = 'country', right_on = 'Country', how = 'left')
    merged.fillna('No data', inplace = True)
    merged_json = json.loads(merged.to_json())
    json_data = json.dumps(merged_json)
    return json_data


#Input GeoJSON source that contains features for plotting.
geosource = GeoJSONDataSource(geojson = json_data(2015))

#Define a sequential multi-hue color palette.
palette = brewer['YlGnBu'][7]

#Reverse color order so that dark blue is highest obesity.
palette = palette[::-1]

#Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors. Input nan_color.
color_mapper = LinearColorMapper(palette = palette, low = 2, high = 8, nan_color = '#d9d9d9')

#Define custom tick labels for color bar.
tick_labels = {'2': 'Index 2', '3': 'Index 3', '4':'Index 4', '5':'Index 5', '6':'Index 6', '7':'Index 7', '8':'Index 8'}

#Add hover tool
hover = HoverTool(tooltips = [ ('Country/region','@country'),('% Happiness Score', '@Happiness_Score')])


#Create color bar.
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=5,width = 650, height = 30,
                     border_line_color=None,location = (0,0), orientation = 'horizontal', major_label_overrides = tick_labels)


#Create figure object.
p = figure(title = 'Happiness Score from 2015 to 2019', plot_height = 600 , plot_width = 950, toolbar_location = None, tools = [hover])
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

#Add patch renderer to figure.
p.patches('xs','ys', source = geosource,fill_color = {'field' :'Happiness_Score', 'transform' : color_mapper},
          line_color = 'black', line_width = 0.25, fill_alpha = 1)


p.add_layout(color_bar, 'below')

# Define the callback function: update_plot
def update_plot(attr, old, new):
    yr = slider.value
    new_data = json_data(yr)
    geosource.geojson = new_data
    p.title.text = 'Happiness Score: %d' %yr

# Make a slider object: slider
slider = Slider(title = 'Year',start = 2015, end = 2019, step = 1, value = 2015)
slider.on_change('value', update_plot)

# Make a column layout of widgetbox(slider) and plot, and add it to the current document
layout = column(p,widgetbox(slider))
curdoc().add_root(layout)

#Display plot inline in Jupyter notebook
# output_file('bokeh.html')
output_notebook()

#Display plot
show(layout)
