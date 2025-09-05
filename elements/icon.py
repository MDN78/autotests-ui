from elements.base_element import BaseElement


class Icon(BaseElement):
    def icon_locator(self, **kwargs):
        self.get_locator(**kwargs)
