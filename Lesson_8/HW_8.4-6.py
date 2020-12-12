"""
Tasks 8.4-8.6 Сам до конца неразобрался. Немного модифицировал то, что сделалДмитрий Вилесов
"""
class Sklad:
    __sklad = {}

    def put_in(self, device):
        device.department = ''
        device_type = device.device_type
        _ = self.__sklad.get(device_type) or []
        _.append(device)
        self.__sklad[device_type] = _

    def get_out(self, device_type, count, otdel):
        if not type(count) is int:
            raise ValueError('Неправильный формат')
        _ = self.__sklad.get(device_type)
        if _ is None:
            raise KeyError('Техника не найдена')
        res_list = []
        for i in range(count):
            try:
                device = _.pop()
            except IndexError as err:
                print(err)
                break
            device.otdel = otdel
            res_list.append(device)
        return res_list

    def __str__(self):
        return str(self.__sklad)

class Orgtechnics:
    name = str
    model = str
    price = int
    otdel = ''

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def __str__(self):
        return f'"{self.dev_type}: {self.name}, {self.model}, {self.price} рублей."'

    @classmethod
    def dev_type(cls):
        return cls.__name__

class Printer(Orgtechnics):
    def __init__(self, device_type, name, model, format, price):
        super().__init__(name, model, price)
        if not type(format) is str:
            raise ValueError('Неправильный формат размера.')
        self.format = format
        self.device_type = device_type

class Scaner(Orgtechnics):
    def __init__(self, device_type, name, model, dpi, price):
        super().__init__(name, model, price)
        if not type(dpi) is int:
            raise ValueError('Неправильный формат разрешения.')
        self.dpi = dpi
        self.device_type = device_type

class Xerox(Orgtechnics):
    def __init__(self, device_type, name, model, wifi, price):
        super().__init__(name, model, price)
        if not type(wifi) is bool:
            raise ValueError('Неправильно указано наличие/отсутствие WiFi.')
        wifi = bool
        self.device_type = device_type

# добавление единицы техники
p = Printer('Принтер', 'HP', 'Laser 135r', 'A4', 10000)
s = Scaner('Сканер', 'Canon', 'DR-C240', 600, 20000)
x = Xerox('Ксерокс', 'Brother', 'DCP-L2500', True, 15000)
print(p)
sk = Sklad()
sk.put_in(p)
sk.put_in(s)
sk.put_in(x)
sk.get_out('Сканер', 1, 'Бухгалтерия')
print(sk)