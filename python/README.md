# Code Benchmarking

## Python

### Coin problem

The idea is return the minimun number of coins needed in order to give
the correct change. The function will return -1 if is impossible.

#### Usage

```bash
$ python coin_problem.py --coins 2 3 4 --amount 34
```

#### Output


```bash
n: 34   p: [4, 3, 2]
subset: [4, 3, 2]
n: 30   p: [4, 3, 2]
subset: [4, 3, 2]
n: 26   p: [4, 3, 2]
subset: [4, 3, 2]
n: 22   p: [4, 3, 2]
subset: [4, 3, 2]
n: 18   p: [4, 3, 2]
subset: [4, 3, 2]
n: 14   p: [4, 3, 2]
subset: [4, 3, 2]
n: 10   p: [4, 3, 2]
subset: [4, 3, 2]
n: 6    p: [4, 3, 2]
subset: [4, 3, 2]
n: 2    p: [4, 3, 2]
n in p
n: 3    p: [4, 3, 2]
n in p
n: 4    p: [4, 3, 2]
n in p
n: 7    p: [4, 3, 2]
subset: [4, 3, 2]
n: 5    p: [4, 3, 2]
subset: [4, 3, 2]
n: 1    p: [4, 3, 2]
1 < min(p): 2
n: 8    p: [4, 3, 2]
subset: [4, 3, 2]
n: 11   p: [4, 3, 2]
subset: [4, 3, 2]
n: 9    p: [4, 3, 2]
subset: [4, 3, 2]
n: 12   p: [4, 3, 2]
subset: [4, 3, 2]
n: 15   p: [4, 3, 2]
subset: [4, 3, 2]
n: 13   p: [4, 3, 2]
subset: [4, 3, 2]
n: 16   p: [4, 3, 2]
subset: [4, 3, 2]
n: 19   p: [4, 3, 2]
subset: [4, 3, 2]
n: 17   p: [4, 3, 2]
subset: [4, 3, 2]
n: 20   p: [4, 3, 2]
subset: [4, 3, 2]
n: 23   p: [4, 3, 2]
subset: [4, 3, 2]
n: 21   p: [4, 3, 2]
subset: [4, 3, 2]
n: 24   p: [4, 3, 2]
subset: [4, 3, 2]
n: 27   p: [4, 3, 2]
subset: [4, 3, 2]
n: 25   p: [4, 3, 2]
subset: [4, 3, 2]
n: 28   p: [4, 3, 2]
subset: [4, 3, 2]
n: 31   p: [4, 3, 2]
subset: [4, 3, 2]
n: 29   p: [4, 3, 2]
subset: [4, 3, 2]
n: 32   p: [4, 3, 2]
subset: [4, 3, 2]
FINAL RESULT: 9
```

#### More examples

##### Impossible case

```bash
$ python coin_problem.py --amount 12 --coins 10 5
```


```bash
n: 12   p: [10, 5]
subset: [10, 5]
n: 2    p: [10, 5]
2 < min(p): 5
n: 7    p: [10, 5]
subset: [5]
FINAL RESULT: -1

```