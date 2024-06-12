from item import Item
from phone import Phone

def main():
  Item.instantiate_from_csv()
  print("- - - - - - - -") 
  print("All Item instances:\n", Item.all)
  print("- - - - - - - -")
  print("Is Integer Function:\n", Item.is_integer(7.5))
  print("- - - - - - - -")
  print("- - - - - - - -")
  phone1 = Phone("Samsung", 500, 5, 1)
  print(Item.all)
  print("- - - - - - - -")
  print("- - - - - - - -")
  item1 = Item("MyItem", 750)
  print(item1.name)
  item1.name = "OtherItem"
  print(item1.name)
  print("- - - ENCAPSULATION - - -")
  # Remove Direct Attribute Access through getters/setters
  print(item1.price)
  item1.price = 900
  print(item1.price)
  print("- - - ABSTRACTION - - -")
  # Do not show unnecessary details to users / instances
  # Convert methods to private 
  #print(item1.send_email("Darius"))
  print(item1.send_email("Darius"))
  print("- - - INHERITANCE - - -")
  # Phone inherits Item attributes
  print("- - - POLYMORPHISM - - -")
  # Have different scenarios with the exact same entity
  # Sample: len() function

if __name__ == '__main__':
  main()