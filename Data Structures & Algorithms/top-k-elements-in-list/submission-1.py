class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        tally = dict()
        for num in nums:
            if num not in tally:
                tally[num] = 0
            tally[num] += 1
        
        count_tally_arr = [0] * (N)
        for num, count in tally.items():
            if count_tally_arr[count - 1] == 0: count_tally_arr[count - 1] = list()
            count_tally_arr[count - 1].append(num)
        res = []
        for i in range(N - 1, -1, -1):
            if count_tally_arr[i] == 0: continue
            for num in count_tally_arr[i]:
                if k <= 0: break
                res.append(num)
                k -= 1

        return res
