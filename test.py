from whitehouse.base import Component
from whitehouse.default import *
from whitehouse.utils import format_html
from whitehouse.custom import Template

from typing import List, Dict, Union



class MyComponent(Component):
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
    

class IndexTemplate(Template):
    def __init__(self, body_content: Component) -> None:
        super().__init__(
            html([
                head([
                    title("Hello, World!"),
                    meta({"charset": "UTF-8", "name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
                ]),
                body([
                    body_content
                ])
            ])
        )


if __name__ == "__main__":
    component = html([
        head([
            title("Hello, World!"),
            meta({"charset": "UTF-8", "name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
            link({"rel": "stylesheet", "href": "style.css"}),
            script("", {"src": "script.js"})
        ]),
        body([
            MyComponent(
                p("Hello, World 3!"), 
                p("Hello, World 4!"), 
                {"id": "custom-component1"}
            ),
            MyComponent(
                p("Hello, World 5!"), 
                p("Hello, World 6!"), 
                {"id": "custom-component2"}
            ),
            script("console.log('Hello, World!');")
        ])
    ])

    print(format_html(component))  # Output: "Hello, World!

    print(format_html([
        MyComponent(p("Hello, World 3!"), p("Hello, World 4!"), {"id": "custom-component1"}),
        MyComponent(p("Hello, World 5!"), p("Hello, World 6!"), {"id": "custom-component2"})
    ]))  # Output: "Hello, World!

    index_template = IndexTemplate(
        MyComponent(p("Hello, World 3!"), p("Hello, World 4!"), {"id": "custom-component1"})
    )
    print(format_html(index_template))  # Output: "Hello, World!