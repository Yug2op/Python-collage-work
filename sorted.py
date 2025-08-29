nums = [20,10,40,30]
sorted_nums = sorted(nums)
print("Original list:", nums)
print("Sorted list:", sorted_nums)

# nums.sort()
print("List after sort() method:", nums)
print("Sorted list using sort() method:", nums)

animals = ['tiger', 'cat', 'elephant', 'lion', 'peacock']
sorted_animals = sorted(animals)
print(sorted_animals)

sorted_animals_by_len = sorted(animals, key=len)
print(sorted_animals_by_len)

pairs = [(1, 3), (2, 1), (3, 2)]
sorted_pairs = sorted(pairs)
print(sorted_pairs)

def itemgetter(pairs):
    return pairs[1]
sorted_pairs_by_second_element = sorted(pairs, key=itemgetter)
print(sorted_pairs_by_second_element)

nums.sort(reverse=True)
print(nums)
