from abc import ABC, abstractmethod


class LineSegmentMetric(ABC):
    @abstractmethod
    def calculate(self, xList, yList):
        pass
 