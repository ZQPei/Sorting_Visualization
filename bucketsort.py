import copy

from data import DataSeq

def BucketSort(ds):
    """
        桶排序只适用于整数排序，且最大元素不能比数组元素大太多的情况
    """
    assert isinstance(ds, DataSeq), "Type Error"
    assert isinstance(ds.data[0], int), "Type Error"

    Length = ds.length
    bucket = [0 for _ in range(Length)]
    for i in range(Length):
        bucket[ds.data[i]] += 1
    j=0
    for i in range(Length):
        tmp = bucket[i]
        while tmp>0:
            ds.SetVal(j, i)
            tmp-=1
            j+=1


if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    BucketSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()