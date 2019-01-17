from data import DataSeq

def GetPivot(ds, Left, Right):
    Mid = (Left+Right)//2
    if ds.data[Left]>ds.data[Right]:
        ds.Swap(Left, Right)
    if ds.data[Left]>ds.data[Mid]:
        ds.Swap(Left, Mid)
    if ds.data[Mid]>ds.data[Right]:
        ds.Swap(Mid, Right)
    ds.Swap(Mid, Right-1)
    return ds.data[Right-1]

def Qsort(ds, Left, Right):
    Cutoff = 10
    if Cutoff <= Right-Left:
        Pivot = GetPivot(ds, Left, Right)
        low=Left+1
        high=Right-2
        while True:
            while ds.data[low]<Pivot :
                low+=1
            while ds.data[high]>Pivot:
                high-=1
            if low<high:
                ds.Swap(low, high)
                low +=1
                high-=1
            else:
                break
        ds.Swap(low, Right-1)
        Qsort(ds, Left, low-1)
        Qsort(ds, low+1, Right)

    else:
        # 元素太少， 用插入排序
        for p in range(Left,Right+1):
            tmp = ds.data[p]
            i=p
            while i>=1 and ds.data[i-1]>tmp:
                ds.SetVal(i, ds.data[i-1])
                i-=1
            ds.SetVal(i, tmp)

def QuickSort(ds):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    Qsort(ds, 0, Length-1)

if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    QuickSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()