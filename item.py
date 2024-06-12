import csv

class Item:
  pay_rate = 0.8 # The pay rate after 20% discount
  all = []

  def __init__(self, name: str, price: float, quantity=0) -> None:
    # Run validations
    assert price >= 0, f"Price {price} is not greater than zero"
    assert quantity >= 0, f"Price {quantity} is not greater than zero"
    
    # Assign to self object
    self.__name = name
    self.__price = price
    self.quantity = quantity

    # Append to class level array
    Item.all.append(self)

  @property
  def name(self):
    return self.__name
  
  @name.setter
  def name(self, value):
    self.__name = value

  @property
  def price(self):
    return self.__price
  
  @price.setter
  def price(self, value):
    self.__price = value

  
  def calculate_total_price(self) -> int:
    return self.price * self.quantity
  
  def apply_discount(self) -> None:
    self.price = self.price * self.pay_rate # Item.pay_rate for Class level
  
  
  def __prepare_body(self, sender) -> str:
    return f"""
    Hello Someone.
    We have {self.name} {self.quantity} times.
    Regards, {sender}
    """
  
  def send_email(self, sender):
    return self.__prepare_body(sender)

  @classmethod
  def instantiate_from_csv(cls):
    with open("sample.csv", 'r') as f:
      reader = csv.DictReader(f)
      items = list(reader)
    
    for item in items:
      Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = float(item.get('quantity'))
      )
  
  @staticmethod
  def is_integer(num):
    if isinstance(num, float):
      return num.is_integer()
    elif isinstance(num, int):
      return True
    else:
      return False

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}('{self.name}', '{self.price}', '{self.quantity}')"