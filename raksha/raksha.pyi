from __future__ import annotations

class Element: ...

class Parser:
    @staticmethod
    def parse(input: str) -> Element | None: ...
    @staticmethod
    def inspect(el: Element) -> str: ...