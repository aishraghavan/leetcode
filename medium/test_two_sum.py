from design_two_sum import TwoSum


def test_case_1():
	sol = TwoSum()
	sol.add(1)
	sol.add(3)
	sol.add(5)
	print sol.num_list
	print sol.find(4)

if __name__ == "__main__":
	test_case_1()