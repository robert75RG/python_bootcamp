'''

Zadanie #11
Zaimplementuj klasy odpowiedzialne za tworzenie dokumenty w
składni MarkDown. Stwórz klase bazowa Element zawierajaca
podstawowa implementacje metody render() oraz kilka jej klas
pochodnych. Stwórz klase Document umozliwiajaca wyrendorowanie
dodanych elementów.
Przykład uzycia:
>>> document = Document()
>>> document.add_element(HeaderElement('Header'))
>>> document.add_element(LinkElement('ABC', 'abc.com'))
>>> document.add_element(Element('Simple'))
>>> document.render()
Header
======
(ABC)[http://abc.com]
Simple
'''


class Document():
    def __init__(self):
        self.conteiner = []

    def add_element(self, element):
        self.conteiner.append(element)
        
class Element():
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


def test_document():
    doc = Document()
    assert doc.conteiner == []
    doc.add_element('TRZY')
    assert doc.conteiner == ['TRZY']
    
def test_element():
    element = Element('Ala ma kota')
    assert element.text == 'Ala ma kota'
    assert element.render() == 'Ala ma kota'