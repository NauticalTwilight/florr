import json
import csv

# Function to parse internal data and make N/A values None (null in JSON)
def parseRow(rowIndex):
    if (rowIndex == "N/A") or (rowIndex == ""):
        return None
    else:
        return rowIndex

# Function to parse the drop table for each mob
def parseDropChances(row, index):
    petalDropDictionary = {}  # Empty dictionary for the drop chances
    # Common drops
    if row[index + 1] != "":
        petalDropDictionary["common"] = row[index + 1] + "%"
    # Unusual drops
    if row[index + 2] != "":
        petalDropDictionary["unusual"] = row[index + 2] + "%"
    # Rare drops
    if row[index + 3] != "":
        petalDropDictionary["rare"] = row[index + 3] + "%"
    # Epic drops
    if row[index + 4] != "":
        petalDropDictionary["epic"] = row[index + 4] + "%"
    # Legendary drops
    if row[index + 5] != "":
        petalDropDictionary["legendary"] = row[index + 5] + "%"
    # Mythic drops
    if row[index + 6] != "":
        petalDropDictionary["mythic"] = row[index + 6] + "%"
    # Ultra drops
    if row[index + 7] != "":
        petalDropDictionary["ultra"] = row[index + 7] + "%"
    return petalDropDictionary

# Function to write the dictionary to a JSON file
def saveJSON(dictionaryData):
    with open(f"./stats/{dictionaryData['name'].lower()}.json", "w") as jsonFile:
        json.dump(dictionaryData, jsonFile, indent=4)

# Open the datasheet first and make a list copy of its contents
dictionaryData = {"name": "[INITIALIZE]"}
specialStats = None
dropItems = None
with open ("./datasheet.csv", "r") as csvInput:
    data = list(csv.reader(csvInput))

# Iterate continuously for each mob
data = data[2:]  # Discard the first two rows (just column/header information)
for row in data:
    if row[0] != "":  # Empty string indicates the start of a new mob series
        print(f"INFO: Dumping data for mob: {dictionaryData['name']} ---> Special Stats: {specialStats} ---> Drops: {dropItems}")
        saveJSON(dictionaryData)
        dictionaryData = {}  # Reset the dictionary for each new mob
        dictionaryData["name"] = parseRow(row[0]).title()
        dictionaryData["description"] = "FILL"
        # Grab health status (if it is a range or a static number)
        if row[6] != "N/A":  # The mob has a range of health values
            healthRange = True
        else:  # Static health value
            healthRange = False
        # Grab super spawn message (which only appears in the first row)
        if row[4] != "N/A":  # A custom super spawn message exists
            dictionaryData["super_spawn_message"] = row[4]
        else:  # Default super spawn message
            dictionaryData["super_spawn_message"] = f"A Super {dictionaryData['name']} has spawned somewhere!"
        # Grab special stats (which only appear in the first row for that mob)
        if row[8] != "N/A":  # One or more special stats exist
            specialStats = row[8].split("; ")
        else:
            specialStats = None
        # Grab drops (which only appear in the first row for that mob)
        if row[20] != "N/A":
            dropItems = row[20].split("\n")
        else:
            dropItems = None
    # Iterating through stats for each rarity
    dictionaryData[row[1].lower()] = dict()  # Empty dictionary for each rarity
    # Basic stats for each mob
    if healthRange:  # The mob has a range of health values
        dictionaryData[row[1].lower()]["health"] = f"{parseRow(row[5])}~{parseRow(row[6])}"
    else:  # Static health value
        dictionaryData[row[1].lower()]["health"] = parseRow(row[5])
    dictionaryData[row[1].lower()]["body_damage"] = parseRow(row[7])
    # Special stats for each mob, if they exist
    if specialStats is not None:
        dictionaryData[row[1].lower()]["special_stats"] = dict()  # Empty dictionary for the special stats
        specialStatIndex = 9
        for specialStat in specialStats:
            dictionaryData[row[1].lower()]["special_stats"]["_".join(specialStat.lower().split(" "))] = parseRow(row[specialStatIndex])  # Convert the special stat name to snake case
            specialStatIndex += 1
    # Parse drop chances
    if dropItems is not None:  # The mob has drops
        dictionaryData[row[1].lower()]["drops"] = {}
        dropIndex = 22
        for dropItem in dropItems:
            dictionaryData[row[1].lower()]["drops"][dropItem.lower()] = parseDropChances(row, dropIndex)
            dropIndex = dropIndex + 9
    else:
        dictionaryData[row[1].lower()]["drops"] = None