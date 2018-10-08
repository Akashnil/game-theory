n = 10000
step = 1./(n-1)
iterations = 100

import matplotlib.pyplot as plt

dist = [1./n] * n
values = [0.] * n

for it in range(iterations):
	value_action = []
	cumulative_dist = [0.] * n
	s = 0.
	for i in range(n):
		s += dist[i]
		cumulative_dist[i] = s - dist[i] / 2.
	for action in range(n):
		val = 0.
		val += cumulative_dist[int((action+1) / 3)]
		if action * 3 < n:
			val += cumulative_dist[action * 3]
		else:
			val += 1.
		val -= cumulative_dist[action]
		value_action.append((val, action))
	value_action.sort()
	for i in range(n):
		val, ac = value_action[i]
		dist[ac] = (2 * i + 1.) / (n * n)
		values[ac] = val

dist = [x * n for x in dist]
actions = [step * x for x in range(n)]

plt.plot(actions, values)
plt.xlabel('Choice')
plt.ylabel('Chance of winning')
plt.show()

plt.plot(actions, dist)
plt.xlabel('Choice')
plt.ylabel('Probability')
plt.show()

val, ac = value_action[n-1]

print ('Action ' + str(ac / (n-1.)) + ' has highest chance of winning = ' + str(val))