from data import DataSeq

Radix = 10

def GetDigit(x, d):
    # 得到第d位的数字
    assert(d>0), "Error"
    return (x//10**(d-1))%10
    

def CountDigits(x):
    # 得到x的位数
    cnt = 0
    while x:
        cnt+=1
        x//=10
    return cnt

def RadixSortLSD(ds):
    MaxCountDigits = 0
    # 得到最大的位数
    for i in range(ds.length):
        tmp = CountDigits(ds.data[i])
        MaxCountDigits = tmp if MaxCountDigits < tmp else MaxCountDigits

    # 基数排序， LSD
    Bucket = {i:[] for i in range(Radix)}
    for i in range(ds.length):
        digit = GetDigit(ds.data[i], 1)
        Bucket[digit].append(ds.data[i])

    for d in range(2, MaxCountDigits+1):
        NewBucket = {i:[] for i in range(Radix)}
        for i in range(Radix):
            for x in Bucket[i]:
                digit = GetDigit(x, d)
                NewBucket[digit].append(x)
        del Bucket
        Bucket = NewBucket

    # 对原数组赋值
    idx = 0
    for i in range(Radix):
        for x in Bucket[i]:
            ds.SetVal(idx, x)
            idx += 1

RadixSort = RadixSortLSD

    
if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    RadixSortLSD(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()