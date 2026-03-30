import xml.etree.ElementTree as ET
import json

class UIValidator:
    """Модуль проверки корректности графических объектов для мобильных экранов"""
    
    def __init__(self, screen_width=1080, screen_height=1920):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def is_within_bounds(self, obj):
        """Проверка: не выходит ли объект за границы экрана смартфона"""
        if 0 <= obj['x'] <= self.screen_width and 0 <= obj['y'] <= self.screen_height:
            return True
        return False

    def export_to_xml(self, objects, filename="ui_layout.xml"):
        """Экспорт макета в XML (часто используется в Android разработке)"""
        root = ET.Element("CommonUI")
        
        for obj in objects:
            if self.is_within_bounds(obj):
                element = ET.SubElement(root, "Widget")
                element.set("id", str(obj['id']))
                element.set("type", obj['type'])
                element.set("position", f"{obj['x']},{obj['y']}")
            else:
                print(f"[Warning] Объект {obj['id']} вне экрана! Пропущен при экспорте.")

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        print(f"[Export] Данные успешно сконвертированы в {filename}")

# Пример интеграции с основным кодом
if __name__ == "__main__":
    # Представим данные, которые мы создали в главном модуле
    sample_objects = [
        {"id": 1, "type": "Button_Fire", "x": 500, "y": 1000},
        {"id": 2, "type": "Health_Bar", "x": 2000, "y": 50},  # Ошибка: x > 1080
    ]

    validator = UIValidator()
    print("--- Запуск проверки макета интерфейса ---")
    validator.export_to_xml(sample_objects)
