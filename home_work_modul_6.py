from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Имя - обязательное поле")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("В номере телефона должно содержаться 10 цифр")   
        super().__init__(value)   

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        if type(phone) == str:
            phone = Phone(phone)
        self.phones.append(phone)
        
    def remove_phone(self, phone):
        phone_to_delete = self.find_phone(phone)
        if phone_to_delete:
            self.phones.remove(phone_to_delete)
        else:
            raise ValueError("Номер не найден")    
            
    def edit_phone(self, old_phone, new_phone):
        if type(new_phone) == str:
                new_phone = Phone(new_phone)
        phone_to_change = self.find_phone(old_phone)
        if phone_to_change:
            self.remove_phone(old_phone)
            self.add_phone(new_phone) 
        else:
            raise ValueError("Этого номера нет в телефонной книге")
        
    def find_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                return el
        return None           

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Контакт не найден")    
    
    def __str__(self):
        return "\n".join(f"{name}: {record}" for name, record in self.data.items())           