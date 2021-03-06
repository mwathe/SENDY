from itertools import combinations as C


def reunion(even, odd):
    oddN = [i for i in range(1, (odd * 2) + 1) if i % 2 != 0]
    evenN = [i for i in range(1, (even * 2) + 1) if i % 2 == 0]
    odds = [list(C(oddN, i)) for i in range(1, len(oddN) + 1)]
    odds = [j for i in odds for j in i]
    oddpics = [(s,) + i for i in odds for s in evenN if all([s > v for v in i])]
    print(f"Odd number pictures: {oddpics}")
    evens = [list(C(evenN, i)) for i in range(1, len(evenN) + 1)]
    evens = [j for i in evens for j in i]
    evenpics = [
        (s,) + i for i in evens for s in oddN if all([s > v for v in i])]
    print(f"Even number pictures: {evenpics}")
    return len(oddpics + evenpics)


v = reunion(2, 3)     #inputs test
print(v)
