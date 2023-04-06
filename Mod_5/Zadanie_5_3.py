# Wizytówka
print('\n')
class BasicContact():
    """Wizytówka prywatna"""
    
    def __init__(self, name, surname, phone, email):
        """Atrybuty opisujące wizytówkę prywatną"""
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def contact(self):
        """Sformułowanie wyboru wizytówki"""
        person_card = f"Wybieram numer prywatny {self.phone} i dzwonię do {self.name.title()} {self.surname.title()}."
        print(person_card)
        
    def label_length(self):
        """Wyświetlenie długości imienia i nazwiska"""
        print(f"Imię i nazwisko ma {len(self.name + self.surname)} znaków.")

class BusinessContact():
    """Wizytówka służbowa"""
    
    def __init__(self, name, surname, position, company, business_phone):
        """Atrybuty opisujące wizytówkę prywatną"""
        self.name = name
        self.surname = surname
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        """Sformułowanie wyboru wizytówki"""
        person_card = f" Wybieram numer służbowy {self.business_phone} i dzwonię do {self.name.title()} {self.surname.title()}."
        print(person_card)
    
    def label_length(self):
        """Wyświetlenie długości imienia i nazwiska"""
        print(f" Imię i nazwisko ma {len(self.name + self.surname)} znaków.")

person_basic = BasicContact('Patrycja', 'Borkowska', +489991435, 'PatrycjaBorkowska@rhyta.com')
person_basic.contact()
person_basic.label_length()

person_business= BusinessContact('Patrycja', 'Borkowska', 'Bartender', 'Magic Gray', +485135904560)
person_business.contact()
person_business.label_length()


