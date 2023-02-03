#!/bin/bash
# Funkcja do wyświetlania menu
show_menu() {
        echo "Wybierz opcję:"
        echo "1. Uruchom kodowanie"
        echo "2. Uruchom dekodowanie"
        echo "3. Backup"
        echo "4. Informacje o projekcie"
        echo "5. Wyjście"
        read option
        case $option in
            1) rm -f output/*.txt; python3 encode.py; clear; python3 html_creator.py;;
            2) rm -f output/*.txt; python3 decode.py; clear; python3 html_creator.py;;
            3) cp raport.html backup/raport-$(date +%Y-%m-%d-%H-%M-%S).html; clear; echo "Backup wykonany.";;
            4) clear;
              echo "Projekt ten dokonuje szyfrowania Staszkowego, które ma następujące zasady:";
              echo "- Dla samogłosek przesuwamy znak o 3 miejsca w prawo.";
              echo "- Dla spógłosek przesuwamy znak o 3 miejsca w prawo i dodajemy 'o'";
              echo "Autor - Aleksandra Kacprzak";;
            5) exit 0;;
            *) clear; echo "Nieprawidłowa opcja";;
        esac
        echo "___________________________"
        show_menu
}

# Wyświetlenie menu
show_menu
