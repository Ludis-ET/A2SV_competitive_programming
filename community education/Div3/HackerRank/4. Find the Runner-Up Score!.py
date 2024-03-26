if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ars = sorted(set(arr))
    print(ars[-2])
