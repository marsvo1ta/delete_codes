from openpyxl import load_workbook


def process_excel_column_a(file):
    workbook = load_workbook(file)
    sheet = workbook.active

    result = []
    for row in sheet.iter_rows(min_col=1, max_col=1, values_only=True):
        cell_value = row[0]
        result.append(cell_value)

    workbook.close()
    return result



