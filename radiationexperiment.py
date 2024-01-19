# Existing radiation information
locations = {
    "city_center" : [22, 19, 20, 31, 28],
    "industrial_zone": [35, 32, 30, 37, 40],
    "residential_district": [15, 12, 18, 20, 14],
    "rural_outskirts": [9, 13, 16, 14, 7],
    "downtown": [25, 18, 22, 21, 26]}

# definition to calculate average


def average(locations, area_selection):
    kv = locations[area_selection]
    area_average = sum(kv)/len(kv)
    print(f'Average of radiation levels of {area_selection} is {round(area_average, 2)}')


while True:
    opening_selection = input("\nPlease select from the following options:"
                                "\n1. Check average radiation levels of existing areas"
                                "\n2. Update radiation levels of existing areas"
                                "\n3. Add new radiation levels of South_City"
                                "\n\nPlease enter 1, 2, 3 here or -1 to exit: ")

    if opening_selection == "1":
        print("\nPlease select which area you would like to see the average radiation of:")
        for i in locations:
            print(i)

        while True:
            area_selection = input("\nPlease enter the area here (or 'end' to exit): ").lower()
            if area_selection not in locations.keys():
                print("\nPlease enter a valid area")
                continue
            else:
                average(locations, area_selection)
                break

    elif opening_selection == "2":
        for i in locations:
            print(i)

        while True:
            area_edit = input("\nPlease enter the area to enter new radiation levels for: ").lower()
            if area_edit in locations.keys():
                break
            else:
                print("\nThat is incorrect, please try again")
                continue

        while True:
            try:
                updated_radiation_levels = int(input("Enter the radiation levels or '-1' to exit: "))
                if updated_radiation_levels == -1:
                    break
                else:
                    locations[area_edit].append(updated_radiation_levels)
                    continue
            except ValueError:
                print("\nPlease enter a valid number")
                continue

        print(f"\nThe updated radiation levels for {area_edit} is now {locations[area_edit]}")
        average(locations, area_edit)

    elif opening_selection == "3":
        south_city = []

        while True:
            try:
                level = int(input("Enter radiation levels for South City or '-1' to finish: "))
                if level == -1:
                    break
                south_city.append(level)
            except ValueError:
                print("\nInvalid input. Please enter a valid number or '-1'.")

        south_city_average = sum(south_city) / len(south_city)
        print(f"\nAverage of South City is {round(south_city_average, 2)}")

    elif opening_selection == "-1":
        print("\nExiting, goodbye!")
        break

    else:
        print("\nPlease make a valid choice to proceed")
        continue
