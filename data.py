import random
import numpy as np
import time
import cv2

class DataSeq:
    WHITE = (255,255,255)
    RED = (0,0,255)
    BLACK = (0,0,0)
    YELLOW = (0,127,255)

    MAX_IM_SIZE = 500
    def __init__(self, Length, time_interval=1, sort_title="Figure", is_resampling=False, is_sparse=False, record=False, fps=25):
        self.data = [x for x in range(Length)]
        if is_resampling:
            self.data = random.choices(self.data, k=Length)
        else:
            self.Shuffle()
        if is_sparse:
            self.data = [x if random.random() < 0.3 else 0 for x in self.data]

        self.length = Length

        self.SetTimeInterval(time_interval)
        self.SetSortType(sort_title)
        self.Getfigure()
        self.InitTime()

        self.record = record
        if record:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.vdo_wtr = cv2.VideoWriter("%s.avi"%self.sort_title, fourcc, fps, (self.im_size, self.im_size), True)

        self.Visualize()

    def InitTime(self):
        self.start=time.time()
        self.time=0
        self.StopTimer()

    def StartTimer(self):
        self.start_flag=True
        self.start = time.time()

    def StopTimer(self):
        self.start_flag=False

    def GetTime(self):
        if self.start_flag:
            self.time = time.time()-self.start

    def SetTimeInterval(self, time_interval):
        self.time_interval=time_interval

    def SetSortType(self, sort_title):
        self.sort_title=sort_title

    def Shuffle(self):
        random.shuffle(self.data)

    def Getfigure(self):
        _bar_width = 5
        figure = np.full((self.length*_bar_width,self.length*_bar_width,3), 255,dtype=np.uint8)
        for i in range(self.length):
            val = self.data[i]
            figure[-1-val*_bar_width:, i*_bar_width:i*_bar_width+_bar_width] = self.GetColor(val, self.length)
        self._bar_width = _bar_width
        self.figure = figure
        size = _bar_width*self.length
        self.im_size = size if size < self.MAX_IM_SIZE else self.MAX_IM_SIZE

    @staticmethod
    def GetColor(val, TOTAL):
        return (120+val*255//(2*TOTAL), 255-val*255//(2*TOTAL), 0)

    def _set_figure(self, idx, val):
        min_col = idx*self._bar_width
        max_col = min_col+self._bar_width
        min_row = -1-val*self._bar_width
        self.figure[ : , min_col:max_col] = self.WHITE
        self.figure[ min_row: , min_col:max_col] = self.GetColor(val, self.length)

    def SetColor(self, img, marks, color):
        for idx in marks:
            min_col = idx*self._bar_width
            max_col = min_col+self._bar_width
            min_row = -1-self.data[idx]*self._bar_width
            img[min_row:, min_col:max_col] = color
    def Mark(self, img, marks, color):
        self.SetColor(img, marks, color)

    def SetVal(self, idx, val):
        self.data[idx] = val
        self._set_figure(idx, val)

        self.Visualize((idx,))

    def Swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        self._set_figure(idx1, self.data[idx1])
        self._set_figure(idx2, self.data[idx2])

        self.Visualize((idx1, idx2))

    def Visualize(self, mark1=None, mark2=None):
        img = self.figure.copy()
        if mark2:
            self.Mark( img, mark2, self.YELLOW)
        if mark1:
            self.Mark( img, mark1, self.RED)

        img = cv2.resize(img, (self.im_size, self.im_size))
        
        self.GetTime()
        cv2.putText(img, self.sort_title+" Time:%02.2fs"%self.time, (20,20), cv2.FONT_HERSHEY_PLAIN, 1, self.YELLOW, 1)

        if self.record:
            self.vdo_wtr.write(img)

        cv2.imshow(self.sort_title, img)
        cv2.waitKey(self.time_interval)

if __name__ == "__main__":
    ds = DataSeq(64, is_sparse=True)
    ds.Visualize()

    for i in range(64):
        for j in range(i,64):
            if ds.data[i]>ds.data[j]:
                ds.Swap(i,j)
                ds.Visualize( (j,i) )

    ds.Visualize()