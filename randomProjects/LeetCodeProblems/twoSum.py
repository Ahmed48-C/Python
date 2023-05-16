nums = [3,2,4]

def sum():
    index_pairs = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]:
                # print('[{},{}]'.format(i,j))
                # print(nums.index(i))
                index_pairs.append([i,j])
    # print(index_pairs)
    return print(index_pairs[0])
                    
                
sum()