import pulp

model = pulp.LpProblem('Maximize Production', pulp.LpMaximize)
L = pulp.LpVariable('L', lowBound=0, cat='Integer')
J = pulp.LpVariable('J', lowBound=0, cat='Integer')

#Цільова функція
model += L + J

# Обмеження
model += 2*L + 1*J <= 100 #Вода
model += 1*L <= 50 #Цукор
model += 1*L <=30 # Лимонний сік
model += 2*J <= 40 # Пюре

model.solve()

print('Оптимальна кількість Лимонаду: ', L.varValue)
print('Оптимальна кількість Фруктового соку: ', J.varValue)