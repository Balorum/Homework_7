import os
import shutil
import sys
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "y",
    "",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
extensions = {
    "video": [
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".wmv",
        ".3gp",
        ".3g2",
        ".mpg",
        ".mpeg",
        ".m4v",
        ".h264",
        ".flv",
        ".rm",
        ".swf",
        ".vob",
    ],
    "audio": [
        ".mp3",
        ".wav",
        ".ogg",
        ".flac",
        ".aif",
        ".mid",
        ".midi",
        ".mpa",
        ".wma",
        ".wpl",
        ".cda",
        ".amr",
    ],
    "image": [
        ".jpg",
        ".png",
        ".bmp",
        ".ai",
        ".psd",
        ".ico",
        ".jpeg",
        ".ps",
        ".svg",
        ".tif",
        ".tiff",
    ],
    "archive": [
        ".zip",
        ".gz",
        ".tar",
    ],
    "text": [
        ".pdf",
        ".txt",
        ".doc",
        ".docx",
        ".rtf",
        ".tex",
        ".wpd",
        ".odt",
        ".xlsx",
        ".pptx",
    ],
}
ext_list = list(extensions.items())


def normalize(file_name):
    file_parts = file_name.split(".")
    new_file = ""
    for i in file_parts[0]:
        if (
            i.isalpha()
            or i.isdigit()
            or i in CYRILLIC_SYMBOLS
            or i in CYRILLIC_SYMBOLS.upper()
        ):
            new_file += i
        else:
            new_file += "_"
    new_file += "." + file_parts[1]
    return new_file.translate(TRANS)


indir_extention = set()
miss_extention = set()


def sort_def(main_folder):
    global indir_extention
    global miss_extention
    for i in main_folder.iterdir():
        if (
            i.is_dir()
            and i.name != "video"
            and i.name != "images"
            and i.name != "documents"
            and i.name != "audio"
            and i.name != "archives"
        ):
            sort_def(i)
        elif i.is_file():
            new_file = Path(os.path.dirname(i) + "\\" + normalize(i.name))
            os.rename(i, new_file)
            if i.suffix in ext_list[0][1]:
                shutil.move(new_file, Path(sys.argv[1] + "\\video"))
            elif i.suffix in ext_list[1][1]:
                shutil.move(new_file, Path(sys.argv[1] + "\\audio"))
            elif i.suffix in ext_list[2][1]:
                shutil.move(new_file, Path(sys.argv[1] + "\\images"))
            elif i.suffix in ext_list[3][1]:
                shutil.move(new_file, Path(sys.argv[1] + "\\archives"))
                archive_path = Path(
                    sys.argv[1] + "\\archives" + "\\" + normalize(i.name)
                )
                file_parts = new_file.name
                created_folder_path = Path(
                    sys.argv[1] + "\\archives" + "\\" + file_parts.split(".")[0]
                )
                os.mkdir(created_folder_path)
                shutil.unpack_archive(
                    archive_path,
                    created_folder_path,
                )
            elif i.suffix in ext_list[4][1]:
                shutil.move(new_file, Path(sys.argv[1] + "\\documents"))
            else:
                miss_extention.add(i.suffix)
            indir_extention.add(i.suffix)
    del_empty_dirs(main_folder)


def del_empty_dirs(path):
    for i in os.listdir(path):
        if (
            i != "video"
            and i != "images"
            and i != "documents"
            and i != "audio"
            and i != "archives"
        ):
            a = os.path.join(path, i)
            if os.path.isdir(a):
                del_empty_dirs(a)
                if not os.listdir(a):
                    os.rmdir(a)


def create_five_folders(sort_folder_path):
    folders = ["video", "images", "documents", "audio", "archives"]
    for i in range(5):
        os.mkdir(Path(str(sort_folder_path) + "\\" + folders[i]))


def run():
    print(type(sys.argv[0]))
    print("fdsgs")
    # sort_folder_path = Path(sys.argv[1])
    # create_five_folders(sort_folder_path)
    # sort_def(sort_folder_path)
    # print(f"Розширення, які оброблює програма: {ext_list}")
    # print(f"Наявні у файлі розширення: {indir_extention}")
    # print(f"Необроблені розширення: {miss_extention}")


if __name__ == "__main__":
    run()
