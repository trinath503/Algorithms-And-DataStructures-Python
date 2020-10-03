class FindTwoSum:
    def __int__(self):
        self.descrption = 'we need to find the indexs of the given arra'

    def find_indexes(self, given_array, target):
        store_ele_indexs = dict()
        for indx, ele in enumerate(given_array):
            current_difference = target - ele

            print(store_ele_indexs,current_difference, given_array)
            if current_difference in store_ele_indexs:
                return [store_ele_indexs[current_difference], indx]

            store_ele_indexs[ele] = indx

        return  []


t = FindTwoSum()
arr = [1,3,5,6,4]
target = 7

print(t.find_indexes(arr, target))