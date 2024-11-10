"""Examples of dictionary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110  # Example of modifying value in dictionary

print("Americone Dream" in ice_cream)  # tests if key is in dictionary

ice_cream["pbj"] = 1  # mutates dictionary by adding key pbj and
# value = 1

ice_cream["pbj"]  # finds value of key pbj

# the len of a dictionary is the number of key values

pbj_orders: int = ice_cream["pbj"]
print(pbj_orders)

ice_cream.pop("strawberry")  # removes strawberry

for flavor in ice_cream:
    count: int = ice_cream[flavor]
    print(f"{flavor}: {count}")
