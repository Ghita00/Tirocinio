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

class SliderHelp():
    #mex(0), ordini_r(1), ordini_e(2), fatture_a(3), fatture_v(4), ddt(5), scontrini(6)
    sliders = [0,0,0,0,0,0,0]

    def aggiorna(self, i, value):
        self.sliders[i] += int(value)
        if self.sliders[i] < 0:
            self.sliders[i] = 0

    def endSlied(self, i):
        return 10*(self.sliders[i] + 1)
help = SliderHelp()