from graph import *

connects = []
my_graph = Graph(connects, directed = False)
print my_graph

#Extracting our input info
path = "text.txt"
file = open(path, "r")
text = file.readlines()
file.close()

commands = []
for x in text:
  action = x.split("\n")[0]
  commands.append(action)

print commands
results = []
for y in commands:
  if "note" in y:
    pass
  else:
    nums = [int(y.split(" ")[-2]), int(y.split(" ")[-1])]
  print nums
  if "is linked" in y:
    print "Is linked?" , nums
    results.append(my_graph.is_linked(nums[0],nums[1]))
  elif "add" in y:
    results.append(my_graph.add(nums[0],nums[1]))
  elif "remove" in y:
    results.append(my_graph.remove(nums[0],nums[1]))

print "Graph:", my_graph
print "\nResults (1):", results[0], "\nResults(2):"
for result in results[1:]:
  if result == True or result == False:
    print result
