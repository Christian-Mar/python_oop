from orange import Orange
from basket import Basket

def main():
    pass

if __name__ == '__main__':
    basket_rouge = Basket() # basket_rouge is een instance van de klasse Basket - instantie met ronde haken
    o = Orange() 

    basket_rouge.content.append(o)

    basket_rouge.put_in_basket(o)