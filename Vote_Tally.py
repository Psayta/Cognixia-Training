#This program tallies votes from votes.csv and returns the national winner and regional winners 
import csv

csvdata = "votes.csv" #assigns the csv file 

headers = [] #empty list to display headers
candidates = ["A","B","C","D","E","F"] #categorizes the letters for each candidate in a dictionary
national = dict.fromkeys(candidates, 0) #initialize each candidates value to 0 
north = dict.fromkeys(candidates, 0)
south = dict.fromkeys(candidates, 0)
east = dict.fromkeys(candidates, 0)
west = dict.fromkeys(candidates, 0)
central = dict.fromkeys(candidates, 0)

with open(csvdata, "rt") as csvfile: #reads vote file 
    data = csv.reader(csvfile) #assigns the votefile to data
    headers = next(data) #reads horizontal data of the headers
    for row in data: #loops the over the data as row
        national[row[3]] += 1 #uses national choice and counts for each candidate 

        if row[1] == "NORTH": north[row[2]] += 1 #adds rows for each candidate based on both indexes
        elif row[1] == "SOUTH": south[row[2]] += 1
        elif row[1] == "EAST": east[row[2]] += 1
        elif row[1] == "WEST": west[row[2]] += 1
        elif row[1] == "CENTRAL": central[row[2]] += 1

national_winner = max(national, key=national.get) # find max value in a dictionary
north_winner = max(north, key=north.get)
south_winner = max(south, key=south.get)
east_winner = max(east, key=east.get)
west_winner = max(west, key=west.get)
central_winner = max(central, key=central.get)

print(headers)
print("NATIONAL", national, "Winner is ",national_winner) 
print("NORTH", north, "Winner is ",north_winner)
print("SOUTH", south, "Winner is ",south_winner)
print("EAST", east, "Winner is ",east_winner)
print("WEST", west, "Winner is ",west_winner)
print("CENTRAL", central, "Winner is ",central_winner)
