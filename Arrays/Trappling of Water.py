class TrapplingofWater:
    def __int__(self):
        self.description = ''

    def find_trapped_water_solution_1(self, given_array_bars):

        '''
        Time complexity: O(n^2)
        Space complexity: O(1)
        '''

        # we can  only trap water if blocks array has more than or equal to 3
        if len(given_array_bars) == 0 or len(given_array_bars) == 1 or len(given_array_bars) == 2:
            return 0
        bars_count = len(given_array_bars)
        water_count =0
        for each_bar_index in range(1, bars_count-1):
            # print(each_bar_index)
            maxLeft = maxRight = given_array_bars[each_bar_index]
            maxLeft = max(maxLeft, max(given_array_bars[:each_bar_index]))
            maxRight = max(maxRight, max(given_array_bars[each_bar_index:]))
            water_count += min(maxLeft,maxRight) - given_array_bars[each_bar_index]

        return water_count

    def find_trapped_water_solution_2(self, given_array_bars):
        # we can  only trap water if blocks array has more than or equal to 3
        if len(given_array_bars) == 0 or len(given_array_bars) == 1 or len(given_array_bars) == 2:
            return 0
        bars_count = len(given_array_bars) #10
        left_index = 0
        right_index = bars_count -1 #9
        maxLeft = given_array_bars[left_index] # 7
        maxRight = given_array_bars[right_index] # 5
        water_count =0
        # we need to check is left_index <right_index
        while left_index < right_index:
            if given_array_bars[left_index] < given_array_bars[right_index]:
                if  given_array_bars[left_index] < maxLeft:
                    water_count += maxLeft - given_array_bars[left_index]
                else:
                    maxLeft = given_array_bars[left_index]
                left_index +=1
            else:
                if given_array_bars[right_index] < maxRight:
                    water_count += maxRight - given_array_bars[right_index]
                else:
                    maxRight = given_array_bars[right_index]
                right_index -=1
        return  water_count








c = TrapplingofWater()
#  [7, 0, 4, 2, 5, 0, 6, 4, 0, 5] - 25
#  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] - 6
# print(c.find_trapped_water_solution_1( [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]))
print(c.find_trapped_water_solution_2( [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]))
