# -*- coding: utf-8 -*-

from language_detection import LanguageDetector
from text_input import get_user_input
from file_operations import FileHandler

def main():
    # Obtenir le texte d'entr�e de l'utilisateur
    text = get_user_input()

    # Cr�er une instance de LanguageDetector
    detector = LanguageDetector()

    # Identifier le langage du texte
    language = detector.detect_language(text)

    # Afficher le r�sultat
    print("Langage detecte :", language)

if __name__ == "__main__":
    main()

