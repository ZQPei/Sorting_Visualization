from data import DataSeq
from bubblesort import BubbleSort
from bucketsort import BucketSort
from cyclesort import CycleSort
from heapsort import HeapSort
from insertionsort import InsertionSort
from mergesort import MergeSort
from quicksort import QuickSort
from selectionsort import SelectionSort
from shellsort import ShellSort

import argparse
parser=argparse.ArgumentParser(description="Sort Visulization")
parser.add_argument('-l','--length',type=int,default=64)
parser.add_argument('-i','--interval',type=int,default=1)
parser.add_argument('-t','--sort-type',type=str,default='BubbleSort')
parser.add_argument('-r','--repetition',action='store_true')
args=parser.parse_args()



if __name__ == "__main__":
    MAXLENGTH=1000
    Length = args.length if args.length<MAXLENGTH else MAXLENGTH
    Interval=args.interval
    SortType=args.sort_type
    Repetition=args.repetition
    try:
        SortMethod=eval(SortType)
    except:
        print("Sort Type Not Found!")
        exit()

    ds=DataSeq(Length, time_interval=Interval, sort_title=SortType, repeatition=Repetition)
    ds.Visualize()
    ds.StartTimer()
    SortMethod(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()