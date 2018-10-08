# game-theory
A game about choosing numbers
Each player recieve 2 random real number from 0 to 1 (with uniform distribution) secretly. Then both simultaneously choose a number from the two choice he get.

After revealing both numbers, the bigger one wins if it's more than 3 times bigger than the smaller one. (Draw if both player choose the same number. But this almost never happens.)

An example game is shown as below:

Alice got 0.345 and 0.192

Bob got 0.777 and 0.212

If Alice choose 0.345 and Bob choose 0.777, then Alice wins because 0.777 > 0.345 but 0.777 < 0.345*3. If Alice choose 0.192 instead, the Bob would win as 0.777 > 0.192*3.

