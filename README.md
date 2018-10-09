# game-theory
A game about choosing numbers

Each player recieve 2 random real number from 0 to 1 (with uniform distribution) secretly. Then both simultaneously choose a number from the two choice he get.

After revealing both numbers, the bigger one wins if it's more than 3 times bigger than the smaller one. (Draw if both player choose the same number. But this almost never happens.)

An example game is shown as below:

Alice got 0.345 and 0.192

Bob got 0.777 and 0.212

If Alice choose 0.345 and Bob choose 0.777, then Alice wins because 0.777 > 0.345 but 0.777 < 0.345\*3. If Alice choose 0.192 instead, the Bob would win as 0.777 > 0.192\*3.


Solution:

Whatever is opponent's strategy, there exists a probability distribution of his choices. Then, our strategy should be the best response to his strategy. Our best response is easy to calculate if we know opponent's distribution of choices. The value of each number is equal to the percent of opponent's choices that we are beating (weighted by their chance of picking it). We have to pick the number which has higher value. If we know this best response strategy, we can calculate what the resulting distribution of our picks will be. Next we can iterate to find opponent's best response in the same way. We can pick an initial distribution: pick randomly which is an uniform distribution of picks, then iterate on it.

If we find a pure strategy that is the best response to itself it must be the nash equilibriumn strategy. This is shown in 2pgame.py. Unfortunately this does not converge. Some regions of the distribution profile keeps oscillating. The way to fix that is to take the average strategy seen so far in each iteration instead of the last strategy when calculating the next best response. This is done in 2pgame_fixed.py. The nash equilibrium is necessarily a mixed strategy where one is indifferent in picking numbers between ~0.61 to 1 which have constant value.
