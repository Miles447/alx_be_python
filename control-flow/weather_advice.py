#prompt user to input current weather conditions.
weather = input("what's the weather like today? (sunny/rainy/cold): ")
#match weather conditions to clothing recommendations.
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget a raincoat and an umbrella.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
#if weather not in ["sunny", "rainy", "cold"]:
else:
    print("I don't have recommendations for this weather.")