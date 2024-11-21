def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    # Calculate the average result for each contestant
    def calculate_average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    # Store the persons and their averages in a list
    persons = [person1, person2, person3]
    averages = [(person, calculate_average(person)) for person in persons]

    # Find the person with the smallest average
    smallest_person = min(averages, key=lambda x: x[1])[0]

    # Return the dictionary of the contestant with the smallest average
    return smallest_person

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
