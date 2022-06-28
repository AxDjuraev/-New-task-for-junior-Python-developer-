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
    self.price = price

class market:
  def __init__(self):
    self.items = list([])
  def getItemsCount(self):
    return len(self.items)
  def getItemAt(self, index):
    try:
      return self.items[index]
    except:
      return -1
  def deleteItemAt(self, index):
    del self.items[index]
  def addItem(self, item):
    if not isinstance(item, object_):
      raise "wrong object type"
    self.items.append(item)
  def addNewItem(self, itemName, itemPrice):
    obj = object_(itemName, itemPrice)
    self.items.append(obj)
  def getItemsPriceSum(self):
    sum = 0
    for item in self.items:
      sum += item.getPrice()
    return sum
  def getItemIndexByName(self, itemName):
    for index in range(self.getItemsCount()):
      item = self.getItemAt(index)
      if item.name.lower() != itemName.lower():
        continue
      return index
    raise ValueError("Наименование не найдено")
  def changeItemByOldName(self, oldName, newName, price):
    itemIndex = self.getItemIndexByName(oldName)
    item = self.items[itemIndex]
    item.name = newName
    item.price = price
  def deleteItemByName(self, name):
    itemIndex = self.getItemIndexByName(name)
    del self.items[itemIndex]
  def writeItems2File(self, file_name):
    newLineSymbol = '\n'
    content = ''
    for item in self.items:
      content += f'{item.name} — {item.price}{newLineSymbol}'
    with open(file_name, 'w') as file_:
      file_.write(content)
  def printItems(self):
    for index in range(self.getItemsCount()):
      item = self.getItemAt(index)
      print(item.getName(), item.getPrice())


