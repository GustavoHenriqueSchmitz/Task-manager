import datetime
class VerificaData:

    def __init__(self, datahora=f'{datetime.datetime.now()}'):
        self.__datahorajun = f'{datahora}'
        self._datahorasep = {'ano': '', 'mes': '', 'dia': '', 'hora': '', 'minuto': '', 'segundo': ''}


    @property
    def __datahorajun(self):
        return self._datahorajun

    @__datahorajun.setter
    def __datahorajun(self, dhj):
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
    def _datahorasep(self):
        return self.datahorasep

    @_datahorasep.setter
    def _datahorasep(self, dhs):
        contnum = 0
        for k in dhs.keys():
            date = ''
            for c, v in enumerate(self.__datahorajun):
                if c < contnum:
                    continue
                if v.isnumeric():
                    date += v
                    contnum += 1
                else:
                    contnum += 1
                    break
            dhs[k] = date
        self.datahorasep = dhs


    def retorna_data_hora_sep(self):
        return self._datahorasep


    @staticmethod
    def retorna_data_hora_atual():
        datatemp = f'{datetime.datetime.now()}'
        dataperm = ''
        for c, v in enumerate(datatemp):
            if c == 18:
                break
            dataperm += v
        return f'{dataperm}'

    @staticmethod
    def mostra_data_hora_atual():
        datatemp = f'{datetime.datetime.now()}'
        dataperm = ''
        for c, v in enumerate(datatemp):
            if c == 18:
                break
            dataperm += v
        print(f'{dataperm}')

    @staticmethod
    def mostra_ano_atual():
        print(f'{datetime.date.today().strftime("%Y")}')

    @staticmethod
    def retorna_ano_atual():
        return f'{datetime.date.today().strftime("%Y")}'

    @staticmethod
    def mostra_mes_atual():
        print(f'{datetime.date.today().strftime("%m")}')

    @staticmethod
    def retorna_mes_atual():
        return datetime.date.today().strftime("%m")

    @staticmethod
    def mostra_dia_atual():
        print(f'{datetime.date.today().strftime("%d")}')

    @staticmethod
    def retorna_dia_atual():
        return datetime.date.today().strftime("%d")

    @staticmethod
    def mostra_hora_atual():
        print(f'{datetime.datetime.now().strftime("%H")}')

    @staticmethod
    def retorna_hora_atual():
        return datetime.datetime.now().strftime("%H")
