import math

# Desired total outer radius
R_total = 50.0

# Volume for each ring
V = 5000.0  # Change this to your desired volume

# Initial inner radius
R_inner = 0.0

# Length of the cylinder
h = 158.0

i = 1
while True:
    # Calculate outer radius for the same volume
    R_outer = math.sqrt(R_inner**2 + V / (math.pi * h))

    # Break the loop if the outer radius is beyond the total radius
    if R_outer > R_total:
        break

    print(
        f"detector Det innerRadius={R_inner:.1f} outerRadius={R_outer:.1f} length={h} material=lXe color=1,0,0 format=ASCII"
    )
    print(f"place Det z=1000 rename=Det#")

    R_inner = R_outer  # update inner radius for next ring
    i += 1
