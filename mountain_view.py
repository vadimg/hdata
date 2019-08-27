import json
from collections import defaultdict
from shapely.geometry import shape

from calc.mountain_view import units_per_density_limit, units_per_height, LOT_SIZE
from calc import color, key_stats

with open('data/mountain_view.geojson') as f:
    obj = json.load(f)

for o in obj['features']:
    prop = o['properties']
    zoning = prop['PRODGISGeneralPlanDesignationLANDUSECODE']
    homes_density = units_per_density_limit(zoning)
    homes_height = units_per_height(zoning)

    homes = min(homes_density, homes_height)

    if 0 < homes < 1:
        homes = 1

    prop['zoning'] = zoning
    prop['homes'] = homes
    prop['homes_zoning'] = homes_density
    prop['homes_height'] = homes_height
    prop['fill'] = color(homes)

    print(zoning, round(min(homes_density, homes_height), 1))

stats = key_stats(obj['features'], LOT_SIZE)
stats['city'] = 'Mountain View'

with open('generated/key_data.mountain_view.json', 'w') as f:
    json.dump(stats, f)

with open('generated/density_map.mountain_view.geojson', 'w') as f:
    json.dump(obj, f)