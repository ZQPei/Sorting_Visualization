from data import DataSeq



def ShellSort(ds):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    D = Length//2
    while D>0:
        i=0
        while i<Length:
            tmp = ds.data[i]

            j=i
            while j>=1 and ds.data[j-D]>tmp:
                ds.SetVal(j, ds.data[j-D])
                j-=D
            ds.SetVal(j, tmp)

            i+=D
        D//=2




if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    ShellSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()