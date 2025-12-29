
# базовый интерфейс

from abc import ABC, abstractmethod
import numpy as np

class ImageStage(ABC):
    @abstractmethod
    def process(self, image: np.ndarray, context: dict) -> np.ndarray:
        pass
