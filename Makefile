all: sf mountain_view

.PHONY: all clean sf mountain_view

clean:
	rm -rf generated/*

sf: generated/sf/density_map.geojson

mountain_view: generated/mountain_view/density_map.geojson

generated/sf/density_map.geojson: generated/sf/zoning_height.geojson
	ENV/bin/python ./lib/sf/map.py

generated/sf/zoning_height.geojson:
	ENV/bin/python ./lib/sf/zoning_height_map.py

generated/mountain_view/density_map.geojson:
	ENV/bin/python ./lib/mountain_view/map.py
