# core/config.py

# ===== OCR =====
OCR_CONFIG = {
    "tesseract_cmd": None,          # путь, если нужен
    "psm": 10,
    "whitelist": "0123456789-"
}

# ===== PREPROCESS =====
PREPROCESS = {
    "use_blur": False,
    "blur_ksize": (3, 3),
}

# ===== EDGE DETECTION =====
CANNY = {
    "threshold1": 70,
    "threshold2": 140,
}

# ===== STYLE =====
COLORS = {
    "part_outline": (30, 30, 200),     # BGR
    "number_box": (0, 140, 0),
}

THICKNESS = {
    "outline": 1,
    "number_box": 0.5,
}

# ===== VALIDATION =====
VALIDATION = {
    "min_digits": 1,
}
# ===== PATHS =====
PATHS = {
    "input_dir": "/root/etc/drawings",
    "output_dir": "/root/etc/drawings/remake",
}
# ===== IMAGE =====
# Какие форматы считаем изображениями
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")

# ===== PERSPECTIVE =====
PERSPECTIVE = {
    "angle_x": 12,      # наклон вверх/вниз
    "angle_y": -18,     # поворот влево/вправо
    "angle_z": 0,       # поворот в плоскости
    "distance": 2200,    # расстояние до камеры (чем меньше — тем сильнее эффект)
    "shadow": True,     # включить тень
    "shadow_offset": (12, 18),
    "shadow_alpha": 0.18
}

