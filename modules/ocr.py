import cv2
from core.config import OCR_CONFIG

import pytesseract
from core.config import OCR_CONFIG
from core.base import ImageStage

class OCRDetector(ImageStage):
    def process(self, image, context):
        gray = context.get("gray", cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

        if OCR_CONFIG["tesseract_cmd"]:
            pytesseract.pytesseract.tesseract_cmd = OCR_CONFIG["tesseract_cmd"]

        config_str = (
            f"--psm {OCR_CONFIG['psm']} "
            f"-c tessedit_char_whitelist={OCR_CONFIG['whitelist']}"
        )

        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, config=config_str)

        numbers = []
        for i, text in enumerate(data["text"]):
            if text.strip().isdigit():
                numbers.append({
                    "text": text,
                    "box": (data["left"][i], data["top"][i], data["width"][i], data["height"][i])
                })

        context["numbers"] = numbers
        return image

    def run(self, image):
        if not hasattr(self, "context"):
            self.context = {}
        return self.process(image, self.context)


