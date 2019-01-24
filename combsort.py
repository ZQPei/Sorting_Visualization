from data import DataSeq



def CombSort(ds):
    Length = ds.length
    D = int(Length / 1.3)

    while D:
        for i in range(Length):
            for j in range(i+D, Length, D):
                if ds.data[j-D] > ds.data[j]:
                    ds.Swap(j-D, j)
        D = int(D / 1.3)



if __name__ == "__main__":
    ds=DataSeq(64, repeatition=True)
    ds.Visualize()
    ds.StartTimer()
    CombSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()