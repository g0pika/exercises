
class Solution:
	def longSubarrWthSumDivByK (self,arr,n,K): 
		lsum = []
		mxsum = {0:-1}
		remls = []
		res = 0
        
		for i, val in enumerate(arr):
		    if i>0:
		        nxt += val
		    else:
		        nxt = val
		    rem = nxt % K    
		    lsum.append(nxt)
		    remls.append(rem)
		    
		    if rem in mxsum:
		        res = max(res, i-mxsum[rem])
		    
		    if rem not in mxsum:
		        mxsum[rem] = i
        return mxsum
        
