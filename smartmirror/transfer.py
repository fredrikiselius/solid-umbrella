from dataclasses import dataclass, field
from typing import TypeVar, Generic, Union, List
from collections import abc
import time

T = TypeVar('T')

@dataclass
class Transfer(Generic[T]):
    _is_iterable: bool = field(init=False, default=False)
    _step: Union[T, List[T]] = field(init=False)
    _start: T
    _end: T
    _duration: float
    _time: float = field(init=False, default=time.time())
    _reverse: bool = field(init=False, default=False)

    def __post_init__(self):
        if type(self._start) != type(self._end): raise TypeError('different types for _start and _end')
        if isinstance(self._start, abc.Iterable):
            if len(self._start) != len(self._end): raise ValueError('_start and _end have different lengths')
            self._is_iterable = True
            self._step = [(self._end[i] - self._start[i]) / self._duration for i in range(len(self._start))]
        else:
            self._step = (self._end - self._start) / self._duration

    def at_time(self, time: float) -> T:
        if time < 0: raise ValueError('time must be >= 0')

        if self._is_iterable:
            length: int = len(self._start)
            if self._reverse:
                values = [self._end[i] - (self._step[i] * time) for i in range(length)] if time < self._duration else self._start
            else:
                values = [self._start[i] + (self._step[i] * time) for i in range(length)] if time < self._duration else self._end
            return type(self._start)(values)
        if self._reverse:
            return self._end - (self._step * time) if time < self._duration else self._start
        else:
            return self._start + (self._step * time) if time < self._duration else self._end

    @property
    def next(self):
        return self.at_time(time.time() - self._time)

    def reverse(self):
        self._reverse = not self._reverse
        time_diff = time.time() - self._time
        travel = self._duration - time_diff if time_diff < self._duration else 0
        self._time = time.time() - travel




