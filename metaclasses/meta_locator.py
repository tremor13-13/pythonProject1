class MetaLocator(type):
    def __new__(cls, name, bases, attrs):
        # перебираем все атрибуты, переданные в класс
        for key, value in attrs.items():
            if isinstance(value, str):
                if value.startswith("//") or value.startswith(".//") or value.startswith("(//"):
                # преобразуем строку в локатор, если она начинается с этого "//"
        return type.__new__(cls, name, bases, attrs)