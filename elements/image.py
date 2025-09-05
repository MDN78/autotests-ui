from elements.base_element import BaseElement


class Image(BaseElement):
    def image_locator(self, **kwargs):
        self.get_locator(**kwargs)
