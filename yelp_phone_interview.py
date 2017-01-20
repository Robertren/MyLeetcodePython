def enumerate(self, s):
	Solution.res = []
	result_list = []
	self.recursion(s, "")  
	# for i in Solution.res:
	# 	if black_box_function(i):
	# 		result_list.append(i)
	return result_list




def recursion(self, s, sequence): 
# sequence is used to store the results, it keeps increasing length
# s is the target string and it keeps shrinking
	if len(s) == 1:
		if s.isalpha():
			result_upper = sequence + s[0].upper()
			result_lower = sequence + s[0].lower()
			Solution.res.append(result_lower[::-1]) # the order of sequence should be reversed 
			Solution.res.append(result_upper[::-1])
			return
		else:
			result_num = sequence + s[0]
			Solution.res.append(result_num[::-1])
			return 
	else:
		if s.isalpha():
			self.recursion(s[0:-1] , sequence + s[-1].lower())
			self.recursion(s[0:-1] , sequence + s[-1].upper())
		else:
			self.recursion(s[0:-1], sequence + s[-1])

