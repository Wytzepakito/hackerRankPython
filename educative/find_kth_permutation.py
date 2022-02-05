def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n - 1)


def find_kth_permutation(v, k, result):
  if not v:
    return result

  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  
  selected = (k - 1) // count

  result += str(v[selected])
  print(result)
  del v[selected]
  print(v)
  print(k)
  k = k - (count * selected)
  find_kth_permutation(v, k, result)


res = []
find_kth_permutation([1, 2, 3], 6, [])
print(res)


res = []

find_kth_permutation([1,2,3,4], 8, res)


print(res)
