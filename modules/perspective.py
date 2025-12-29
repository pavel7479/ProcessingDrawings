import cv2
import numpy as np

class Perspective:
    def __init__(
        self,
        angle_x=0,
        angle_y=0,
        angle_z=0,
        distance=800,
        shadow=False,
        shadow_offset=(20, 30),
        shadow_alpha=0.3
    ):
        self.ax = np.deg2rad(angle_x)
        self.ay = np.deg2rad(angle_y)
        self.az = np.deg2rad(angle_z)
        self.distance = distance

        self.shadow = shadow
        self.shadow_offset = shadow_offset
        self.shadow_alpha = shadow_alpha

    def _rotation_matrix(self):
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(self.ax), -np.sin(self.ax)],
            [0, np.sin(self.ax),  np.cos(self.ax)]
        ])

        Ry = np.array([
            [ np.cos(self.ay), 0, np.sin(self.ay)],
            [0, 1, 0],
            [-np.sin(self.ay), 0, np.cos(self.ay)]
        ])

        Rz = np.array([
            [np.cos(self.az), -np.sin(self.az), 0],
            [np.sin(self.az),  np.cos(self.az), 0],
            [0, 0, 1]
        ])

        return Rz @ Ry @ Rx

    def apply(self, image: np.ndarray) -> np.ndarray:
        h, w = image.shape[:2]
        cx, cy = w / 2, h / 2

        # координаты
        ys, xs = np.indices((h, w))
        xs = xs - cx
        ys = ys - cy
        zs = np.zeros_like(xs)

        coords = np.stack([xs, ys, zs], axis=-1).reshape(-1, 3)

        R = self._rotation_matrix()
        rotated = coords @ R.T

        z = rotated[:, 2] + self.distance
        z[z == 0] = 1e-6  # защита

        x_proj = (rotated[:, 0] * self.distance) / z + cx
        y_proj = (rotated[:, 1] * self.distance) / z + cy

        map_x = x_proj.reshape(h, w).astype(np.float32)
        map_y = y_proj.reshape(h, w).astype(np.float32)

        warped = cv2.remap(
            image,
            map_x,
            map_y,
            interpolation=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_CONSTANT,
            borderValue=(255, 255, 255)
        )

        if self.shadow:
            warped = self._add_shadow(warped)

        return warped

    def _add_shadow(self, image):
        shadow = np.zeros_like(image)
        dx, dy = self.shadow_offset

        shadow[max(dy,0):, max(dx,0):] = image[:image.shape[0]-dy, :image.shape[1]-dx]
        shadow = cv2.GaussianBlur(shadow, (21, 21), 0)

        return cv2.addWeighted(image, 1.0, shadow, self.shadow_alpha, 0)


