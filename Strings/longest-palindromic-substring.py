# expand in both directions of low and high to find
# maximum length palindrome
def expand(str, low, high):

	length = len(str)

	# expand in both directions
	while low >= 0 and high < length and str[low] == str[high]:
		low = low - 1
		high = high + 1

	# return palindromic substring
	return str[low + 1:high]


# Function to find Longest Palindromic substring in O(n^2) time and O(1) space
def LongestPalindromicsubstring(str, length):

	# max_str stores the maximum length palindromic substring found so far
	max_str = ""

	# max_length stores the length of maximum length palindromic
	# substring found so far
	max_length = 0

	# consider every adjacent pair of characters as mid points and
	# expand in both directions to find maximum length palindrome

	for i in range(length):

		# find a longest odd length palindrome with str[i] as mid point
		curr_str = expand(str, i, i)
		curr_length = len(curr_str)

		# update maximum length palindromic substring if odd length
		# palindrome has greater length

		if curr_length > max_length:
			max_length = curr_length
			max_str = curr_str

		# find a longest even length palindrome with str[i] and str[i+1] as mid points
		# Note that a even length palindrome has two mid points

		curr_str = expand(str, i, i + 1)
		curr_length = len(curr_str)

		# update maximum length palindromic substring if even length
		# palindrome has greater length

		if curr_length > max_length:
			max_length = curr_length
			max_str = curr_str

	return max_str


if __name__ == '__main__':

	str = "ABDCBCDBDCBBC"

	print("Longest Palindromic substring is", 
          LongestPalindromicsubstring(str, len(str) - 1))
