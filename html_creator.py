import os


# Funkcja do generowania wiersza tabeli z informacjami o pliku
def generate_table_row(input_filename):
    input_filepath = f"input/{input_filename}"
    output_filename = input_filename.replace("inp", "out")
    output_filepath = f"output/{output_filename}"

    # Otwieramy plik wejściowy i wyjściowy
    with open(input_filepath, "r") as input_file, open(output_filepath, "r") as output_file:
        # Pobieramy zawartość plików
        input_content = input_file.read()
        output_content = output_file.read()
        # Zamieniamy znaki nowej linii na elementy HTML <br>
        input_content = input_content.replace("\n", "<br>")
        output_content = output_content.replace("\n", "<br>")

    # Generujemy wiersz tabeli z informacjami o plikach
    return f"<tr><td>{input_filename}</td><td>{input_content}</td><td>{output_filename}</td><td>{output_content}</td></tr>"


# Funkcja do generowania całego raportu
def generate_report():
    # Pobieramy listę plików z folderów input i output
    input_filenames = os.listdir("input")
    output_filenames = os.listdir("output")

    inp_files_exist = False
    for file_name in output_filenames:
        if file_name.startswith("out"):
            inp_files_exist = True
            break
    if inp_files_exist:
        # Inicjujemy listę z wierszami tabeli
        table_rows = []

        # Iterujemy po plikach wejściowych i odpowiadającym im plikom wyjściowym
        for input_filename in input_filenames:
            if input_filename.startswith("."):
                continue
            # Generujemy wiersz tabeli dla danej pary plików
            table_row = generate_table_row(input_filename)
            table_rows.append(table_row)

        # Łączymy wiersze tabeli w jedną całość
        table_content = "\n".join(table_rows)

        # Generujemy kod HTML dla całego raportu
        report_html = f"""
      <html>
        <head>
          <title>Raport</title>
          <meta charset="utf-8">
          <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
        <h2>Raport </h2>
          <table>
            <tr>
              <th>Nazwa pliku wejściowego </th>
              <th> Zawartość pliku wejściowego </th>
              <th> Nazwa pliku wyjściowego </th>
              <th> Zawartość pliku wyjściowego </th>
            </tr>
            {table_content}
          </table>
        </body>
      </html>
      """

        # Zwracamy kod HTML raportu
        return report_html
    else:
        return 0


def main():
    # Generujemy raport
    report_html = generate_report()
    if report_html == 0:
        print("Raport nie został utworzony ze względu na brak analizowanych plików.")
    else:
        # Zapisujemy raport do pliku
        with open("raport.html", "w") as report_file:
            report_file.write(report_html)

        print("Raport został wygenerowany.")


if __name__ == "__main__":
    main()
