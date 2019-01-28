from data import DataSeq
from bubblesort import BubbleSort
from bucketsort import BucketSort
from combsort import CombSort
from cyclesort import CycleSort
from heapsort import HeapSort
from insertionsort import InsertionSort
from mergesort import MergeSort
from monkeysort import MonkeySort
from quicksort import QuickSort
from radixsort import RadixSort
from selectionsort import SelectionSort
from shellsort import ShellSort

import argparse
parser=argparse.ArgumentParser(description="Sort Visulization")
parser.add_argument('-l','--length',type=int,default=64)
parser.add_argument('-i','--interval',type=int,default=1)
parser.add_argument('-t','--sort-type',type=str,default='BubbleSort', 
                                    choices=["BubbleSort","BucketSort","CombSort",
                                            "CycleSort","HeapSort","InsertionSort",
                                            "MergeSort","MonkeySort","QuickSort",
                                            "RadixSort","SelectionSort","ShellSort",])
parser.add_argument('-r','--resample', action='store_true')
parser.add_argument('-s','--sparse', action='store_true')
parser.add_argument('-n','--no-record', action='store_true')
args=parser.parse_args()



if __name__ == "__main__":
    MAXLENGTH=1000
    Length=    args.length if args.length<MAXLENGTH else MAXLENGTH
    Interval=  args.interval
    SortType=  args.sort_type
    Resampling=args.resample
    Sparse=    args.sparse
    NoRecord=  args.no_record
    try:
        SortMethod=eval(SortType)
    except:
        print("Sort Type Not Found! Please Check if %s Exists or Not!"%SortType)
        exit()

    ds=DataSeq(Length, time_interval=Interval, sort_title=SortType, is_resampling=Resampling, is_sparse=Sparse, record=not NoRecord)
    ds.Visualize()
    ds.StartTimer()
    SortMethod(ds)
    ds.StopTimer()
    ds.SetTimeInterval(0)
    ds.Visualize()