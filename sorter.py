import os
import shutil
import threading

def sort_files(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            file_path = os.path.join(root, file)
            new_folder_path = os.path.join(folder_path, file_extension[1:])
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            shutil.move(file_path, new_folder_path)

def process_folder(folder_path):
    main_thread = threading.Thread(target=sort_files, args=(folder_path,))
    main_thread.start()

    # Перебираємо всі підпапки та створюємо потік для кожної
    for root, dirs, _ in os.walk(folder_path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            thread = threading.Thread(target=sort_files, args=(dir_path,))
            thread.start()

    main_thread.join()

if __name__ == "__main__":
    folder_to_process = "Хлам"
    process_folder(folder_to_process)