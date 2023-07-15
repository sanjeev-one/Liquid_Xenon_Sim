with open("g4beamline_input.txt", "w") as file:
    for x in range(11):
        for y in range(11):
            for z in range(21):
                file.write(
                    f"place Det x={x*10} y={y*10} z={z*10 + 1000} rename=Det{x}_{y}_{z}\n"
                )
