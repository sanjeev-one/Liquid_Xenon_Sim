# Open a new file in write mode
with open("input.txt", "w") as f:
    # Write your initial setup to the file
    f.write(
        "detector Det radius=100 length=15.8 material=lXe color=1,0,0 format=ASCII\n"
    )
    f.write("place Det z=1000\n")

    # Start the placement at 1000
    z = 1000

    # While the z coordinate is less than the desired total length
    while z < 1158:
        # Increase z by the length of the detector
        z += 15.8
        # Write the place command to the file
        f.write("place Det z={} rename=Det#\n".format(z))
