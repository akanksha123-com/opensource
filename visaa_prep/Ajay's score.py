def calculate_scores(test_cases):
    results = []
    for X, N in test_cases:
        score_per_test_case = X // 10
        score = N * score_per_test_case
        results.append(score)
    return results
T = int(input())

test_cases = []
for _ in range(T):
    X, N = map(int, input().split())
    test_cases.append((X, N))

scores = calculate_scores(test_cases)
for score in scores:
    print(score)
