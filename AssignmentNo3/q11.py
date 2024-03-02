def main():
    # Take the names of 5 cities as input
    cities = []
    for i in range(5):
        city = input("Enter the name of a city: ")
        cities.append(city)

    # Convert each city name to uppercase
    cities_uppercase = [city.upper() for city in cities]

    # Print the uppercase city names
    print("City names in uppercase:")
    for city in cities_uppercase:
        print(city)

if __name__ == "__main__":
    main()
