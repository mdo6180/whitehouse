from .base import Component


class Template:
    def __init__(self, component: Component) -> None:
        self.component = component

    def get_component(self) -> Component:
        return self.component