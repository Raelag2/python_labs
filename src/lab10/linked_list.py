class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self) -> str:
        return f"Node({self.value})"
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None # start of a linked list
        self._size = 0


    def __len__(self):
        return self._size 
    
    def append(self, value):
        new_node = Node(value)          # 1. Создаем новый узел
        if self.head is None:           # 2. Если список пуст
            self.head = new_node        #    новый узел становится головой
        else:
            current = self.head         # 3. Ищем конец списка
            while current.next is not None:
                current = current.next
            current.next = new_node     # 4. Цепляем новый узел в конец
        
        self._size += 1                 # 5. Увеличиваем счетчик

    def prepend(self, value):
        new_node = Node(value, next=self.head)  # 1. Новый узел указывает на старую голову
        self.head = new_node                    # 2. Новая голова = новый узел
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:          # 1. Проверка индекса
            raise IndexError(f"Incorrect index {idx}")
        
        if idx == 0:                             # 2. Вставка в начало
            self.prepend(value)
            return
        elif idx == self._size:
            self.append(value)
        new_node = Node(value)      # Создаем новый узел
        current = self.head         # Начинаем с головы списка
        for _ in range(idx - 1):    
            current = current.next  # Переходим к следующему узлу
        new_node.next = current.next  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1

    def remove_at(self, idx):
        # 1. Проверка: индекс должен быть от 0 до (размер-1)
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} goes beyond list limits.")
        
        # 2. Особый случай: удаляем первый элемент (индекс 0)
        if idx == 0:
            self.head = self.head.next  # голова теперь следующий элемент
            self._size -= 1             # уменьшаем размер
            return                      # выходим из функции
        
        # 3. Общий случай: удаляем не первый элемент
        prev = None         # будет хранить предыдущий узел
        current = self.head # начинаем с головы
        position = 0        # текущая позиция
        
        # 4. Ищем узел для удаления
        while current and position < idx:
            prev = current          # запоминаем предыдущий узел
            current = current.next  # переходим к следующему
            position += 1           # увеличиваем счетчик позиции
        
        # 5. Удаляем узел (пропускаем его)
        prev.next = current.next  # предыдущий узел теперь указывает НА следующий после удаляемого
        
        # 6. Уменьшаем размер списка
        self._size -= 1
            
    def remove_value(self, value):
        # 1. Проверка: если список пуст
        if self.head is None: 
            return  # просто выходим, ничего не делаем
        
        # 2. Особый случай: удаляем первый элемент (голову)
        if self.head.value == value:
            self.head = self.head.next  # голова теперь следующий элемент
            self._size -= 1             # уменьшаем размер
            return      
        
         # 3. Общий случай: ищем значение в остальной части списка
        prev = None           # будет хранить предыдущий узел
        current = self.head   # начинаем с головы
        
        # 4. Ищем узел с нужным значением
        while current is not None: 
            if current.value == value:  # нашли!
                prev.next = current.next  # пропускаем найденный узел
                self._size -= 1           # уменьшаем размер
                break                     # выходим из цикла (удалили первый найденный)
            # не нашли на этом шаге, идем дальше
            prev = current          # запоминаем текущий как предыдущий
            current = current.next  # переходим к следующему

        def __repr__(self) -> str:
            values = list(self)  # 1. Превращаем список в обычный Python list
            return f"SinglyLinkedList({values})"  # 2. Форматируем строку

        def visual_repr(self) -> str:
            parts = []  # 1. Создаем пустой список для частей
            current = self.head  # 2. Начинаем с головы
            
            while current is not None:  # 3. Идем по всем узлам
                parts.append(f"[{current.value}]")  # 4. Добавляем узел
                current = current.next  # 5. Переходим к следующему
            
            parts.append("None")  # 6. Добавляем None в конец
            return " -> ".join(parts)  # 7. Соединяем стрелочками
        
sll = SinglyLinkedList()
print("\n--- Testing Singly Linked List ---")
sll.append(1)
sll.prepend(2)
sll.insert(1, 3)
print("Current state of the list:", sll)      # expected: Current state of the list: SinglyLinkedList([2, 3, 1])
sll.remove_value(3)
print("After removing value 3:", sll)         # expected: After removing value 3: SinglyLinkedList([2, 1])
sll.remove_at(0)
print("After removing at index 0:", sll)      # expected: After removing at index 0: SinglyLinkedList([1])
print("Length of the list:", len(sll))        # expected: Length of the list: 1


sll = SinglyLinkedList()
sll.append('A')
sll.append('B')
sll.append('C')
print(sll)  # expected: [A] [B] [C] -> None