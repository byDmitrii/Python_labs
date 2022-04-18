import networkx as nx
import algorithmx
import json


G = nx.DiGraph()


with open('graph.json', 'r') as file:
    data = json.load(file)
    for row in data:
        G.add_weighted_edges_from([(row[0], row[1], row[2])])



canvas = algorithmx.create_canvas()
canvas.size((900,500))
canvas.edgelength(120)

canvas.nodes(range(len(G.nodes))).add()
canvas.edges(G.edges).add().directed(True).label().text(lambda e: G.edges[e]['weight'])



# начальная вершина
source = 0



# расстояние от исходной вершины до остальных вершин считаются как бесконечные
edges = list(G.edges(data=True))
# массив вершин со всеми значениями равными бесконечности, кроме изначальной
dist = [0 if node == source else float("INF") for index, node in enumerate(G.nodes)]
pred = [None for node in enumerate(G.nodes)]


for i in range(len(G.nodes) - 1):
    updated = False

    for index, edge in enumerate(G.edges):
        # задаём значение для двух вершин и веса ребра
        u = edges[index][0]
        v = edges[index][1]
        weight = edges[index][2]['weight']

        # если расстояние первой вершины задано как бесконечность
        # и сумма её с весом ребра меньше, значения второй вершины
        # обновляем значение верщины и отмечаем её как пройденную
        if dist[u] is not float("INF") and dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            pred[v] = u
            is_updated = True

    if not updated:
        break

# проверка на убываюший цикл
for index, edge in enumerate(G.edges):
    u = edges[index][0]
    v = edges[index][1]
    weight = edges[index][2]['weight']

    if dist[u] is not float("INF") and dist[u] + weight < dist[v]:
        raise Exception("Внимание! Цикл отрицательного веса!")

#print(f"Все пройденные расстояние: {dist}")

print(f"Минимальное расстояние равно: {dist[-1]}")