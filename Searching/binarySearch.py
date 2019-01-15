
'''
nums: 排序過後的array
target: 欲尋找的目標值
l: window 左邊的 index
r: window 右邊的 index
'''

def binarySearch(nums, target, l, r):
    
	m = (l + r) // 2 
    print("Now l: %d, Now r: %d, Now m: %d" % (l, r, m))
    
    if l > r: ## 找不到目標的情況下, 最後會因為l, r相等, 再遞迴一次(m+1, r) 之後, l會大於r, 把這個條件作為終止條件
        print("Target is not in nums array...")
        return
    
    if target > nums[m]:  ## 當目標比中間值大, ex: 目標:50, 目前中間值為20, 右邊的序列: [20][23]..[100] @ 所以l傳入 m+1, 也就是[23]的位置, 右邊r不動
        return binarySearch(nums, target, m+1, r) ## 要加return, 把遞迴的最終結果一層層傳回來!
    elif target < nums[m]:
        return binarySearch(nums, target, l, m-1)
    else:
        print("At index %d find target %d" % (m, nums[m]))
        return m    
		
nums = [1, 8, 9, 15, 25, 33, 42, 66, 74, 81, 90]
last_idx = len(nums) - 1

binarySearch(nums, 25, 0, last_idx)
binarySearch(nums, 81, 0, last_idx)
binarySearch(nums, 10, 0, last_idx)
binarySearch(nums, 1, 0, last_idx)
binarySearch(nums, 90, 0, last_idx)

'''
Now l: 0, Now r: 10, Now m: 5
Now l: 0, Now r: 4, Now m: 2
Now l: 3, Now r: 4, Now m: 3
Now l: 4, Now r: 4, Now m: 4
At index 4 find target 25

Now l: 0, Now r: 10, Now m: 5
Now l: 6, Now r: 10, Now m: 8
Now l: 9, Now r: 10, Now m: 9
At index 9 find target 81

Now l: 0, Now r: 10, Now m: 5
Now l: 0, Now r: 4, Now m: 2
Now l: 3, Now r: 4, Now m: 3
Now l: 3, Now r: 2, Now m: 2
Target is not in nums array...

Now l: 0, Now r: 10, Now m: 5
Now l: 0, Now r: 4, Now m: 2
Now l: 0, Now r: 1, Now m: 0
At index 0 find target 1

Now l: 0, Now r: 10, Now m: 5
Now l: 6, Now r: 10, Now m: 8
Now l: 9, Now r: 10, Now m: 9
Now l: 10, Now r: 10, Now m: 10
At index 10 find target 90
'''