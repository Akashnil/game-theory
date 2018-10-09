import math

n = 1000
step = 1./(n-1)
iterations = 1000

import matplotlib.pyplot as plt

dist = [1./n] * n
values = [0.] * n

actions = [step * x for x in range(n)]

for it in range(iterations):
	value_action = []
	cumulative_dist = [0.] * n
	s = 0.
	for i in range(n):
		s += dist[i]
		cumulative_dist[i] = s - dist[i] / 2.
	for action in range(n):
		val = 0.
		x = cumulative_dist[int(action / 3)]
		y = cumulative_dist[int(action / 3) + 1]
		u = action % 3
		val += x + (y-x) * u / 3.
		if action * 3 < n-1:
			val += cumulative_dist[action * 3]
		else:
			val += 1.
		val -= cumulative_dist[action]
		value_action.append((val, action))
	value_action.sort()
	for i in range(n):
		val, ac = value_action[i]
		factor = it
		dist[ac] = (dist[ac] * factor + (2 * i + 1.) / (n * n)) / (factor+1)
		values[ac] = val
		'''
	if (it & (it - 1)) == 0:
		dist_scaled = [x * n for x in dist]

		plt.plot(actions, dist_scaled)
		plt.xlabel('Choice')
		plt.ylabel('Probability')
		plt.show()
		'''


plt.plot(actions, values)
plt.xlabel('Choice')
plt.ylabel('Chance of winning')
plt.show()

dist_scaled = [x * n for x in dist]

plt.plot(actions, dist_scaled)
plt.xlabel('Choice')
plt.ylabel('Probability')
plt.show()

val, ac = value_action[n-1]

print ('Action ' + str(ac / (n-1.)) + ' has highest chance of winning = ' + str(val))