import csv
import math
with open("data.csv", newline='') as f:
    readData = csv.reader(f)
    listOfData = list(readData)

data = listOfData[0]

# Calculating the mean 'u'
def mean(data):
    lengthOfData = len(data)
    total = 0
    for i in data:
        total = total + int(i)
    mean = total/lengthOfData
    return mean

listOfDifferences = []
for i in data:
    # Subtracting the mean from individual values from the mean of the data
    difference = int(i) - mean(data)
    # Squaring those values
    difference = difference*difference
    # Storing those values in a list
    listOfDifferences.append(difference)

sumOfDifferences = 0
for i in listOfDifferences:
    # Adding all the differences between the individual values and mean of the data
    sumOfDifferences += i

# Dividing the sum of differences by the length of the data.
resultUnderTheRoot = sumOfDifferences/len(data)
# Taking the square root of the result. Hence, the standard deviation is found.
standard_deviation = math.sqrt(resultUnderTheRoot)
print(standard_deviation)
