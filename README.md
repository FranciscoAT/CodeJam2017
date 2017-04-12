# CodeJam 2017

-------------
##[Round 1](https://code.google.com/codejam/contest/3264486/dashboard#s=a)

### Problem A

Problem A was a pancake flipper. My solution was to check if any panckackes in the flipper were side down then to flip.\s
Then move to the right one and continue until the end. If the last check for if any side-down pancakes returned true then \s
it was impossible.

### Problem B

Problem B was to find the first point in the integer where a number went from `N[x] > N[y]` where `x>y`. Then to subtract one from \s
`N[x]` and switch all integers from `N[y]` to `N[z]` where `z` is last int in integer to 9. Then to iterate backwards from `N[x]`. If now \s
`N[x-1] > N[x]`. Then subtract 1 from `N[x-1]` and change `N[x]` to 9. Repeat this process until `N[x-n] <= N[x-n+1]`. Then we can ensure that \s
all values in `N` are increasing. Then return `N`.

### Problem C

Problem C was a tricky one. The first small solution was to actually implement an array and work with a physical array. However \s
when I get to Small-in 2 I realized that this solution took way too long. So had to work on the program. I came very close and it turns \s out my solution was off by a faulty calculation. In such a way some solutions like `13 6` would return `1 1` instead of proper `1 0`.

### Round 1 Conclusion

All told I scored Perfectly on A and B. And on C small 1, earning 40 points. Very excited for the next round!
