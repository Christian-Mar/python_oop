from orange import Orange
from apple import Apple

class Basket: 
    location: str = ""
    content: list[Orange | Apple] =[]

    #def 