from data import DataSeq

def CheckMaxHeap(data, size, child):
    if child <= size:
        father = child//2
        if data[child]>data[father]:
            print("error found")
        CheckMaxHeap(data, size, child*2)
        CheckMaxHeap(data, size, child*2+1)


def HeapSort(ds):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    # 先构建最大堆
    for i in range(1,Length):
        X = ds.data[i]
        child = i
        father = (child+1)//2-1
        while X>ds.data[father] and father>=0:
            ds.SetVal(child, ds.data[father])
            ds.Visualize((child,father))
            child=father
            father = (child+1)//2-1
        ds.SetVal(child, X)
        ds.Visualize((child,))

    # 检查最大堆是否正确
    # data = [100000]+ds.data
    # print(data)
    # CheckMaxHeap(data, ds.length, 1)

    # 再反向弹出
    p=ds.length-1
    while(p>0):
        maxval = ds.data[0]
        last = ds.data[p]
        father = 0
        child = (father+1)*2-1
        while child<p:
            if child!=(p-1) and ds.data[child]<ds.data[child+1]:
                child += 1
            if ds.data[child]<last:
                break
            else:
                ds.SetVal(father, ds.data[child])
                ds.Visualize((father, child))
                father = child
                child = (father+1)*2-1
        ds.SetVal(father, last)
        ds.SetVal(p,maxval)
        ds.Visualize((p,))
        p-=1


if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()
    ds.StartTimer()
    HeapSort(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()