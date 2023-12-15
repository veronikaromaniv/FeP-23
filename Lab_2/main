import json
from ship import Ship, ConfigShip
from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port


def get_nearest_port_with_containers(ship, ports):
    closest_port = None
    shortest_distance = float('inf')

    for port in ports.values():
        if port != ship.current_port and len(port.containers) > 0:
            distance = ship.distance_to(port)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_port = port

    return closest_port


def process_operations(ports, ships):
    for ship in ships.values():
        print(f"Ship {ship.id} starting its journey from port {ship.port.id} with {len(ship.containers)} containers onboard.")

        # loading containers from port into ship
        loaded_containers = []
        for container in list(ship.port.containers.values()):
            for cont in container:
                if ship.load(cont):
                    loaded_containers.append(cont)

        print(f"Loaded {len(loaded_containers)} containers onto ship {ship.id}.")

        # remove loaded containers from port
        for container in loaded_containers:
            if isinstance(container, BasicContainer):
                ship.port.containers["basic_container"].remove(container)
            elif isinstance(container, HeavyContainer):
                ship.port.containers["heavy_container"].remove(container)
            elif isinstance(container, RefrigeratedContainer):
                ship.port.containers["refrigerated_container"].remove(container)
            elif isinstance(container, LiquidContainer):
                ship.port.containers["liquid_container"].remove(container)

        # sail to next port if current port has no more containers or ship is full
        while sum([len(c) for c in ship.port.containers.values()]) > 0 or len(ship.containers) < ship.configs.max_number_of_all_containers:
            destination_port = get_nearest_port_with_containers(ship, ports)
            if not destination_port:
                break

            successful_sail = ship.sail_to(destination_port)
            if successful_sail:
                print(f"Ship {ship.id} sailed to port {destination_port.id}.")
                # unload containers at the destination port
                unloaded_containers = []
                for container in list(ship.containers):
                    if container.destination == destination_port:
                        ship.unload(container)
                        destination_port.add_container(container)
                        unloaded_containers.append(container)
                print(f"Unloaded {len(unloaded_containers)} containers from ship {ship.id} at port {destination_port.id}.")


def process_input(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    ports = {}
    ships = []
    containers = []

    # Creating ports
    for entry in data:
        port_id = entry["port_id"]
        latitude = entry["latitude"]
        longitude = entry["longitude"]
        ports[port_id] = Port(port_id, latitude, longitude)  # Pass port_id as the first argument

        # Creating containers for each port
        for _ in range(entry["basic"]):
            container = BasicContainer(3000)
            containers.append(container)
            ports[port_id].add_container(container)

        for _ in range(entry["heavy"]):
            container = HeavyContainer(4000)
            containers.append(container)
            ports[port_id].add_container(container)

        for _ in range(entry["refrigerated"]):
            container = RefrigeratedContainer(4000)
            containers.append(container)
            ports[port_id].add_container(container)

        for _ in range(entry["liquid"]):
            container = LiquidContainer(4000)
            containers.append(container)
            ports[port_id].add_container(container)

        # Creating ships for each port
        for ship_data in entry["ships"]:
            ship_config = ConfigShip(
                total_weight_capacity=ship_data["totalWeightCapacity"],
                max_number_of_all_containers=ship_data["maxNumberOfAllContainers"],
                maxNumberOfHeavyContainers=ship_data["maxNumberOfHeavyContainers"],
                maxNumberOfRefrigeratedContainers=ship_data["maxNumberOfRefrigeratedContainers"],
                maxNumberOfLiquidContainers=ship_data["maxNumberOfLiquidContainers"],
                fuelConsumptionPerKM=ship_data["fuelConsumptionPerKM"]
            )
            ship = Ship(ports[port_id], ship_config)
            ships.append(ship)
            ports[port_id].incoming_ship(ship)

    # Simulating the operations
    for port_id, port in ports.items():
        for ship in port.current_ships:
            # Load containers from port into ship
            for container in ship.port.containers:
                ship.load(container)

    # Generate the output
    output_data = {}

    for port_id, port in ports.items():
        port_data = {
            "lat": f"{port.latitude:.2f}",
            "lon": f"{port.longitude:.2f}",
            "basic_container": len(port.containers["basic_container"]),
            "heavy_container": len(port.containers["heavy_container"]),
            "refrigerated_container": len([container for container in port.containers["refrigerated_container"] if isinstance(container, RefrigeratedContainer)]),
            "liquid_container": len([container for container in port.containers["liquid_container"] if isinstance(container, LiquidContainer)]),
            "ships": {}
        }

        for ship in port.current_ships:
            ship_data = {
                "fuel_left": f"{ship.fuel:.2f}",
                "basic_container": len([container for container in ship.containers if isinstance(container, BasicContainer)]),
                "heavy_container": len([container for container in ship.containers if isinstance(container, HeavyContainer)]),
                "refrigerated_container": len([container for container in ship.containers if isinstance(container, RefrigeratedContainer)]),
                "liquid_container": len([container for container in ship.containers if isinstance(container, LiquidContainer)]),
            }

            port_data["ships"][f"ship_{ship.id}"] = ship_data

        output_data[f"Port_{port_id}"] = port_data

    with open("output.json", "w") as outfile:
        json.dump(output_data, outfile, indent=4)


if __name__ == "__main__":
    process_input('input.json')
