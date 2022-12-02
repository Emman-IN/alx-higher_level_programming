#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lens = len(sys.argv)
    sum = 0
    for i in range(1, lens):
        sum += int(sys.argv[i])
    print(sum)
