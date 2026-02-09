from __future__ import annotations
from datetime import date


class Orange: 
    weight: float = 0.5 # men kan ook weigh definiëren zonder al een waarde toe te kennen
    orchard: str = ""
    date_picked: date = date.today()
    is_in_basket: Basket

class Apple:
    pass

class Basket: 
    location: str = ""
    content: list[Orange | Apple] =[]
