n = int(input())
shares = [int(input()) for _ in range(3)]
if 0 in shares:
    print("UNFAIR")
else:
    if len(set(shares)) != 3:
        print("UNFAIR")
    else:
        if sum(shares) != n:
            print("UNFAIR")
        else:
            print("FAIR")