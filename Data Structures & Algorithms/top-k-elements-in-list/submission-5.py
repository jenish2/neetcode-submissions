class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        freq_num  = defaultdict(list)

        for key,v in num_freq.items():
            freq_num[v].append(key)


        freqs  = sorted(num_freq.values(),reverse = True)
        
        result = []
        for i in range(len(freqs)):
            if i < k:
                result.append(freq_num[freqs[i]])
        
        re = [sublist for sublist in result for sublist in sublist]
        reset = set(re)
        result = list(reset)
        
        return result