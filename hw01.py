import os
import shutil

# Функція для рекурсивного копіювання та сортування файлів за розширенням
def copy_and_sort_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_ext = os.path.splitext(file)[1][1:]  # отримуємо розширення файлу
            ext_dir = os.path.join(dest_dir, file_ext)  # створюємо директорію для розширення
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(ext_dir, file)
            shutil.copy2(src_file_path, dest_file_path)
            print(f"Копіюється {src_file_path} до {dest_file_path}")

# Головна функція
def main():
    # Запитуємо шляхи від користувача
    src_dir = input("Введіть шлях до вихідної директорії: ")
    dest_dir = input("Введіть шлях до директорії призначення (за замовчуванням 'dist'): ")

    # Якщо шлях призначення не введено, використовуємо 'dist'
    if not dest_dir:
        dest_dir = 'dist'

    try:
        copy_and_sort_files(src_dir, dest_dir)
        print("Копіювання завершено.")
    except Exception as e:
        print(f"Помилка під час копіювання файлів: {e}")

if __name__ == "__main__":
    main()
