pets: list[str] = ["Louie", "Bo", "Bear"]
for p in pets:
    print(f"Good boy, {p}!")

names: list[str] = ["Alyssa", "Janet", "Victoria"]
# print each index: name
for idx in range(0, len(names)):
    print(str(idx) + ": " + names[idx])
