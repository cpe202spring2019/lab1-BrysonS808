
def max_list_iter(int_list):  # must use iteration not recursion
	"""finds the max of a list of numbers and returns the value (not the index)
	If int_list is empty, returns None. If list is None, raises ValueError"""
	if int_list == None:
		raise ValueError
	if len(int_list) == 0:
		return None
	else:
		max = int_list[0]
		for x in (int_list):
			if x > max:
				max = x
	return max

def reverse_rec(int_list):   # must use recursion
	"""recursively reverses a list of numbers and returns the reversed list
	If list is None, raises ValueError"""
	if int_list == None:
		raise ValueError
	if len(int_list) == 0:
		return []
	else:
		return[int_list.pop()] + reverse_rec(int_list)

def bin_search(target, low, high, int_list):  # must use recursion
	"""searches for target in int_list[low..high] and returns index if found
	If target is not found returns None. If list is None, raises ValueError """
	if int_list == None:
		raise ValueError
	midpoint = int(((high - low)/2)+low)
	'''print()
	print("midpoint", midpoint, 'value', int_list[midpoint])
	print('list', int_list[low:high])
	print('low', low, 'high', high)
	print('midpoint', midpoint, 'len', len(int_list))
	print("len", len(int_list[low:high]))'''
	if int_list[midpoint] == target:
		return midpoint
	elif len(int_list[low:high]) == 1:
		#print('true none')
		return None
	elif int_list[midpoint] < target:
		#print('higher')
		return bin_search(target, midpoint, len(int_list), int_list)
	elif int_list[midpoint] > target:
		#print('lower')
		return bin_search(target, low, midpoint, int_list)
	else:
		return None

list1 = [1,23, 42, 4, 2, 9]
list2 = [1,2,3,4,5,6,7,98]
list3 = [1, 4, 6, 7, 12, 45]

def tester():
	'''print(max_list_iter(list1))
	print(max_list_iter([]))
	print()
	print(reverse_rec([1,2,3,4,5]))
	print(reverse_rec([2,34,56,2,35,3]))
	print(reverse_rec([]))
	#print(reverse_rec(None))
	print()
	#print(bin_search(None))
	print(bin_search(4, 0, len(list2), list2))
	print(bin_search(-1, 0, len(list3), list3))
	print(bin_search(70, 0, len(list3), list3))
	print(bin_search(10, 0, len(list2), list2))'''
	pass

if __name__ == "__main__":
    tester()
