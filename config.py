"""
  setup the variables for your city:

  all of them are mandatory!!
"""

# Full city name, it may contain special characters, spaces...
CITY_NAME = 'Lima'

# simple name, spaces must be replaced by underscores, no special characters, all in lowercase
CITY_SHORTNAME = 'lima'

# username, for addresses
USERNAME = 'opensidewalkmap'

# repository name, for many weblink references:
REPO_NAME = 'lima'

# BOUNDING BOXES
# A good tool to find them is: bboxfinder.com
# # entire city: 
BOUNDING_BOX = (
    -12.236681, # SOUTHERNMOST LATITUDE
    -77.937012, # WESTERNMOST  LONGITUDE
    -11.980218, # NORTHERNMOST LATITUDE
    -77.937012  # EASTERNMOST  LONGITUDE
    )

# Set a midpoint for the map AND A Z LEVEL FOR THE INITIAL ZOOM:
MID_LAT = -12.066559
MID_LGT = -77.090313
INITIAL_Z_LEVEL = 19

# MIN AND MAX ZOOM LEVELS FOR TILE GENERATION:
# (since there's the 100MB file size limit, for big datasets might be better to stay at 19 or even 18)
TILES_MIN_ZOOM = 9
TILES_MAX_ZOOM = 20


### MORE DELICATE ONES: (leave them unchanged by default)

# TAGS FOR ADDITIONAL FOOTWAYS
# you can check the reason behind those default ones at: https://kauevestena.github.io/opensidewalkmap/information/other_footways.html

# Values must all be set as a list, even if there's a single value!!

# depending on local rules, the other types of footways can differ, so you migh tune the options
OTHER_FOOTWAY_RULES = {'highway':['footway','steps','living_street','pedestrian','track','path'],'foot':['yes','designated','permissive','destination'],'footway': ['alley','path','yes']}

# since we download all features containing the tags of the previous rule-set, if there's another tag hierarchically above, we should exclude those features:
OTHER_FOOTWAY_EXCLUSION_RULES = {'highway': ['trunk','motorway','primary','secondary','trunk_link','motorway_link','primary_link'],'access':['no','private'],'foot':['no','use_sidepath','private']}
