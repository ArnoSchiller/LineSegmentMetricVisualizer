import numpy as np

from metrics.lineSegmentMetric import LineSegmentMetric


class SumSquaredError(LineSegmentMetric):
    
    def __init__(self,weight):
        super().__init__

    def calculate(self, xList, yList):
        xMean = np.mean(xList)
        xSSE = np.sum([np.square(x - xMean) for x in xList])
        
        yMean = np.mean(yList)
        ySSE = np.sum([np.square(y - yMean) for y in yList])

        # how to combine multiple SSE?
        return xSSE + ySSE


if __name__ == '__main__':
    metric = SumSquaredError(weight = 1)

    print(metric.calculate([0,0], [1,1])) # 0.0
    print(metric.calculate([1,1], [0,1])) # 0.5
    print(metric.calculate([0,1], [0,1])) # 1.0
