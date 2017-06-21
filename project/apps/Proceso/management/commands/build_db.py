from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from apps.Proceso import models
import os
import xlrd

class Fecha:
    def __init__(self, periodo, ano):
        self.periodo = periodo
        self.ano = ano
        self.programas = []

    def __str__(self):
        return str(self.periodo) + "-" + str(self.ano)

    def __repr__(self):
        return self.__str__()




class Command(BaseCommand):

    def handle(self, *args, **options):

        matrizFechas = []


        workbook = xlrd.open_workbook(os.path.join(settings.BASE_DIR, 'PENSUM.xlsx'))
        sheet = workbook.sheet_by_name('Hoja10')


        for j in range(sheet.ncols):
            valor = sheet.cell(0, j).value
            if valor != '':
                valor = valor.split('-')
                matrizFechas.append(Fecha(valor[0], valor[1]))


        for i in range(2,(sheet.nrows)):

            for j in range(1,sheet.ncols):

                valor = sheet.cell(i,j).value
                if(valor != ""):
                    matrizFechas[j-1].programas.append(str(valor))



        for i in range(len(matrizFechas)):
            index = 0
            while index < len(matrizFechas[i].programas):

                if(str(matrizFechas[i].programas[index][0]) != '['):
                    index += 1
                if(index < len(matrizFechas[i].programas) -1 ):
                    codigo = matrizFechas[i].programas[index].strip('[').strip(']')
                    nombre = matrizFechas[i].programas[index+1]
                    periodo = matrizFechas[i].periodo
                    ano = matrizFechas[i].ano
                    programa = models.Programas.objects.create(
                        codigo_materia = codigo,
                        nombre = nombre,
                        periodo_electivo = periodo,
                        periodo_annio = ano,
                    )

                    print('{} created'.format(programa))
                    index += 4
