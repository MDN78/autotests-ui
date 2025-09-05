from elements.base_element import BaseElement


class Link(BaseElement):
    def link(self, **kwargs):
        self.get_locator(**kwargs)
