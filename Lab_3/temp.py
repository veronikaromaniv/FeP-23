import json
from uuid import uuid4
import random

ports = []

# Create ports and collect their IDs
ports_id = [str(uuid4()) for i in range(5)]

# Ship types
ship_types = ["LightWeightShip", "MediumShip", "HeavyShip"]

# Ships
ships = []
for i in range(10):
    ship = {}
    ship_id = str(uuid4())
    port_id = random.choice(ports_id)
    ports_id_copy = ports_id.copy()
    ports_id_copy.remove(port_id)
    ports_deliver = random.choice(ports_id_copy)
    ship["ship_id"] = ship_id
    ship["port_id"] = port_id
    ship["ports_deliver"] = ports_deliver
    ship["totalWeightCapacity"] = 1000
    ship["maxNumberOfAllContainers"] = random.randint(1, 20)
    ship["maxNumberOfHeavyContainers"] = random.randint(1, 5)
    ship["maxNumberOfRefrigeratedContainers"] = random.randint(1, 2)
    ship["maxNumberOfLiquidContainers"] = random.randint(1, 5)
    ship["fuelConsumptionPerKM"] = random.uniform(10, 30)
    ship["ship_type"] = random.choice(ship_types)  # Random ship type
    ships.append(ship)

# Ports
for i in range(5):
    port = {}
    port["port_id"] = ports_id[i]
    port["latitude"] = random.uniform(-90, 90)
    port["longitude"] = random.uniform(-180, 180)
    port["ships"] = [ship for ship in ships if ship["port_id"] == port["port_id"]]
    port["basic"] = random.randint(1, 10)
    port["heavy"] = random.randint(1, 8)
    port["refrigerated"] = random.randint(1, 5)
    port["liquid"] = random.randint(1, 5)
    ports.append(port)

json_object = json.dumps(ports, indent=2)

# Writing to input.json
with open("input.json", "w") as outfile:
    outfile.write(json_object)
