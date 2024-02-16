from faker import Faker
fake = Faker()


class BaseContact:

    def __init__(self, name, second_name, home_number, email):
        self.name = name
        self.second_name = second_name
        self.home_number = home_number
        self.email = email

    def __str__(self):
        return f'{self.name} {self.second_name} {self.home_number} {self.email}'

    def contact(self):
        return f'Wybieram numer {self.home_number} i dzwonię do {self.name} {self.second_name}'

    @property
    def label_length(self):
        length = len(self.name) + 1 + len(self.second_name)
        return length

class BusinessContact(BaseContact):
    def __init__(self, company, job, business_number, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.business_number = business_number
        self.company = company
        self.job = job

    def contact(self):
        return f'Wybieram numer {self.business_number} i dzwonię do {self.name} {self.second_name}'
    
    def __str__(self):
        return f'{self.name} {self.second_name} {self.company} {self.job} {self.business_number} {self.email}'


person1 = BaseContact(name="Joel",
                    second_name="Nick",
                    home_number="+0487536584",
                    email="jnick@apple.com")

person2 = BusinessContact(name="Juanita",
                    second_name="Smith",
                    company="Crafts Canada",
                    job="nurse",
                    home_number = '+0485855555',
                    business_number = '+004826568888',
                    email="JuanitaMShinn@rhyta.com")



def create_contacts(card_class, quantity):
    contact_list = []
    for card in range(quantity):
        contact_name = fake.first_name()
        contact_sec_name = fake.last_name()
        contact_bnumber = fake.phone_number()
        contact_hnumber = fake.phone_number()
        contact_email = fake.email()
        contact_job = fake.job()
        contact_company = fake.company()

        if card_class == 'base':
            card = BaseContact(name = contact_name,
                               second_name = contact_sec_name,
                               home_number = contact_hnumber,
                               email = contact_email)
            
        elif card_class == 'business':
            card = BusinessContact(name = contact_name,
                                   second_name = contact_sec_name,
                                   home_number = contact_hnumber,
                                   email = contact_email,
                                   business_number = contact_bnumber, 
                                   company = contact_company,
                                   job = contact_job)
            
        contact_list.append(print(card))
        

create_contacts('base', 5)
    
