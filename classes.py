# class Dog:
#     def __init__(self, nume_caine, rasa_caine, varsta_caine, are_stapan):
#         self.name = nume_caine
#         self.race = rasa_caine
#         self.age = varsta_caine
#         self.are_stapan = are_stapan
        
#     def bark(self):
#         print("Ham Ham")

#     def speak(self):
#         print(f"sunt {self.name}, am varsta de {self.age} ani, sunt rasa {self.race} si {"am" if self.are_stapan  else "n-am"} stapan")


# caine1 = Dog("Bolt", "White Shpeherd", 3, False)
# caine2 = Dog("Sirius", "actually a cat", 1, True)

# caine1.speak()
# caine2.speak()

# clasa care sa se numeasca triunghi, are o metoda perimetrul
# from math import sqrt


# class Forma:
#     def __init__(self, laturi):
#         self.laturi = laturi

#     def perimetru(self):
#         return sum(self.laturi)



# class Triunghi(Forma):
#     def __init__(self, lat1, lat2, lat3):
#         self.lat1 = lat1
#         self.lat2 = lat2
#         self.lat3 = lat3

#     def perimetru(self):
#         return self.lat1 + self.lat2 + self.lat3
    
#     def get_catete(self):
#         ipotenuza = max(self.lat1, self.lat2, self.lat3)
#         laturi = [self.lat1, self.lat2, self.lat3]
#         laturi.remove(ipotenuza)
#         cateta1, cateta2 = laturi
#         return cateta1, cateta2

#     def este_dreptunghic(self):
#         ipotenuza = max(self.lat1, self.lat2, self.lat3)
#         cateta1, cateta2 = self.get_catete()

#         return ipotenuza**2 == cateta1**2 + cateta2**2

#     def este_echilateral(self):
#         return self.lat1 == self.lat2 == self.lat3

#     def aria(self):
#         # dreptunghic
#         if self.este_dreptunghic():
#             c1, c2 = self.get_catete()
#             print(c1, c2)
#             return c1 * c2 / 2

#         # echilateral
#         elif self.este_echilateral():
#             return (self.lat1**2) * sqrt(3) / 4

#         # oarecare
#         else:
#             p = self.perimetru() / 2
#             rez = p*(p-self.lat1)*(p-self.lat2)*(p-self.lat3)
#             return sqrt(rez)


# t = Triunghi(12, 11, 20)
# print(t.aria())




class Car:
    def __init__(self, km, an, nr_locuri):
        self.km = km
        self.an = an
        self.nr_locuri = nr_locuri

    def da_in_spate_kilometraju(self, km):
        self.km -= km

    def print_km(self):
        print(self.km)


class Audi(Car):
    def __init__(self, km, an, nr_locuri, pret):
        super().__init__(km, an, nr_locuri)
        self.pret = pret


class Mercedes(Car):
    def __init__(self, km, an, nr_locuri, cai):
        super().__init__(km, an, nr_locuri)
        self.cai = cai


masina1 = Audi(100000, 2009, 5, 10000)
masina2 = Mercedes(300000, 2010, 5, 300)


masina1.print_km()
masina1.da_in_spate_kilometraju(12131)
masina1.print_km()