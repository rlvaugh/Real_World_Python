from os.path import abspath
import webbrowser
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

counties = [dict(county, Unemployment=unemployment[cid])
            for cid, county in counties.items()
             if county["state"] == "tx"]

choropleth = hv.Polygons(counties, ['lons', 'lats'],
                         [('detailed name', 'County'), 'Unemployment'])

choropleth.opts(opts.Polygons(logz=True,
                              tools=['hover'],
                              xaxis=None, yaxis=None,
                              show_grid=False,
                              show_frame=False,
                              width=500, height=500,
                              color_index='Unemployment',
                              colorbar=True, toolbar='above',
                              line_color='white')) 

hv.save(choropleth, 'texas.html', backend='bokeh')
url = abspath('texas.html')
webbrowser.open(url)
