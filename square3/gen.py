with open("g4beamline_input.txt", "w") as file:
    for x in range(70):
        for y in range(70):
            for z in range(100):
                file.write(
                    f"place Det x={x*1} y={y*1} z={z*1 + 1000} rename=Det{x}_{y}_{z}\n"
                )
