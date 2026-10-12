"""
License: Apache
Organization: UNIR
"""

import os
import argparse

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ordena las palabras de un fichero."
    )

    parser.add_argument(
        "filename",
        nargs="?",
        default=DEFAULT_FILENAME,
        help="Nombre del fichero de palabras (por defecto: words.txt)"
    )

    parser.add_argument(
        "--order",
        choices=["ascending", "descending"],
        default="ascending",
        help="Orden de las palabras: ascending o descending"
    )

    parser.add_argument(
        "--unique",
        action="store_true",
        default=DEFAULT_DUPLICATES,
        help="Eliminar palabras duplicadas"
    )

    args = parser.parse_args()

    filename = args.filename
    remove_duplicates = args.unique
    ascending = args.order == "ascending"

    print(f"Se leerán las palabras del fichero {filename}")

    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("The filename must be provided as the first argument")
        print("The second argument specifies whether to remove duplicates")
        sys.exit(1)

    print(f"Reading words from file {filename}")
    file_path = os.path.join(".", filename)

    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"El fichero {filename} no existe")
        word_list = [
            "ravenclaw",
            "gryffindor",
            "slytherin",
            "hufflepuff"
        ]
        print(f"File {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending=ascending))