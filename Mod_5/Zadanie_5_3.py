# Wizytówka
print('\n')
class BasicContact():
    """Wizytówka prywatna"""
    
    def __init__(self, name, forname, phone, email):
        """Atrybuty opisujące wizytówkę prywatną"""
        self.name = name
        self.forname = forname
        self.phone = phone
        self.email = email

    def contact(self):
        """Sformułowanie wyboru wizytówki"""
        person_card = f"Wybieram numer prywatny {self.phone} i dzwonię do {self.name.title()} {self.forname.title()}."
        print(person_card)
        
    def label_length(self):
        """Wyświetlenie długości imienia i nazwiska"""
        print(f"Imię i nazwisko ma {len(self.name + self.forname)} znaków.")

class BusinessContact():
    """Wizytówka służbowa"""
    
    def __init__(self, name, forname, position, company, business_phone):
        """Atrybuty opisujące wizytówkę prywatną"""
        self.name = name
        self.forname = forname
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        """Sformułowanie wyboru wizytówki"""
        person_card = f" Wybieram numer służbowy {self.business_phone} i dzwonię do {self.name.title()} {self.forname.title()}."
        print(person_card)
    
    def label_length(self):
        """Wyświetlenie długości imienia i nazwiska"""
        print(f" Imię i nazwisko ma {len(self.name + self.forname)} znaków.")

person_basic = BasicContact('Patrycja', 'Borkowska', +489991435, 'PatrycjaBorkowska@rhyta.com')
person_basic.contact()
person_basic.label_length()

person_business= BusinessContact('Patrycja', 'Borkowska', 'Bartender', 'Magic Gray', +485135904560)
person_business.contact()
person_business.label_length()


