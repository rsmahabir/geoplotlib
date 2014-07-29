import sys,os
sys.path.append(os.path.realpath('..'))

import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox


data = read_csv('./data/loc-andrea-prod-resampled.csv')
geoplotlib.hist(data)
geoplotlib.set_bbox(BoundingBox.DTU)
geoplotlib.show()
