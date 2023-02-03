import os
import decode
import encode


def save_files(coding):
    file_list = os.listdir("input")
    # sprawdzenie czy w ogóle pliki istnieją
    inp_files_exist = False
    for file_name in file_list:
        if file_name.startswith("inp"):
            inp_files_exist = True
            break
    # Przeiteruj przez pliki
    if inp_files_exist:
        for file_name in file_list:
            # pomin ukryte pliki
            if file_name.startswith("."):
                continue
            with open("input/" + file_name) as f:
                lines = []
                for line in f:
                    lines.append(line)
                output_file_name = file_name.replace("inp", "out")
                with open("output/" + output_file_name, "w") as outf:
                    for line in lines:
                        if coding is False:
                            outf.write(decode.decode(line))
                        else:
                            outf.write(encode.encode(line))
    else:
        print("Poszukiwane pliki nie istnieją.")
