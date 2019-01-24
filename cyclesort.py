from data import DataSeq

def CycleSort(ds):
    """
        环排序只适用于整数排序，且数正好范围在[0,N-1]内，且只有少量重复元素，不稳定
    """
    assert isinstance(ds, DataSeq), "Type Error"
    assert isinstance(ds.data[0], int), "Type Error"

    Length = ds.length
    # 重复元素的列表
    repeatIdxs = []
    for i in range(Length):
        currIdx=i
        nextIdx=ds.data[currIdx]
        while ds.data[nextIdx] != nextIdx:
            ds.Swap(currIdx, nextIdx)
            nextIdx=ds.data[currIdx]
        if ds.data[i] != i:
            repeatIdxs.append(i)
    # 剩下少数重复元素，整个数组基本有序，使用插入排序
    # print(repeatIdxs)
    for p in range(Length):
        tmp = ds.data[p]
        i=p
        while i>=1 and ds.data[i-1]>tmp:
            ds.SetVal(i, ds.data[i-1])
            i-=1
        ds.SetVal(i, tmp)
    

if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    CycleSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()