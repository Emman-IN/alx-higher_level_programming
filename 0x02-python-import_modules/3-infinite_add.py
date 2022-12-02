#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lens = len(sys.argv)
    sum = 0
    for i in range(1, lens):
        sum += int(argv[i])
    print(sum)
