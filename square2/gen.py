with open("g4beamline_input.txt", "w") as file:
    for x in range(14):
        for y in range(14):
            for z in range(20):
                file.write(
                    f"place Det x={x*5} y={y*5} z={z*5 + 1000} rename=Det{x}_{y}_{z}\n"
                )
