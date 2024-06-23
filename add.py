# Step 2: Read temperature with unit from the user
temp = input("temp with unit: ")

# Step 3: Extract the unit
unit = temp[-1]

# Step 4: Define valid units
valid_units = ['F', 'C', 'f', 'c']

# Step 4: Check if unit is valid
if unit not in valid_units:
    print("unrecognized unit:", unit)
    exit

# Extract the temperature part
t = float(temp[:-1])

# Step 4: Convert temperature based on unit
if unit in ['F', 'f']:
    c = (5 / 9) * (t - 32)
    print("{:.2g} {} = {:.2g} C".format(t, unit, round(c, 2)))
else:
    f = (9 / 5) * t + 32
    print("{:.2g} {} = {:.2g} F".format(t, unit, round(f, 2)))
