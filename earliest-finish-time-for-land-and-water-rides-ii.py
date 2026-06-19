"""
You are given two categories of theme park attractions: land rides and water rides.

Land rides
landStartTime[i] – the earliest time the ith land ride can be boarded.
landDuration[i] – how long the ith land ride lasts.
Water rides
waterStartTime[j] – the earliest time the jth water ride can be boarded.
waterDuration[j] – how long the jth water ride lasts.
A tourist must experience exactly one ride from each category, in either order.

A ride may be started at its opening time or any later moment.
If a ride is started at time t, it finishes at time t + duration.
Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
Return the earliest possible time at which the tourist can finish both rides.

"""


from git import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        from bisect import bisect_right
        
        land = sorted(zip(landStartTime, landDuration))
        water = sorted(zip(waterStartTime, waterDuration))
        
        n, m = len(land), len(water)
        
        land_starts = [l[0] for l in land]
        water_starts = [w[0] for w in water]
        
        land_prefix_min_dur = [0] * n
        land_prefix_min_dur[0] = land[0][1]
        for i in range(1, n):
            land_prefix_min_dur[i] = min(land_prefix_min_dur[i-1], land[i][1])
        
        water_prefix_min_dur = [0] * m
        water_prefix_min_dur[0] = water[0][1]
        for i in range(1, m):
            water_prefix_min_dur[i] = min(water_prefix_min_dur[i-1], water[i][1])
        
        land_suffix_min_end = [10**9] * (n + 1)
        for i in range(n - 1, -1, -1):
            land_suffix_min_end[i] = min(land[i][0] + land[i][1], land_suffix_min_end[i+1])
        
        water_suffix_min_end = [10**9] * (m + 1)
        for i in range(m - 1, -1, -1):
            water_suffix_min_end[i] = min(water[i][0] + water[i][1], water_suffix_min_end[i+1])
        
        ans = 10**9
        
        for i in range(n):
            lf = land[i][0] + land[i][1]
            idx = bisect_right(water_starts, lf) - 1
            if idx >= 0:
                ans = min(ans, lf + water_prefix_min_dur[idx])
            idx2 = idx + 1
            if idx2 < m:
                ans = min(ans, water_suffix_min_end[idx2])
        
        for j in range(m):
            wf = water[j][0] + water[j][1]
            idx = bisect_right(land_starts, wf) - 1
            if idx >= 0:
                ans = min(ans, wf + land_prefix_min_dur[idx])
            idx2 = idx + 1
            if idx2 < n:
                ans = min(ans, land_suffix_min_end[idx2])
        
        return ans