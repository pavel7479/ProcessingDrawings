
from core.config import COLORS, THICKNESS
import cv2
from core.base import ImageStage

class Styler(ImageStage):
    def process(self, image, context):
        contours = context.get("contours", [])
        numbers = context.get("numbers", [])

        # Контуры деталей
        cv2.drawContours(image, contours, -1, COLORS["part_outline"], THICKNESS["outline"])

        # Номера позиций
        for item in numbers:
            x, y, w, h = item["box"]
            cv2.rectangle(image, (x, y), (x + w, y + h), COLORS["number_box"], THICKNESS["number_box"])

        return image

    def run(self, image):
        if not hasattr(self, "context"):
            self.context = {}
        return self.process(image, self.context)
