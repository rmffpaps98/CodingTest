n = int(input())
roads = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = roads[0] * oil[0]
m_cost = oil[0]

for i in range(1, n-1) :
    if m_cost > oil[i] :
        m_cost = oil[i]

    cost += m_cost * roads[i]

print(cost)