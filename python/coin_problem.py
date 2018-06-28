import logging
import argparse
import sys

def parse(argv):
    logging.info("Parsing arguments")
    parser = argparse.ArgumentParser(description="Coin problem")
    parser.add_argument('--amount', dest='amount', type=int, help='Total amount to change (e.g: 245)')
    parser.add_argument('--coins', dest='coins', nargs="+", type=int, help='List of coins (e.g: 2 3 4 5)')
    return parser.parse_args(argv)


def getResult(n, p):
    return search(n, sorted(list(set(p)), reverse=True), []) 

def search(n, p, visited):
    print("n: %d\tp: %s" % (n, p))
    myn = n
    if n in p:
        print("n in p")
        myn = 1
    elif n < min(p):
        print("%d < min(p): %d" % (n, min(p)))
        myn = -1
    else:
        try:
            subset = [m for m in p if m < n]
            print("subset: %s" % str(subset))
            for i in subset:
                if n-i not in visited:
                    total = 1 + search(n - i, subset, visited)
                    visited += [n - i]
                    if total <=0:
                        total = -1
                    elif total < myn:
                        myn = total
        except Exception as e:
            myn = -1
    return myn

if __name__ == '__main__':
    argv = sys.argv
    args = parse(argv[1:])
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    result = getResult(args.amount, args.coins)
    print("FINAL RESULT: %d" % result)