
import os
import cv2

from core.config import PATHS, PERSPECTIVE, IMAGE_EXTENSIONS
from core.pipeline import Pipeline
from modules.preprocess import Preprocessor
from modules.ocr import OCRDetector
from modules.shapes import ShapeDetector
from modules.style import Styler

def main():
    input_dir = PATHS["input_dir"]
    output_dir = PATHS["output_dir"]

    if not os.path.isdir(input_dir):
        raise ValueError(f"Входная папка не существует: {input_dir}")

    os.makedirs(output_dir, exist_ok=True)

    pipeline = Pipeline(
        modules=[
            Preprocessor(),
            OCRDetector(),
            ShapeDetector(),
            Styler(),
        ],
        config={"PERSPECTIVE": PERSPECTIVE}  # вот тут передаём конфиг
    )

    files = sorted(os.listdir(input_dir))

    for filename in files:
        if not filename.lower().endswith(tuple(IMAGE_EXTENSIONS)):
            continue

        input_path = os.path.join(input_dir, filename)
        image = cv2.imread(input_path)

        if image is None:
            print(f"⚠️ Пропущен файл (не изображение): {filename}")
            continue

        result = pipeline.run(image)

        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, result)

        print(f"✅ Обработан: {filename}")

if __name__ == "__main__":
    main()


