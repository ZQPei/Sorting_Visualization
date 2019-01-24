from data import DataSeq
import time
import random
random.seed(42)

MAX_TIME = 30

def MonkeySort(ds):
    Length = ds.length

    while True:
        i=1
        while i<Length:
            if ds.data[i-1] < ds.data[i]:
                i+=1
            else:
                break
        if i==Length or ds.time>MAX_TIME:
            break

        random.shuffle(ds.data)
        ds.Getfigure()
        ds.Visualize()
        time.sleep(0.1)

if __name__ == "__main__":
    ds=DataSeq(64, repeatition=True)
    ds.Visualize()
    ds.StartTimer()
    MonkeySort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()