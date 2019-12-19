from src.data import DataSeq
from src.bubblesort import BubbleSort
from src.bucketsort import BucketSort
from src.combsort import CombSort
from src.cyclesort import CycleSort
from src.heapsort import HeapSort
from src.insertionsort import InsertionSort
from src.mergesort import MergeSort
from src.monkeysort import MonkeySort
from src.quicksort import QuickSort
from src.radixsort import RadixSort
from src.selectionsort import SelectionSort
from src.shellsort import ShellSort

import argparse

def parse_args():
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
    parser.add_argument('--no-record', action='store_true')
    parser.add_argument('--silent', action='store_true')
    parser.add_argument('--sound-interval', type=int, default=16)
    args=parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_args()
    MAXLENGTH=1000
    Length     = args.length if args.length<MAXLENGTH else MAXLENGTH
    Interval   = args.interval
    SortType   = args.sort_type
    Resampling = args.resample
    Sparse     = args.sparse
    NoRecord   = args.no_record
    NoSound    = args.silent
    sound_interval = args.sound_interval
    try:
        SortMethod=eval(SortType)
    except:
        raise RuntimeError("Sort Type Not Found! Please Check if %s Exists or Not!"%SortType)
        exit()
    if not NoSound and sound_interval*10<Interval:
        raise UserWarning("UserWarning: sound interval too small")

    ds=DataSeq(Length, time_interval=Interval, 
                        sort_title=SortType, 
                        is_resampling=Resampling, 
                        is_sparse=Sparse, 
                        record=not NoRecord, 
                        sound=not NoSound, sound_interval=sound_interval)
    ds.StartTimer()
    SortMethod(ds)
    ds.StopTimer()
    ds.Hold()