import copy

from data import DataSeq

def Merge(ds, L, R, RightEnd, time_interval):
    tmpData = copy.copy(ds.data)
    LeftEnd = R-1
    i=L
    j=R
    k=L
    # import ipdb; ipdb.set_trace()
    while i<=LeftEnd and j<=RightEnd:
        if tmpData[i] < tmpData[j]:
            ds.SetVal(k, tmpData[i]) 
            i+=1
        else:
            ds.SetVal(k, tmpData[j]) 
            j+=1
        k+=1
    while i<=LeftEnd:
        ds.SetVal(k, tmpData[i]) 
        k+=1
        i+=1
    while j<=RightEnd:
        ds.SetVal(k, tmpData[j]) 
        k+=1
        j+=1

def Sort(ds, L, RightEnd, time_interval):
    # import ipdb; ipdb.set_trace()
    if RightEnd>L:
        mid = (L+RightEnd)//2
        Sort(ds,L,mid, time_interval)
        Sort(ds,mid+1,RightEnd, time_interval)
        Merge(ds,L,mid+1,RightEnd, time_interval)



def MergeSort(ds, time_interval=1):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    Sort(ds, 0,Length-1, time_interval)



    


if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    MergeSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()