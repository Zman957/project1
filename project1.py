from operator import truediv

list1 = []
list2 = []

while True :
    first = input("Enter two decimals values separated by a space (or type -1.0 to stop.):")
    if first.strip() == "-1.0":
        break

    try:
        wind, rain = map(float, first.split())
        list1.append(wind)
        list2.append(rain)
    except ValueError:
        print("Invalid number.")

average1 = sum(list1) / len(list1)
print("The average rain is:", average1)

average2 = sum(list2) / len(list2)
print("The average wind is:", average2)

weathersev = (average1 * 10) + average2
print ("The weather severity for these", len(list1), "readings is:", weathersev)
