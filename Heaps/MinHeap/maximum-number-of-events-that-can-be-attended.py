import heapq
class Solution(object):
    def maxEvents(self, events):
        events = sorted(events, key = lambda x:x[0]) #1
        total_days = max(event[1] for event in events) #2
        min_heap = [] #3
        current_day_of_event, total_events_attended, event_no = 1, 0, 0 #4
        
        
        while current_day_of_event <= total_days: #5
		    # if no events are available to attend today, let time flies to the next available event.
            if event_no < len(events) and not min_heap: #6
                current_day_of_event = events[event_no][0] #7
			
			# all events starting from today are newly available. add them to the heap.
            while event_no < len(events) and events[event_no][0] <= current_day_of_event: #8
                heapq.heappush(min_heap, events[event_no][1]) #9
                event_no += 1 #10

			# if the event at heap top already ended, then discard it.
            while min_heap and min_heap[0] < current_day_of_event: #11
                heapq.heappop(min_heap) #12

			# attend the event that will end the earliest
            if min_heap: #13
                heapq.heappop(min_heap) #14 
                total_events_attended += 1 #15
            elif event_no >= len(events): #16
                break  # no more events to attend. so stop early to save time.

            current_day_of_event += 1 #17
            
        return total_events_attended #18


    # def maxEvents(self, events: List[List[int]]) -> int:
        
    #     # sort the events by start_day of events
    #     events = sorted(events,key= lambda x:x[0])
        
    #     # event days details
    #     start_day_of_event = 1
    #     end_day_of_events = max(event[1] for event in events)
        
    #     total_events_attended = 0 
        
    #     total_events = len(events)
        
    #     min_heap = []
        
    #     event_no = 0 
        
    #     # traverse through all days
    #     while start_day_of_event <= end_day_of_events:
            
    #         if event_no < total_events and not min_heap:
    #             start_day_of_event = events[event_no][0]
        
        
    #         # if any events on that day , save events
    #         while event_no < total_events and events[event_no][0] <= start_day_of_event:
    #             heapq.heappush(min_heap, events[event_no][1])
    #             event_no +=1
            
    #         # current_day > start_day_of_event remove finshed events
            
    #         while min_heap and min_heap[0] < start_day_of_event:
    #             heapq.heappop(min_heap)
                
    #         if min_heap:
    #             heapq.heappop(min_heap)
    #             total_events_attended +=1
    #         elif event_no >=total_events:
    #             break
            
    #         start_day_of_event +=1
            
    #     return total_events_attended
        
        