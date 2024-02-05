from whitehouse.base import Component
from whitehouse.default import *
from whitehouse.utils import format_html

from typing import List, Dict, Union



class CustomComponent(Component):
    def __init__(
        self, 
        child1: Union[str, 'Component', List['Component']], 
        child2: Union[str, 'Component', List['Component']], 
        attributes: Dict[str, str] = {}
    ) -> None:
        super().__init__([
            div([
                p("Hello, World 1!"),
                child1
            ], {"class": "container"}),
            div([
                p("Hello, World 2!"),
                child2
            ], {"class": "container"})
        ], attributes=attributes)

    def __str__(self) -> str:
        return super().__str__() 
    

if __name__ == "__main__":
    component = html([
        head([
            title("Hello, World!"),
            meta({"charset": "UTF-8", "name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
            link({"rel": "stylesheet", "href": "style.css"}),
            script("", {"src": "script.js"})
        ]),
        body([
            CustomComponent(
                p("Hello, World 3!"), 
                p("Hello, World 4!"), 
                {"id": "custom-component1"}
            ),
            CustomComponent(
                p("Hello, World 5!"), 
                p("Hello, World 6!"), 
                {"id": "custom-component2"}
            ),
            script("console.log('Hello, World!');")
        ])
    ])

    print(format_html(component))  # Output: "Hello, World!

    print(format_html([
        CustomComponent(p("Hello, World 3!"), p("Hello, World 4!"), {"id": "custom-component1"}),
        CustomComponent(p("Hello, World 5!"), p("Hello, World 6!"), {"id": "custom-component2"})
    ]))  # Output: "Hello, World!