def test(nums):
    pos = [n for n in nums if n>0]
    neg = [n for n in nums if n<0]
    return [max(neg) if neg else 0, min(pos) if pos else 0]

nums = eval(input())
print("Largest negative and smallest positive numbers (or 0 if none) of the said list:")
print(test(nums))
