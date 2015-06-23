import numpy as np
import pysal as ps
import random as rdm
from pysal.contrib.viz import mapping as maps
import matplotlib.pyplot as plt

shp_link = 'transportation.shp'
shp = ps.open(shp_link)

fig = plt.figure()

base = maps.map_poly_shp(shp)
base.set_facecolor('none')
base.set_linewidth(0.75)
base.set_edgecolor('0.8')

ax = maps.setup_ax([base])
fig.add_axes(ax)
plt.show()