from functools import cmp_to_key

nums = [3, 30, 34, 5, 9]

# 这里的 lambda 接收两个参数 x 和 y
# 规则：如果转成字符串后 x+y < y+x，则返回 1（把 x 排在 y 后面），否则返回 -1
# 从而实现将数字组合成最大数字的排序
nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))

print(nums) # 输出: [9, 5, 34, 3, 30]