import PyPDF2 as p2

# Opening the pdf file:
pdf = open('tests/test_pdfs/ExxonMobil 2019 10-K Report.pdf', 'rb')

pdfread = p2.PdfFileReader(pdf)

x = pdfread.getOutlines()


def parse_destination_object(destination_object):

    if type(destination_object) is not list:
        print(destination_object)

    else:
        for x in destination_object:
            parse_destination_object(x)


for destination in x:
    parse_destination_object(destination)

"""TODO: Find a way of tracking how the recursive function travels through the
nested destenation objects and for a way to group all of them, potentally re-nested
dicts."""
