# CodeJam 2017

-------------
## [Round 0](https://code.google.com/codejam/contest/3264486/dashboard#s=a)

### Problem A

Problem A was a pancake flipper. My solution was to check if any panckackes in the flipper were side down then to flip. Then move to the right one and continue until the end. If the last check for if any side-down pancakes returned true then it was impossible.

### Problem B

Problem B was to find the first point in the integer where a number went from `N[x] > N[y]` where `x>y`. Then to subtract one from `N[x]` and switch all integers from `N[y]` to `N[z]` where `z` is last int in integer to 9. Then to iterate backwards from `N[x]`. If now `N[x-1] > N[x]`. Then subtract 1 from `N[x-1]` and change `N[x]` to 9. Repeat this process until `N[x-n] <= N[x-n+1]`. Then we can ensure that all values in `N` are increasing. Then return `N`.

### Problem C

Problem C was a tricky one. The first small solution was to actually implement an array and work with a physical array. However when I get to Small-in 2 I realized that this solution took way too long. So had to work on the program. I came very close and it turns out my solution was off by a faulty calculation. In such a way some solutions like `13 6` would return `1 1` instead of proper `1 0`.

### Round 0 Conclusion

All told I scored Perfectly on A and B. And on C small 1, earning 40 points. Very excited for the next round!

------------
## [Round 1A](https://code.google.com/codejam/contest/5304486/dashboard#s=p1) <a name="round1a"></a>

### Problem A

In retrospect some of the solutions could have been more easily done. But essentiall the solution was to while reading the rows to fill them in accordingly. So find all the question marks until a letter is hit then fill those in with that letter. If any exist after the letter do so with those until you hit another letter then repeat the process. This ensures that any remaming rows that contain a question mark will be all question marks. So essentially here we duplicate the process with the filling out horizontally but duplicate the rows in whole.

### Problem B

This problem I had just finished the solution however did not have time to fully submit. The solution was to essentially iterate through all the packages. Then find the closest multiplier `N` compared to the grams required for that ingredient. Then to check the package value and test if it is within `0.9*N*Default` to `1.1*N*Default`. Then split those packages into their multiplier. Iterate through the packages of each type and get the min of all of value N for all N. Then add up all those values and return the number of recipes.

### Round 1A Conclusion

A little more difficult questions compared to the ones I had practiced previously. However enjoyable none the less and excited for being able to qualify in Round 1B.

-----------
## [Round 1B](#)

### Problem A

This was a straight forward problem. Essentially had to calculate each horses total number of hours to reach the destination. Then take the number of hours it took that horse to reach the end and divide it into the total distance. This gave the constant speed for the first horse to reach the end without slowing down.

### Problem B

This problem was a little more difficult. Post event I got the small input correct however did not get the large input correct. The solutions was essentially a series of logic to figure out which pony should go where.

### Round 1B Conclusion

A little more easy than [Round 1A](#round1a), however still spent a little too long figuring out the logic on Problem B. Leaving me with not enough time to complete Problem C. Nevertheless enjoyable, I feel my Python skills ever improving and learning about some interesting libraries to help me along.
