__author__ = 'marcovigilante'

import os

BASEDIR = "/"
READ = 'r'
READWRITE = 'r+'
WRITE = 'w'

#MAIN FUNCTION
def main():

    #get a list of file in the directory
    list = os.listdir(BASEDIR)
    print ("Printing directory list for '" + BASEDIR + "' : ")
    stampaLista(list)
#   salvaLista(list)


#METHOD
def stampaLista(lista):

    for l in lista:
        print (l)
    return





#FIRE MAIN
main()
