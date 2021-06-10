from deepforest import utilities
import re
import math


def LatLonToMeters(lat, lon):
    originShift = 2 * math.pi * 6378137 / 2.0
    mx = lon * originShift / 180.0
    my = math.log(math.tan((90 + lat) * math.pi / 360.0 )) / (math.pi / 180.0)
    my = my * originShift / 180.0
    return mx, my

def MetersToPixels(mx, my):
    res = 0.074645535
    originShift = 2 * math.pi * 6378137 / 2.0
    px = (mx + originShift) / res
    py = (my + originShift) / res
    return px, py

def PixelsToMeters(px, py):
    res = 0.074645535
    originShift = 2 * math.pi * 6378137 / 2.0
    mx = px * res - originShift
    my = py * res - originShift
    return mx, my

def MetersToLatLon( mx, my ):
    originShift = 2 * math.pi * 6378137 / 2.0
    lon = (mx / originShift) * 180.0
    lat = (my / originShift) * 180.0
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180.0)) - math.pi / 2.0)
    return lat, lon

def global_calculator(center_lat, center_lon, tree_x_pix, tree_y_pix):
    mx, my = LatLonToMeters(center_lat,center_lon)
    center_x, center_y = MetersToPixels(mx, my)
    x = center_x + tree_x_pix - 640
    y = center_y - tree_y_pix + 640 # axes inversés
    mx, my = PixelsToMeters(x, y)
    return MetersToLatLon(mx, my)

def calculate_tree_positions(xml_file):
	df = utilities.xml_to_annotations(xml_file)
	df['latitude'] = ''
	df['longitude'] = ''
	for index, row in df.iterrows():
		tree_x_pix = (df['xmin'][index] + df['xmax'][index]) / 2
		tree_y_pix = (df['ymin'][index] + df['ymax'][index]) / 2
		center_lat, center_lon = extract_center_from_filename(df['image_path'][index])
		lat_tree, lon_tree = global_calculator(center_lat, center_lon, tree_x_pix, tree_y_pix)
		df.loc[index, 'latitude'] = lat_tree
		df.loc[index, 'longitude'] = lon_tree
	return df

def extract_center_from_filename(filename):
	center = re.search(r'_{1}(\d*.\d*)_{1}(\d*.\d*)_', filename)
	lat = float(center.group(1))
	lon = float(center.group(2))
	return lat, lon

df = calculate_tree_positions('Hack4Nature/data/labels_43.2863_5.3909_a9CTV64.xml')
print(df)