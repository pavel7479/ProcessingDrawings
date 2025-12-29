import cv2
import pytesseract
from core.base import ImageStage
from core.config import CANNY

class ShapeDetector(ImageStage):
    def process(self, image, context):
        gray = context.get("gray", cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

        edges = cv2.Canny(gray, CANNY["threshold1"], CANNY["threshold2"])
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        context["contours"] = contours
        return image

    def run(self, image):
        if not hasattr(self, "context"):
            self.context = {}
        return self.process(image, self.context)



