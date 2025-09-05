from elements.base_element import BaseElement


class Text(BaseElement):
    def text_locator(self, **kwargs):
        self.get_locator(**kwargs)
