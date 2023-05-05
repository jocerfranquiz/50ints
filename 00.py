# 00. Sort a sequence of integers

# Sort from less to more

# first try

def insertion_sort(l):
  len_l = len(l)

  if len_l < 2:
    return l
  if len_l == 2:
    return [l[0], l[1]] if l[0] < l[1] else [l[1], l[0]]
  if len_l > 2:
    # Insertion-sort
    for j in range(1, len(l)):
      key = l[j]
      # insert l[j] into the sorted seq l[0...j]
      i = j - 1
      while i > -1 and l[i] > key:
        l[i + 1] = l[i]
        i = i - 1
      l[i + 1] = key

    return l

if __name__ == '__main__':

  l = [4,1,2,2,7]

  print(insertion_sort(l))

# TODO: merge_sort
