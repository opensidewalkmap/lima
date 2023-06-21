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

# City OSM relation id: (search at  https://nominatim.openstreetmap.org/ui/search.html ):
CITY_RELATION_ID = 'R1944670' #as string!!

# BOUNDING BOXES
# A good tool to find them is: bboxfinder.com
# # entire city: 
BOUNDING_BOX = (-12.239701,-77.123852,-12.026897,-76.877518)
# SOUTHMOST  LATITUDE, # WESTMOST   LONGITUDE, # NORTHMOST  LATITUDE, # EASTMOST   LONGITUDE)

# # A sample of a region of special interest, like the city centre, 
# # It must have sidewalks as geometries and be inside the bigger one!!
BOUNDING_BOX_SAMPLE = (-12.086676,-77.087942,-12.081598,-77.081210) 
# SOUTHMOST  LATITUDE, # WESTMOST   LONGITUDE, # NORTHMOST  LATITUDE, # EASTMOST   LONGITUDE)

STREAMLIT_URL='https://kauevestena-opensidewalkmap-beta-streamlit-routing-app-52bins.streamlitapp.com/'
