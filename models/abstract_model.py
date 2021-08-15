from abc import ABC, abstractmethod


class AbstractModel(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def dynamics(self, state, t):
        pass

    @abstractmethod
    def __call__(self, t):
        pass