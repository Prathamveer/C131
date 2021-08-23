import csv
import pandas as pd

rows = []

with open("stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

df = pd.read_csv("stars.csv")
mass_list = df["solar_mass"].tolist()
radius_list = df["solar_radius"].tolist()

mass_list.pop(0)
radius_list.pop(0)

mass_si_unit = []

for data in mass_list:

    si_unit = float(data)*1.989e+30
    mass_si_unit.append(si_unit)

print(mass_si_unit)

radius_si_unit = []

for data in radius_list:
    si_unit = float(data)* 6.957e+8
    radius_si_unit.append(si_unit)

print(radius_si_unit)

star_masses = mass_si_unit
star_radiuses = radius_si_unit
star_name = df["star_names"].tolist()
star_name.pop(0)

star_gravities = []

for index,data in enumerate(star_name):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radiuses[index])*float(star_radiuses[index])*6371000*6371000) * 6.674e-11
    star_gravities.append(gravity)

print(star_gravities)