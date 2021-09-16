from faker import Faker
fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, private_phone,email):
        self.first_name= fake.first_name()
        self.last_name = fake.last_name()
        self.private_phone = fake.phone_number()
        self.email = fake.email()
        self._label_length = len(self.first_name) + len(self.last_name)
    def ___repr__(self):
        return f"BaseContact(first_name={self.first_name},last_name={self.last_name}, private_phone={self.privat_phone}, email= {self.email}"
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.private_phone} {self.email}"
    def contact(self):
        return f"Wybieram numer prywatny {self.private_phone} i dzwonię do {self.first_name} {self.last_name}"
    @property
    def label_length(self):
        return f"Suma liter imienia i naziwska to: {self._label_length}"

class BusinessContact(BaseContact):
    def __init__(self, position, company_name, business_phone, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.position = fake.job()
        self.company_name = fake.company()
        self.business_phone = fake.phone_number()
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.private_phone} {self.email} {self.position} {self.company_name} {self.business_phone}"
    def contact(self):
        return f"Wybieram numer służbowy {self.business_phone} i dzwonię do {self.first_name} {self.last_name}"


def create_contacts(card_type, quantity):
   if card_type == "BaseContact":
      for _ in range(quantity):
          print(BaseContact("first_name", "last_name", "private_phone","email"))
      return ""
      
   elif card_type == "BusinessContact":
      for _ in range(quantity):
          print(BusinessContact("position", "company_name", "business_phone","first_name", "last_name", "private_phone","email"))
      return ""


print(create_contacts("BaseContact", 4))
print(create_contacts("BusinessContact", 3))

Private_p = BaseContact("first_name", "last_name", "private_phone","email")
Business_p = BusinessContact("position", "company_name", "business_phone","first_name", "last_name", "private_phone","email")

print(Private_p.contact())
print(Private_p.label_length)
print(Business_p.contact())
print(Business_p.label_length)
