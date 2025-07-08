#!/usr/bin/python
from deep_translator import GoogleTranslator
from autocorrect import Speller
import signal
from termcolor import colored
import sys

def handler(sig,frame):
    #estado de salida
    print(colored("\n\nSaliendo del programa...\n","red"))
    sys.exit(1)
signal.signal(signal.SIGINT,handler)


def corrector(palabra):
    #corregir palabra
    corrector_str = Speller(lang="es")
    return corrector_str(palabra)

def translate(corrector):
    #Traduccir palabra
    translated = GoogleTranslator(source="es", target="en").translate(corrector)
    print(f"\n{translated}")

def main():
    try:
        palabra = input(">> ")
        word_correct = corrector(palabra)
        translate(word_correct)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
