import numpy as np
def squary():
    n, k = list(map(int, input().split(" ")))
    e = np.array(list(map(int, input().split(" "))))

    if np.sum(e)**2 == np.sum(e**2):
        return [0]
    
    # K = 1
    # (s1+...+sn+a)**2 = a**2 + 2*a*(s1+...+sn) + (s1+...+sn)**2 = s1**2+...sn**2+a**2

    if np.sum(e) != 0:
        a = (np.sum(e**2) - np.sum(e)**2) / (2 * np.sum(e))
        if int(a) == a:
            return [int(a)]
    
    # up to K
    # (s1+...sn)**2 + 2 * (a1 + ... + ak) * (s1+...+sn) + (a1 +... +ak)**2 - a1**2 - ... - ak**2 - = s1**2 + ... sn**2
    """
    squared_sum = np.sum(e**2)
    sum_squared = np.sum(e)**2
    basic_sum = np.sum(e)
    diff = squared_sum - sum_squared
    def func(x):
        return abs((np.sum(x)**2 - np.sum(x**2) + 2 * np.sum(x) * basic_sum) - diff)
    
    bounds = [(-10**18, 10**18) for _ in range(k)]
    cons = ({'type': 'eq',
             'fun': lambda x : max([abs(x[i]-int(x[i])) for i in range(len(x))])})
    # cons = NonlinearConstraint(lambda x: max([x[i]-int(x[i]) for i in range(len(x))]), -1e-3, 1e-3)
    constraints = [cons]
    x0 = np.array([1 for _ in range(k)])
    root = minimize(func, x0=x0, bounds=bounds, constraints=cons)
    """
    return "IMPOSSIBLE"

if __name__ == "__main__":
    test_cases = int(input())
    for case in range(1, test_cases + 1):
        res = squary()
        if res != "IMPOSSIBLE":
            res = [str(x) for x in res]
            res = " ".join(res)
        print(f'Case #{case}: {res}')
