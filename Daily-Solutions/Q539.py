class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time strings to total minutes since midnight
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(':'))
            return hours * 60 + minutes

        # Apply the conversion to each element in the list
        minutes_list = [time_to_minutes(time_str) for time_str in timePoints]

        # Sort minutes list
        minutes_list.sort()

        # Assume smallest difference
        min_diff = float('inf')
                
        # Iterate through sorted list to find the smallest difference
        for i in range(len(minutes_list) - 1):
            diff = minutes_list[i + 1] - minutes_list[i]
            if diff < min_diff:
                min_diff = diff
                
        # List of possible answers
        poss_ans = [min_diff]
    
        # "00:00" can be "1440" in minutes. And we have to check the difference from that way too. Example differece in minutes between "23:00" and "01:00" is "120"
        for i in minutes_list:
            if i > 1300:
                poss_ans.append((1440 - i) + minutes_list[0])
            
        # Return the minimum value of all the differences
        return min(poss_ans)
