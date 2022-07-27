
#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
#where the chosen numbers sum to target. 
#You may return the combinations in any order.
#The same number may be chosen from candidates an unlimited number of times. 
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        
        def findCombinations(ind,target,ans,ds):
            if ind == length:
                if target == 0:
                    ans.append(list(ds))
                return
            
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                findCombinations(ind,target-candidates[ind],ans,ds)
                ds.pop()
                
            findCombinations(ind+1,target,ans,ds)
            
        
        ans = []
        findCombinations(0,target,ans,[])
        return ans
                
