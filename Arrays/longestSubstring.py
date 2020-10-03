def longestSubtring(given_string):
    '''
    :param given_string: str
    :return: str
    '''
    window = {}

    # to store last max string indexs
    min_index =0
    max_index =0

    #to balance the window size
    low = high =0
    while high < len(given_string):

        if window.get(given_string[high]):

            while given_string[low] != given_string[high]:
                window[given_string[low]] = False
                low += 1
            low +=1
        else:
            window[given_string[high]] = True
            if max_index -min_index < high - low:
                min_index =low
                max_index = high

        high +=1

    return given_string[min_index:max_index+1]

str = "abbcdafeegh"
print(longestSubtring(str))

