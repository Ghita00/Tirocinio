class Auxcarrello():
    quantità = 0
    totale = 0

class Active():
    #index, shop, blog, contact
    pagine = [1, 0, 0, 0]

    def disattiva(self, active):
        for i in range(4):
            self.pagine[i] = 0
        self.pagine[active] = 1

pages = Active()