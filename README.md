To install all requirements :
-> pip install -r requirements.txt


Following feilds need to be filled.
origin  : lat, long in string format
destination : lat, long in string format
distance: In float format


After running the script step_calibrated contains the equi distant point 


LOGIC:

1. First, we chalk out all the polylines between points from the distance API.
2. Second, we keep adding the difference between the consecutive points until desired distance is reached.
3. If the distance is more than the desired we calibrate the same using haversine formula from geopy library of google.
4. We append all the required points to a list.

Output format can be changed:
Copy the output from CLI and test on -> https://www.mapcustomizer.com/#