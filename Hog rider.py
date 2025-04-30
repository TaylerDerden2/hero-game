class Party:
    def __init__(self,init_name):
        self.name = init_name

    #def zakup(self):
    #    print("Ми закуптли їжу сік 'Садочок' та гобліна діджея ")

    def decor_party(func_to_decor):
        def wrapper(*args,**kwargs):
            print("Ми закуптли їжу,сік 'Садочок' та гобліна діджея ")
            res = func_to_decor(*args,**kwargs)
            print("Ми помили дім та заплатили за їжу ")
        return wrapper

    @decor_party
    def party(self):
        print(f"Нашу вечірку приймає{self.name}")
    @decor_party
    def no_party(self):
        print(f"Несподівно до {self.name} додому прийшла мама вечірки не буде ")

user_name = input("До кого йдемо на білу вечірку ----->")
user_party = Party(user_name)


x = input("Чи відбулася вечірка (Y/N)?")
if x[0].upper() == "Y":
    user_party.party()
else:
    user_party.no_party()
