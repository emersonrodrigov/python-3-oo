import datetime

class Data:

    def __init__(self, dia,mes,ano):
        self.data = datetime.date(ano,mes,dia)


    def formatada(self):
        data_str = self.data.strftime('%d/%m/%Y')
        print(data_str)
        return  self.data.strftime('%d/%m/%Y')