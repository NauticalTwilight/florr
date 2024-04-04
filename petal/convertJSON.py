import json
import csv

# Function to parse internal data and make N/A values None (null in JSON)
def parseRow(rowIndex):
    if rowIndex == "N/A":
        return None
    else:
        return rowIndex

# Function to parse internal data specifically for the count value
def parseCount(rowIndex):
    if rowIndex == "N/A":
        return "0"
    else:
        return rowIndex

# Function to write the dictionary to a JSON file
def saveJSON(dictionaryData):
    with open(f"./stats/{dictionaryData['name'].lower()}.json", "w") as jsonFile:
        json.dump(dictionaryData, jsonFile, indent=4)

# Open the datasheet first and make a list copy of its contents
dictionaryData = {"name": "[INITIALIZE]"}
specialStats = None
with open ("./datasheet.csv", "r") as csvInput:
    data = list(csv.reader(csvInput))

# Iterate continuously for each petal
data = data[1:]  # Discard the first row (just information about data)
for row in data:
    if row[0] != "":  # Empty string indicates the start of a new petal series
        print(f"INFO: Dumping data for petal: {dictionaryData['name']} ---> Special Stats: {specialStats}")
        saveJSON(dictionaryData)
        dictionaryData = {}  # Reset the dictionary for each new petal
        dictionaryData["name"] = parseRow(row[0]).title()
        dictionaryData["description"] = "FILL"
        # Grab special stats (which only appear in the first row for that petal)
        if row[9] != "N/A":  # One or more special stats exist
            specialStats = row[9].split("; ")
        else:
            specialStats = None
    # Iterating through stats for each rarity
    dictionaryData[row[1].lower()] = dict()  # Empty dictionary for each rarity
    # Basic stats for each petal
    dictionaryData[row[1].lower()]["damage"] = parseRow(row[4])
    dictionaryData[row[1].lower()]["health"] = parseRow(row[5])
    dictionaryData[row[1].lower()]["petal_reload"] = parseRow(row[6])
    dictionaryData[row[1].lower()]["usage_reload"] = parseRow(row[7])
    dictionaryData[row[1].lower()]["count"] = parseCount(row[3])
    # Special stats for each petal, if they exist
    if specialStats is not None:
        dictionaryData[row[1].lower()]["special_stats"] = dict()  # Empty dictionary for the special stats
        specialStatIndex = 10
        for specialStat in specialStats:
            dictionaryData[row[1].lower()]["special_stats"]["_".join(specialStat.lower().split(" "))] = parseRow(row[specialStatIndex])  # Convert the special stat name to snake case
            specialStatIndex += 1
