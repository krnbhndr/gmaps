import requests
import googlemaps as gm
from geopy import Point
from geopy.distance import distance, geodesic
import polyline
from geographiclib.geodesic import Geodesic


def get_bearing(lat1, lat2, long1, long2):  # for getting bearing
    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
    return brng


# input data
origin = "12.927923,77.627106"
destination = "12.990230,77.714340"
distance = 0.5  # for calculating points


api_key = "AIzaSyAEQvKUVouPDENLkQlCF6AAap1Ze-6zMos"  # key

url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + \
    origin+"&destination="+destination+"&key=" + api_key

payload = {}
headers = {}
try:
    response = requests.request("GET", url, headers=headers, data=payload)
except:
    print("API not accessable . Exiting in 0 sec")
    exit()
finally:
    if(response.status_code != 200):
        print("API output not desired . Exiting in 0 sec")
        exit()


step_data = response.json()["routes"][0]["legs"][0]["steps"]
polylines = []
if(response.status_code == 200 and response.json()['status'] == "OK"):
    for d in step_data:
        polylines.append(polyline.decode(d["polyline"]["points"]))
        pass


prev_step = polylines[0][0]
temp_dis = 0.0
prev_dis = 0.0
step_calibrated = []


for pos in polylines:
    for p in pos:
        prev_dis = temp_dis
        temp_dis += geodesic(prev_step, p).km

        if(temp_dis < distance):
            prev_step= p
            continue
        else:
            distMiles = distance -prev_dis

            bearing = get_bearing(prev_step[0], prev_step[1], p[0], p[1])
            prev_step= geodesic(miles=distMiles).destination(
                Point(prev_step[0], prev_step[1]), bearing)
            temp_dis = geodesic(prev_step, p).km
            step_calibrated.append(prev_step)
            prev_step= p

for j in step_calibrated:
    print(j[0], j[1])
