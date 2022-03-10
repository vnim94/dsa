def largestComponent(graph):
    largest = 0
    visited = {}

    for node in graph:
        count = 0

        if node not in visited:
            nodes = []
            nodes.append(node)

            while len(nodes) > 0:
                n = nodes.pop(0)
                for link in graph[n]:
                    if link not in visited:
                        visited[link] = 1
                        nodes.append(link)
                        count += 1

            if largest == None or count > largest:
                largest = count

    return largest

print(largestComponent({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # 4

print(largestComponent({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6

print(largestComponent({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # -> 5

print(largestComponent({})) # -> 0

print(largestComponent({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
})) # -> 3