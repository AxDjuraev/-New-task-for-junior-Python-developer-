import os

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

def inputWithoutWhiteSpaces(prompt):
  userInput = input(prompt)
  if userInput == "" or userInput.strip() == "":
    raise ValueError("Пустое поле.")
  return userInput.strip()

def getActionFromUser(market0):
  actions = {
    "Добавить в список":        lambda: market0.addNewItem(inputWithoutWhiteSpaces("Наименование: "), inputWithoutWhiteSpaces("Цена: ")),
    "Изменить запись в списке": lambda: market0.changeItemByOldName(inputWithoutWhiteSpaces("Наименование: "), inputWithoutWhiteSpaces("Новое наименование: "), inputWithoutWhiteSpaces("Цена: ")),
    "Удалить из списка":        lambda: market0.deleteItemByName(inputWithoutWhiteSpaces("Наименование: ")),
    "Вычесть общую сумму":      lambda: f'Общая сумма: {market0.getItemsPriceSum()}'
  }  
  for actionIndex in range(len(actions)):
    actionName = list(actions.keys())[actionIndex]
    print(f'{(actionIndex+1)}.{actionName}')
  actionIndex = int(inputWithoutWhiteSpaces("Номер действия: "))-1
  if actionIndex < 0 or actionIndex > len(actions)-1:
    raise ValueError("Номер действия виходить за гран")
  result = list(actions.values())[actionIndex].__call__()
  if result:
    print(result)
  
if __name__ == "__main__":
  try:
    file_name = inputWithoutWhiteSpaces("Имя файла: ").strip()
    market1 = market()
    if not os.path.exists(file_name):
      with open(file_name, "w") as file_:
        file_.write(" ")
    with open(file_name,"r") as file_:
      for line in file_:
        line = line.split("—")
        if len(line) != 2:
          continue
        line = list(map(lambda item: item.strip(), line))
        (name, price) = (line[0], line[1])
        obj = object_(name, float(price))
        market1.addItem(obj)
    getActionFromUser(market1)
    market1.writeItems2File(file_name)
  except Exception as exception:
    print(f'Error: {str(exception)}')

