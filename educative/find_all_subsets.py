def get_bit(num, bit):

    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
      return 0
    return 1


def get_all_subsets(v, sets):
  """
  The number of subsets of a list, of length N,  is equal to N ** 2, or K
  , the number (K - 1) in bit value contains all 1's for N.
  So a list of length 3 has 8 subsets, 7 in bit value is 111.
  To create all subsets iterate over all numbers until (K - 1) and & this value at
  each index, J, possible so if a list is length three then J = 0, 1, 2
  """
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
      st = set([])
      for j in range(0, len(v)):
         if get_bit(i, j) == 1:
            print(f"{j =}, {i =}")
            st.add(v[j])
      sets.append(st)



print(get_bit(1, 3))

get_all_subsets([2, 5, 7], [])