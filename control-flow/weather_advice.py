#promp user to input current weather conditons.
weather = input("what is the current weather condition? (sunny, rainy, cold): ")
#match weather conditons to clothing recomendations.
if weather == "sunny":
    print("wear  t-shirt and sunglasses")
elif weather == "rainy":
    print("dont forget a raincoat and an umbrella")
elif weather == "cold":
    print("make sure to wear a warm coat and a scarf")
#if weather not in ["sunny", "rainy", "cold"]:
else:
    print("I don't have recommendations for this weather.")