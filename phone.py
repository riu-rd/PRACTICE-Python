from item import Item

class Phone(Item):
  def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
    super().__init__(name, price, quantity)

    assert broken_phones >= 0, f"{broken_phones} is less than 0"
    self.broken_phones = broken_phones