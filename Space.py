import requests
from datetime import datetime, timedelta

url = "http://api.open-notify.org/astros.json"
req = requests.get(url)
print(req)

data = req.json()


Info = data.get("people")
first_group = Info[0]

first_craft = first_group.get("craft")
first_name = first_group.get("name")

second_group = Info[1]
second_craft = second_group.get("craft")
second_name = second_group.get("name")

third_group = Info[2]
third_craft = third_group.get("craft")
third_name = third_group.get("name")

number_of_people = len(Info)
print("There is: " + str(number_of_people) + " people on the space")
Austraunat_name = Info[0].get("name") , Info[1].get("name") , Info[2].get("name")
Craft = Info[0].get("craft") , Info[1].get("craft") , Info[2].get("craft")

for i in Austraunat_name:
        print("Austraunat name: ", i)


if first_craft == second_craft and first_craft == third_craft and second_craft == third_craft:
        print(first_name +" ,"+ second_name +" and "+ third_name + " are all in the same craft: " + first_craft)
else:
      pass


lat: 42.083302
LON = -71.019897
url ="http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON"
adv_req = requests.get(url)
print(adv_req)

data = adv_req.json()
print(data)

#lat = float(input("The latitude of the place to predict passes: "))
#lon = float(input("The longitude of the place to predict passes: "))

reason = data.get("reason")
#reason = lat,lon
data["LAT"] = lat

print(data)
