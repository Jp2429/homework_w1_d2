total=0
united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1].update({'capital':'Cardiff'})
print(united_kingdom[1])

#Another way
#united_kingdom[1]['name']='Cardiff'

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
northern_ireland={
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
  }
united_kingdom.append(northern_ireland)
print(united_kingdom[3])

# 3. Use a loop to print the names of all the countries in the UK.
i=0
while i<4:
    print(united_kingdom[i].get('name'))
    i=i+1

#Another way to do it
#for country in united_kingdom:
    #print(country['name'])

# 4. Use a loop to find the total population of the UK.
j=0
while j<4:
    current=united_kingdom[j].get('population')
    total=total+current
    
    j=j+1
print(total)

#Another way to do it
# total=0
# for country in united_kingdom:
#     current_pop= country['population']
#     total+=current_pop

# print(total)