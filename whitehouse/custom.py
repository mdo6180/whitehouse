from .base import Component
from typing import List, Dict, Union



class Template(Component):
    def __init__(self, component: Component) -> None:
        super().__init__(component)

    def __str__(self) -> str:
        return self.children


class CustomComponent(Component):
    def __init__(self, children: Union[str, 'Component', List['Component']], attributes: Dict[str, str] = {}) -> None:
        super().__init__(children, attributes)
    
    def __str__(self) -> str:
        return super().__str__()