with open("g4beamline_input.txt", "w") as file:
    for x in range(35):
        for y in range(35):
            for z in range(50):
                file.write(
                    f"place Det x={x*2} y={y*2} z={z*2 + 1000} rename=Det{x}_{y}_{z}\n"
                )
