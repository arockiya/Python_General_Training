Cities = ["Chennai", "Madurai", "Thiruppathur", "Karaikudi"]
print(Cities[2])
print(Cities[-1])
print(Cities[1:])
print(Cities[1:3]) #from 1 before 3

States = ["Tamilnadu","Kerala","Karnataka","Andra"]

Cities.extend(States)
Cities.append("Koratti")
Cities.insert(4,"New Insert")
Cities.remove("New Insert")
print(Cities)

States.clear()
print(States)
# pop- Removes the last element in the list
Cities.pop()
print(Cities) #removed Koratti

print(Cities.index("Thiruppathur")+1)

Cities.append("Chennai")
print(Cities.count("Chennai"))

Cities.sort()
print(Cities)

Cities.reverse()
print(Cities)

new_cities=Cities.copy()
print(new_cities)