import json, re, os, pprint

def getUntil(wd, time, roomTimetables, room):
    for i in range(time, 32): # 32=12pm
        if (roomTimetables[wd][room][i] == 1):
            break
    return i

# run scrapy crawl timeslot before using this

# preparation: read the files
weekdays = []
for i in range(0, 7):
    with open('./timeslots/'+str(i)+'.json') as f:
        weekdays.append(json.loads(f.read().decode('utf-8')))

# step 1: O(n^2) (counting the set.union() too) scan to get a set of rooms

rooms = [set(),set(),set(),set(),set(),set(),set()]

for i in range(len(weekdays)):
    wd = weekdays[i]
    for timeslot in wd: # O(n)
        rooms[i].add(timeslot['room']) # O(n) (set function)

# step 2: O(n) scan to create 7*n timetable templates, n donates the sum of # of rooms for every week day

roomTimetables = [{},{},{},{},{},{},{}]

for i in range(0, 7):
    for room in rooms[i]:
        roomTimetables[i][room] = [0] * 32 # 0=8am, 7pm=23, 12pm=32

# step 3: O(n^2) scan to calculate the timetable for each room, every day
for i in range(0, 7):
    for timeslot in weekdays[i]:
        for t in range(timeslot['start'], timeslot['end']):
            roomTimetables[i][timeslot['room']][t] = 1

# step 4: O(n^2) scan to see for each timeslot what room is available
# take the fucking transpose (any better way?)

## database (length=7)
## database[*] (length=32, timeslots)
## database[*][*] (length=N, N denotes the number of empty rooms at this time)

database = []

for i in range(0, 7):
    database.append([])
    for t in range(0, 32):
        database[i].append([])
        for room in roomTimetables[i]:
            # initialize the database
            if (roomTimetables[i][room][t] == 0):
                database[i][t].append({'room': room, 'until': getUntil(i, t, roomTimetables, room)})

f = open('database.json', 'w+')
f.write(json.dumps(database))
f.close()
