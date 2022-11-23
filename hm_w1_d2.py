stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
#1
stops.append("Edinburgh Waverly")
print(stops)
#2
stops.insert(0,"Glasgow Queen St")
print(stops)
#3
stops.insert(4,"Polmont")
print(stops)
#4
int=stops.index("Linlithgow")
print(int)
#5
stops.remove("Livingston")
print(stops)
#6
stops.pop(2)
print(stops)
#7
print(len(stops))
#8
stops.sort()
print(stops)
#9
stops.reverse()
print(stops)
#10
for i in stops:
    print(i)