class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(number, arr, total):
            if total == target:
                res.append(arr[:])
                return
            if total > target:
                return
            backtrack(number, arr + [candidates[number]], total+candidates[number])

            if number + 1 != len(candidates):
                backtrack(number+1, arr, total)
        backtrack(0, [], 0)
        return res
