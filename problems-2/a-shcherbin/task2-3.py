class Vector:
    """Вектор линейной алгебры. Реализует операции умножения на константу при записи a*V,
     где a - константа V - вектор; При записи U*V выполняет операцию скалярного произведения,
     в данном случае U,V - векторы"""

    myVector = []

    def __init__(self, iterable):
        """Создает vector из переданного iterable
        :param iterable
        """
        self.myVector = list(iterable)

    def __len__(self) -> int:
        """
        :return: Количество элементов вектора
        """
        return len(self.myVector)

    def __setitem__(self, key, value):
        """
        Устанавливает указанное значение в указанную координату
        :param key: Номер координаты в векторе >= 0
        :param value: Значение в этой координате (число)
        """
        self.myVector[key] = value

    def __add__(self, other: "Vector") -> "Vector":
        """Операция сложения векторов
        :param other: Объект этого же класса Vector
        :return: Сумма векторов линейной алгебры (объект класса Vector)
        """
        rez = Vector([])
        i = 0
        try:
            while i != len(self):
                rez.myVector.append(self.myVector[i] + other.myVector[i])
                i += 1
            return rez
        except TypeError:
            print("Некорректные параметры!")

    def __sub__(self, other):
        """Операция вычитания векторов
        :param other: Объект этого же класса Vector
        :return:
        """
        rez = Vector([])
        i = 0
        try:
            while i != len(self):
                rez.myVector.append(self.myVector[i] - other.myVector[i])
                i += 1
            return rez
        except TypeError:
            print("Некорректные параметры!")

    def __rmul__(self, other):
        """Операция умножения на константу
        :param other: Числовая константа
        :return: Вектор, умноженный на константу(в смысле линейной алгебры)
        """
        rez = Vector([])
        i = 0
        while i != len(self):
            rez.myVector.append(self.myVector[i] * other)
            i += 1
        return rez

    def __mul__(self, other):
        """Операция скалярного произведения
        :param other: Объект класса Vector
        :return: Результат скалярного произведения векторов(в смысле линейной алгебры)
        """
        if isinstance(other, Vector):
            rez = Vector([])
            i = 0
            while i != len(self):
                rez.myVector.append(self.myVector[i] * other.myVector[i])
                i += 1
            return rez

    def __eq__(self, other):
        """Проверка векторов на равенство
        :param other: Объект класса Vector
        :return: true если координаты векторов совпадают, false - иначе
        """
        return self.myVector == other.myVector;

    def __getitem__(self, item):
        """Получение элемента по индексу
        :param item: Индекс(номер координаты вектора)
        :return: Число, находящееся в векторе по данному индексу
        """
        return self.myVector[item]

    def __str__(self):
        """Перевод в строку
        :return: Строковое представление вектора
        """
        return str(self.myVector)

    def get_length(self):
        """
        Вычисляет Евклидову длину вектора
        :return: Евклидова длина вектора
        """
        res = 0
        for cord in self.myVector:
            res = res + cord ** 2
        res = res ** 0.5
        return res
