graph = {}
# Reading the graph.txt file line by line
with open('graph.txt', 'r') as file:
    for line in file:
        line = line.split(', ')             # Spliting inputs
        line1 = line[1].split('\n')         # Spliting inputs

        # Creating list of connections in graph
        if line[0] in graph:
            temp = graph[line[0]]
            temp = temp+","+line1[0]
            graph[line[0]] = temp
        else:
            graph[line[0]] = line1[0]