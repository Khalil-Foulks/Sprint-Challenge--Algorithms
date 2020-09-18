#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

When n is 2 the while loop has to run 2 times. When n is 3 the loop runs 3 times.
The number of loops is dependent on whatever n is so the runtime is linear, O(n)

b) O(n log n)

The for loop is runtime O(n) it runs a loop 1 time until it reaches n
The while loop runs multiple times per index in the for loop which makes it worse than O(n).


c) O(n)

The recursion will run decreasing bunnies by 1 each time until the number of bunnies reaches 0. Which makes it similar to a for loop.

## Exercise II

n-story building
egg breaks if dropped from >= floor f 
egg doesn't break if dropped from < floor f
find value of f


- I want to find the midpoint of the building and drop an egg.
- If the egg doesn't break then floor f is on a floor higher than the midpoint.
- Then I ignore everything from the midpoint down and update the midpoint. 
- If the egg breaks then the middle floor of the building is where floor f is or it's higher than floor f. 
- Then I ignore everything above the midpoint and update the midpoint using the floors below. 
- I repeat until I've gone through all the floors or the midpoint is floor f


runtime is O(log n) because i'm using binary searching
