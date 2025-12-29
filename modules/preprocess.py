import cv2
from core.config import PREPROCESS
from core.base import ImageStage  # если у тебя есть базовый класс

class Preprocessor(ImageStage):
    def process(self, image, context):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if PREPROCESS["use_blur"]:
            gray = cv2.GaussianBlur(gray, PREPROCESS["blur_ksize"], 0)

        context["gray"] = gray
        return image

    def run(self, image):
        if not hasattr(self, "context"):
            self.context = {}
        image = self.process(image, self.context)
        return image


