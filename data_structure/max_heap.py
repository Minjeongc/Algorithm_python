# 힙과 이진트리와의 공통점 및 차이점
#https://m.blog.naver.com/leeinje66/221622360256 


class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1

        while i > 1:
            if self.data[i] < self.data[(i//2)]:
                self.data[i], self.data[(i//2)] = self.data[(i//2)], self.data[i]
                i = i //2
            else:
                break
    
    def remove(self):
        if len(self.data) > 1:
            self.data[1] , self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data
    
