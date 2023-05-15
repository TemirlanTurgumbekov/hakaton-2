from views import CreateMixin, ListingMixin, RetriaveMixin, UpdateMixin, DeleteMixin
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
import os
import json

class Cars(CreateMixin, ListingMixin, RetriaveMixin, UpdateMixin, DeleteMixin):
    def save(self):
        try:
            with open('data.json', 'w') as file:
                json.dump(self.objects, file, ensure_ascii=False, indent=4)
            return 'Данные успешно сохранены!'
        except Exception:
            return 'Не удалось сохранить данные!'
    

def add_car():
    os.system('cls||clear')
    kuzov = ['Седан', 'Универсал', 'Купе', 'Хетчбек', 'Минивен', 'Внедорожник', 'Пикап']
    print('Добавление новой машины: ')
    marka = input('[1] - Марка: ')
    model = input('[2] - Модель: ')
    data_of_issue = input('[3] - Дата выпуска: ')
    engine_capacity = input('[4] - Объем двигателя: ')
    color = input('[5] Цвет: ')
    print('[6] Тип кузова:\n')
    body_type = TerminalMenu(kuzov)
    kuzov_entry_index = body_type.show()
    mileage = input('[7] Пробег: ')
    price = input('[8] Цена: ')
        
    return {'marka': marka, 'model': model, 'date_of_issue': data_of_issue, 'engine_capacity': engine_capacity, 'color': color, 'body_type':kuzov_entry_index, 'mileage':mileage, 'price': price}

def update_car():
    fields = ['marka', 'model', 'date_of_issue', 'endine_capacity', 'color', 'body_type', 'mileage', 'price']
    print('Выберите поле для изменения:')
    field_menu = TerminalMenu(fields)
    field_index = field_menu.show()
    
    return fields[field_index]
    
def main():
    obj = Cars()

    while True:
        os.system('cls||clear')
        options = ['[1] - Добавить машину',
                '[2] - Вывести список машин',
                '[3] - Поиск машины по id', 
                '[4] - Обновить информацию о машине', 
                '[5] - Удалить запись',
                '[6] - Сохранить в БД',
                '[X] - Выход'
                ]
        menu = TerminalMenu(options)
        menu_entry_index = menu.show()
        print(options[menu_entry_index])
        
        if options[menu_entry_index] == '[1] - Добавить машину':
            car = add_car()
            print(obj.post(car))
            
            input('\n\nДля продолжения нажмите на любую клавищу...')
            
        elif options[menu_entry_index] == '[2] - Вывести список машин':
            result = obj.list_()
            
            if type(result) == list:
                mytable = PrettyTable()
                mytable.field_names = ['id', 'Марка', 'Модель', 'Дата выпуска', 'Объем двигателя', 'Цвет', 'Тип кузова', 'Пробег', 'Цена']
                
                for i in result:
                    mytable.add_row(i.values())
                print(mytable)
                
            else:
                print(result)
                
            input('\n\nДля продолжения нажмите на любую клавищу...')
            
            
            
        elif options[menu_entry_index] == '[3] - Поиск машины по id':
            id = int(input('Введите id машины:'))
            print(obj.retriave(id))
            
            input('\n\nДля продолжения нажмите на любую клавищу...')
            
        elif options[menu_entry_index] == '[4] - Обновить информацию о машине':
            id = int(input('Введите id машины:'))
            field = update_car()

            new_info = input('Введите новую информацию: ')
            print(obj.patch(id, field, new_info))
            
            input('\n\nДля продолжения нажмите на любую клавищу...')
        
        elif options[menu_entry_index] == '[5] - Удалить запись':
            id = int(input('Введите id машины: '))
            print(obj.delete_(id))
            
            input('\n\nДля продолжения нажмите на любую клавищу...')
        
        elif options[menu_entry_index] == '[6] - Сохранить в БД':
            print(obj.save())
            input('\n\nДля продолжения нажмите на любую клавищу...')
            
        elif options[menu_entry_index] == '[X] - Выход':
            print('Программа завершила работу!')
            break
        
if __name__ == '__main__':
    main()
    


