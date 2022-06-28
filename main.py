class object_:
  name: str
  price: float
  def __init__(self, name, price):
    self.name = name
    self.price = price
  def getName(self):
    return self.name
  def getPrice(self):
    return self.price
  def changeName(self, name):
    if name == None or name.strip() == '':
      raise "Incorrect format of name"
    self.name = name
  def changePrice(self, price):
    if price < 0:
      raise "Incorrect format of price"
    self.price = pricex