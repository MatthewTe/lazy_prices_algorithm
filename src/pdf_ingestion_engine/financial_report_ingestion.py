# Importing PyPDF2 PDF management package:
import PyPDF2 as p2


# Creating class that is meant to represent the Financial Report PDF:
class financial_report(object):
    """
    financial_report() object contains all the methods necessary to parse a
    10-K or 10-Q Financial Report.

    Critically most of the methods stored within this object are used to
    construct instance variables and as such many of the methods are called within
    the initalization of object and heavily make use of the PyPDF2 library.
    This will primarily be used as a base class to be inherited for other
    packages and methods.

    Parameters
    -----------

    Methods
    -----------

    """

    def __init__(self, file_path):

    # Declaring key instance variables:
    self.file_path = file_path


    # Opening the pdf file:
    pdf = open('tests/test_pdfs/ExxonMobil 2019 10-K Report.pdf', 'rb')

    # TODO: Write the PDF PyPDF2 Object initalization as well as Password Decrypt.




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
