import re

with open("input.txt", "r") as f:
# with open("example.txt", "r") as f:
    data = f.read()

x = re.search(
    r"seeds: (.*?)\n\nseed-to-soil map:\n([\s\S]*.*)\nsoil-to-fertilizer map:\n([\s\S]*.*)\nfertilizer-to-water map:\n([\s\S]*.*)\nwater-to-light map:\n([\s\S]*.*)\nlight-to-temperature map:\n([\s\S]*.*)\ntemperature-to-humidity map:\n([\s\S]*.*)\nhumidity-to-location map:\n([\s\S]*.*)",
    data,
)

def splitter(s: str) -> list:
    return list(map(lambda x: list(map(int, x.split(" "))), list(filter(None, s.split("\n")))))

def destinationfrommap(map: list, source: int):
    # mapping[0] = destination
    # mapping[1] = source
    # mapping[2] = rangelength
    for mapping in map:
        if source >= mapping[1] and source <= mapping[1] + mapping[2]:
            # print(f"wow found for {source} so {mapping}")
            return mapping[0] + abs(source - mapping[1])
        
    # print("returning default")
    return source

seeds = list(map(int, x.group(1).strip().split(" ")))
seedtosoil = splitter(x.group(2))
soiltofertilizer = splitter(x.group(3))
fertilizertowater = splitter(x.group(4))
watertolight = splitter(x.group(5))
lighttotemperature = splitter(x.group(6))
temperaturetohumidity = splitter(x.group(7))
humiditytolocation = splitter(x.group(8))

locations = []
for seed in seeds:
    location = destinationfrommap(
        humiditytolocation,
        destinationfrommap(
            temperaturetohumidity,
            destinationfrommap(
                lighttotemperature,
                destinationfrommap(
                    watertolight,
                    destinationfrommap(
                        fertilizertowater,
                        destinationfrommap(
                            soiltofertilizer,
                            destinationfrommap(seedtosoil, seed)
                        )
                    )
                )
            )
        )
    )

    locations.append(location)

print(f"Answer 1: {min(locations)}")

newlocations = []
newseedspaired = list(zip(seeds[::2], seeds[1::2]))
for newseedpair in newseedspaired:
    print(f"Running seed pair {newseedpair}")
    for i in range(newseedpair[0], newseedpair[0] + newseedpair[1]):
        newlocation = destinationfrommap(
            humiditytolocation,
            destinationfrommap(
                temperaturetohumidity,
                destinationfrommap(
                    lighttotemperature,
                    destinationfrommap(
                        watertolight,
                        destinationfrommap(
                            fertilizertowater,
                            destinationfrommap(
                                soiltofertilizer,
                                destinationfrommap(seedtosoil, i)
                            )
                        )
                    )
                )
            )
        )
        newlocations.append(newlocation)

print(f"Answer 2: {min(newlocations)}")

# print(f'Answer 2: {sum(list(map(lambda x: x["how_many_of"], records)))}')
