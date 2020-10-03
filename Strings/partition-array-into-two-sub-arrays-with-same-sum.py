class Partition_Array_Into_two_parts:
    def __init__(self):
        self.author = 'Trinath Redd'

    def set_array(self,array):
        self.given_array = array

    def get_array(self):
        return self.given_array

    def do_partition(self, given_array=None):
        if given_array is None:
            self.given_array
        else:
            self.given_array = given_array

        # 1. First edge case
        if total_sum %2 !=0 or len(self.given_array)==0:
            return -1
        total_sum = sum(self.given_array)
        current_sum = 0
        for ele in range(len(self.given_array)):
            if current_sum == total_sum-current_sum:
                return ele

            current_sum += self.given_array[ele]
        return -1

if __name__ == '__main__':

    # A = [6, -4, -3, 2, 3]
    A = [3, 1, 1, 2, 2,1,]
    p = Partition_Array_Into_two_parts()
    # get index i that points to starting of second sublist
    partition_index = p.do_partition(A)

    if partition_index != -1:
        print(A[:partition_index])  # print the first sublist [0, i-1]
        print(A[partition_index:])  # print the second sublist [i, len(A))
    else:
        print("The list can't be partitioned")
