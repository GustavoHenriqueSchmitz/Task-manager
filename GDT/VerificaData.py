import datetime
class VerificaData:

    def __init__(self, datahora=f'{datetime.datetime.now()}'):
        self.datahorajun = f'{datahora}'
        self.datahorasep = {'ano': '', 'mes': '', 'dia': '', 'hora': '', 'minuto': '', 'segundo': ''}


    @property
    def datahorajun(self):
        return self._datahorajun

    @datahorajun.setter
    def datahorajun(self, dhj):
        fordatahorajun = ''
        fordatahorajunperm = ''
        contnums = 0
        for v in dhj:
            if v.isnumeric():
                fordatahorajun += f'{v}'
        for v in fordatahorajun:
            if v.isnumeric:
                fordatahorajunperm += f'{v}'
                contnums += 1
            if contnums == 4:
                fordatahorajunperm += ' '
                contnums = 2
        self._datahorajun = fordatahorajunperm

    @property
    def datahorasep(self):
        return self._datahorasep

    @datahorasep.setter
    def datahorasep(self, dhs):
        contnum = 0
        for k in dhs.keys():
            date = ''
            for c, v in enumerate(self.datahorajun):
                if c < contnum:
                    continue
                if v.isnumeric():
                    date += v
                    contnum += 1
                else:
                    contnum += 1
                    break
            dhs[k] = date
        self._datahorasep = dhs


    def retorna_data_hora_sep(self):
        return self.datahorasep

    @staticmethod
    def retorna_data_hora_atual():
        return datetime.datetime.now()

    @staticmethod
    def mostra_data_hora_atual():
        print(f'{datetime.datetime.now()}')

    @staticmethod
    def mostra_ano_atual():
        print(f'{datetime.datetime.now()}')

    @staticmethod
    def retorna_ano_atual():
        return datetime.datetime.year

print(VerificaData.mostra_ano_atual())
