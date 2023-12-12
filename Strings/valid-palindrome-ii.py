class Solution:

    def ValidPalindrome(self, s: str) -> bool:

        left , right = 0 , len(s) -1

        while left < right :


            if s[left] != s[right]:

                # skip left char
                left_skip = s[left+1: right+1]

                # skip right
                right_skip = s[left: right]


                return left_skip == left_skip[::-1] or right_skip == right_skip[::-1]

            left , right = left +1 , right +1

        return True
