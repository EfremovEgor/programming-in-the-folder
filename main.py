import os
import time
import sys
import io

WORKING_FOLDER_PATH = os.path.join(os.getcwd(), "development")
STARING_FILE_PATH = os.path.join(WORKING_FOLDER_PATH, "DELETE TO START THE PROGRAM")
EXAMPLE_FILE_PATH = os.path.join(WORKING_FOLDER_PATH, "1 print('HELLO WORLD')")
ORIGINAL_STDOUT = sys.stdout


def create_template():
    with open(STARING_FILE_PATH, "w"):
        ...
    with open(EXAMPLE_FILE_PATH, "w"):
        ...


def create_file(name: str):
    name = (
        name.replace("/", "∕")
        .replace(":", "꞉")
        .replace(">", "»")
        .replace("<", "«")
        .replace("*", "⊛")
        .replace("?", "Ɂ")
        .replace("\\", "⑊")
    )
    with open(
        os.path.join(
            WORKING_FOLDER_PATH,
            name,
        ),
        "w",
    ):
        ...


def programming_loop():
    while True:
        if not os.path.isfile(STARING_FILE_PATH):
            string_code = "\n".join(
                file.split(" ", 1)[1]
                for file in sorted(os.listdir(WORKING_FOLDER_PATH), key=lambda x: x[0])
                if file[0].isdigit()
            )
            for file in os.listdir(WORKING_FOLDER_PATH):
                if not file[0].isdigit():

                    os.remove(os.path.join(WORKING_FOLDER_PATH, file))
            print(string_code)
            sys.stdout = string = io.StringIO()
            try:
                exec(string_code)
            except Exception as ex:
                print(ex)
            sys.stdout = ORIGINAL_STDOUT
            create_file("$_________CONSOLE OUTPUT_________$")
            time.sleep(1)

            for line in string.getvalue().strip().split("\n"):

                create_file("$ " + line)
                time.sleep(1)
            create_file("!______END OF CONSOLE OUTPUT______!")
            time.sleep(1)
            with open(STARING_FILE_PATH, "w"):
                ...


if __name__ == "__main__":
    if not os.path.exists(WORKING_FOLDER_PATH):
        os.mkdir(WORKING_FOLDER_PATH)
    if not os.listdir(WORKING_FOLDER_PATH):
        create_template()
    programming_loop()
