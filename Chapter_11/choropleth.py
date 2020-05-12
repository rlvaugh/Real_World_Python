from os.path import abspath
import webbrowser
import pandas as pd
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
from bokeh.sampledata.us_counties import data as counties

df = pd.read_csv('census_data_popl_2010.csv', encoding="ISO-8859-1")

df = pd.DataFrame(df,
                  columns=
                  ['Target Geo Id2',
                  'Geographic area.1',
                  'Density per square mile of land area - Population'])
                            
df.rename(columns =
          {'Target Geo Id2':'fips',
           'Geographic area.1': 'County',
           'Density per square mile of land area - Population':'Density'},
          inplace = True)

print(f"\nInitial popl data:\n {df.head()}")
print(f"Shape of df = {df.shape}\n")

# Remove non-county rows from data frame.
df = df[df['fips'] > 100]
print(f"Popl data with non-county rows removed:\n {df.head()}")
print(f"Shape of df = {df.shape}\n")

# Create columns for state and county id numbers.
df['state_id'] = (df['fips'] // 1000).astype('int64')
df['cid'] = (df['fips'] % 1000).astype('int64')
print(f"Popl data with new ID columns:\n {df.head()}")
print(f"Shape of df = {df.shape}\n")
print("df info:")
print(df.info())  # Lists data types of each column.

# Check that 5-digit fips handled correctly.
print("\nPopl data at row 500:")
print(df.loc[500])

# Make dictionary of state_id, cid tuple vs popl density.
state_ids = df.state_id.tolist()
cids = df.cid.tolist()
den = df.Density.tolist()
tuple_list = tuple(zip(state_ids, cids))
popl_dens_dict = dict(zip(tuple_list, den))

# Exclude states & territories not part of conterminious US.
EXCLUDED = ('ak', 'hi', 'pr', 'gu', 'vi', 'mp', 'as')

counties = [dict(county, Density=popl_dens_dict[cid])
            for cid, county in counties.items()
            if county["state"] not in EXCLUDED]

choropleth = hv.Polygons(counties,
                         ['lons', 'lats'],
                         [('detailed name', 'County'), 'Density'])

choropleth.opts(opts.Polygons(logz=True,
                  tools=['hover'],
                  xaxis=None, yaxis=None,
                  show_grid=False, show_frame=False,
                  width=1100, height=700,
                  colorbar=True, toolbar='above',
                  color_index='Density', cmap='Greys', line_color=None,
                  title='2010 Population Density per Square Mile of Land Area'
                  ))

hv.save(choropleth, 'choropleth.html', backend='bokeh')
url = abspath('choropleth.html')
webbrowser.open(url)
