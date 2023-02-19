print("A statement that prints 'Hello world!'" + "\n")

print("Hello world!\n")



print("A list populated with several values, then print one of those values:" + "\n")

favorite_foods = ["bread pudding", "snickers", "sumo mandarin", "smarties", "hot fudge sauce"]
print(favorite_foods[0] + "\n")

print("A dictionary populated with two keys and two values, then print one of the values:" + "\n")

california_county_population = {
    "Los Angeles" : 10019635,
    "Alameda" : 1673133,
    "Sacramento" : 1571767,
    "San Joaquin" : 771406,
    "Marin" : 262387
}
county = "San Joaquin"
print(county + ": " + format(california_county_population[county]) + "\n")

print("A tuple with four values, then print one of them:" + "\n")

all_the_things = (
    "Hello world!\n",
    ["bread pudding", "snickers", "sumo mandarin", "smarties", "hot fudge sauce"],
    {
        "Los Angeles" : 10019635,
        "Alameda" : 1673133,
        "Sacramento" : 1571767,
        "San Joaquin" : 771406,
        "Marin" : 262387
    },
    "Hello, world! I like to eat bread pudding in San Joaquin!"
)
print(all_the_things[-1])