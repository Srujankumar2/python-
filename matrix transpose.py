def find_sum_and_difference(elements, M, N):
    elements.sort(reverse=True)
    Mth_max = elements[M - 1]
    elements.sort()
    Nth_min = elements[N - 1] 
    sum_result = Mth_max + Nth_min
    diff_result = abs(Mth_max - Nth_min)
    return Mth_max, Nth_min, sum_result, diff_result
elements = list(map(int, input("Enter the elements : ").split()))
M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))
Mth_max, Nth_min, sum_result, diff_result = find_sum_and_difference(elements, M, N)
print(f"{M}st Maximum Number = {Mth_max}")
print(f"{N}rd Minimum Number = {Nth_min}")
print(f"Sum = {sum_result}")
print(f"Difference = {diff_result}")
