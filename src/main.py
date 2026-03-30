import json
import os

class UIObject:
    """Класс графического объекта игрового интерфейса"""
    def __init__(self, obj_id, obj_type, x, y):
        self.id = obj_id
        self.type = obj_type
        self.x = x
        self.y = y

    def to_dict(self):
        return {"id": self.id, "type": self.type, "x": self.x, "y": self.y}

class UIEditor:
    """Логика редактора: Создание, Редактирование, Удаление (CRUD)"""
    def __init__(self):
        self.objects = []
        self.save_file = "ui_layout.json"

    def add_object(self, obj_type, x, y):
        obj_id = len(self.objects) + 1
        new_obj = UIObject(obj_id, obj_type, x, y)
        self.objects.append(new_obj)
        print(f"[Editor] Добавлен объект: {obj_type} (ID: {obj_id})")

    def delete_object(self, obj_id):
        self.objects = [obj for obj in self.objects if obj.id != obj_id]
        print(f"[Editor] Объект ID {obj_id} удален.")

    def save_to_file(self):
        """Реализация функции сохранения в файл (задание ПМ.04)"""
        data = [obj.to_dict() for obj in self.objects]
        with open(self.save_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"[Storage] Конфигурация сохранена в {self.save_file}")

    def load_from_file(self):
        """Реализация функции загрузки из файла (задание ПМ.04)"""
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.objects = [UIObject(**item) for item in data]
            print(f"[Storage] Загружено объектов: {len(self.objects)}")
        else:
            print("[Storage] Файл сохранения не найден.")

# Имитация работы приложения
if __name__ == "__main__":
    editor = UIEditor()
    
    # 1. Тест создания объектов
    editor.add_object("Button_Start", x=100, y=200)
    editor.add_object("Health_Bar", x=10, y=10)
    
    # 2. Тест сохранения
    editor.save_to_file()
    
    # 3. Тест удаления и загрузки
    editor.delete_object(1)
    print("Состояние после удаления:", [o.id for o in editor.objects])
    
    editor.load_from_file()
    print("Состояние после загрузки из файла:", [o.id for o in editor.objects])
