test_cases = int(input())
results = []
for _ in range(test_cases):
    n, k = map(int, input().split())
    students = [input().strip() for _ in range(n)]
    total_length = sum(len(name) for name in students)
    if total_length % (n // k) == 0:
        result="possible"
    else:
        result="Not possible"
    results.append(result)
for result in results:
    print(result)