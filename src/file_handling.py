import os
import shutil
import logging

def copy_src_to_destination(src: str, dest: str) -> None:
    src = os.path.expanduser(src)
    dest = os.path.expanduser(dest)
    logging.basicConfig(
        filename="logging_copy_files.log",
        filemode="a",
        level=logging.INFO
    )
    if os.path.exists(dest):
        shutil.rmtree(dest)
        logging.info(f"{dest} directory was cleaned")
    os.mkdir(dest)
    logging.info(f"{dest} directory was recreated")

    for content in os.listdir(src):
        name = os.path.join(src, content)
        new_name = os.path.join(dest, content)
        if os.path.isfile(name):
            logging.info(f"{name} was copied to {new_name}")
            shutil.copy(name, new_name)
            continue

        
        copy_src_to_destination(name, new_name)
        logging.info(f"Copying the files of {name} to {new_name}")

    return None

    
