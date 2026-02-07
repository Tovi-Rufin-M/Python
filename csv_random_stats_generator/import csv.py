import pandas as pd
import random

# 1. Your Lists
food_items = [
    "Bagel", "Lobster Bisque", "Caesar Salad", "T-Bone Steak", 
    "Blueberry Muffin", "Dim Sum", "Gelato", "Chicken Curry", 
    "Kimchi", "Pancakes", "Falafel", "Glazed Donut"
]

tools = [
    "Phillips Screwdriver", "Crowbar", "Spirit Level", "Chainsaw", 
    "Wire Strippers", "Sander", "Hot Glue Gun", "Ratchet Set", 
    "Utility Knife", "Wheelbarrow", "Jigsaw", "Flashlight"
]

# 2. Select two unique random names for headers
all_items = food_items + tools
header1, header2 = random.sample(all_items, 2)

# 3. Generate Data
# Column 1: 11 random numbers
col1_data = [random.randint(1, 50) for _ in range(11)]

# Column 2: 10 random numbers + 1 None/Empty value to match length
col2_data = [random.randint(1, 50) for _ in range(10)]
col2_data.append(None)  # Add empty value at the end so both columns have 11 rows

# 4. Create DataFrame
df = pd.DataFrame({
    header1: col1_data,
    header2: col2_data
})

file_name = f'{header1}_&_{header2}.csv'
# 5. Save to CSV
# index=False prevents pandas from adding 0,1,2... as a row label
df.to_csv(file_name, index=False)

print(f"File '{file_name}' created successfully with headers: {header1} and {header2}")
print(df) # Prints a preview to the console