from modules.perspective import Perspective

class Pipeline:
    def __init__(self, modules=None, config=None):
        self.modules = modules or []
        self.context = {}

        self.perspective = None
        if config and "PERSPECTIVE" in config:
            p = config["PERSPECTIVE"]
            self.perspective = Perspective(**p)

    def run(self, image):
        for module in self.modules:
            image = module.process(image, self.context)

        if self.perspective:
            image = self.perspective.apply(image)

        return image



