import xlwt
from apps.overtime.models import OverTime
import csv
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io
from apps.employees.models import Employee
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
# Create your views here.


def report_employees(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="relatório.pdf"'
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(200, 810, "Relatórios de Funcionários.")
    company = request.user.employee.company
    employees = Employee.objects.filter(company=company)
    y = 790

    for employee in employees:
        text = ''
        if employee.user.first_name:
            text = f'Nome: {employee.user.first_name} {employee.user.last_name}'
        else:
            text = f'{employee.name}'
        text += f' | Saldo de horas: {employee.overtime_total}'
        p.drawString(
            10, y, text)
        y -= 40

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:

    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={filename}.pdf'
            return response
        else:
            response = HttpResponse(
                "Erro ao Renderelizar o PDF", status_code=400)


class PDF(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel salves',
            'request': request,
        }
        return Render.render('employees/report_employees.html', params, 'my_file')


class OverTimeExportCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatório.csv"'

        overtime_rest = OverTime.objects.filter(is_hours=True)

        writer = csv.writer(response)
        writer.writerow([
            'Code',
            'Funcionário',
            'Motivo',
            'Rest. Func',
            'Horas'
        ])
        for time in overtime_rest:
            writer.writerow([
                time.pk,
                time.employee,
                time.reason,
                time.employee.overtime_total,
                time.hours,
            ])

        return response


class OverTimeExportExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatório.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        row_num = 0
        columns = [
            'Code',
            'Funcionário',
            'Motivo',
            'Rest. Func',
            'Horas'
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        times = OverTime.objects.filter(is_hours=True)

        row_num = 1
        for time in times:
            ws.write(row_num, 0, str(time.pk), font_style)
            ws.write(row_num, 1, time.employee.name, font_style)
            ws.write(row_num, 2, time.reason, font_style)
            ws.write(row_num, 3, time.employee.overtime_total, font_style)
            ws.write(row_num, 4, time.hours, font_style)
            row_num += 1

        wb.save(response)
        return response
