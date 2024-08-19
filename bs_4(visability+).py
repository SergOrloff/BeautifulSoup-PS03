from bs4 import BeautifulSoup
import requests
from googletrans import Translator
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button


# Создаем объект Translator
translator = Translator()

# Инициализация глобальной переменной
current_word = ""

# Цвета и шрифты
bg_color = "#282C34"
fg_color = "#ABB2BF"
yellow_color = "#FFD700"
green_color = "#32CD32"
highlight_color = "#E06C75"
font_large = ("Helvetica", 14)
font_bold = ("Times new roman", 14, "bold")

# Создаем функцию, которая будет получать информацию по url запросу
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаем объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. Text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его определение на русский
        translated_word = translator.translate(english_words, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        # Чтобы программа возвращала словарь
        return {
            "english_words": translated_word,
            "word_definition": translated_definition
        }
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

# Функция для старта игры
def start_game():
    global current_word
    word_dict = get_english_words()
    if word_dict:
        current_word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
        label_word_definition.config(text=f"Значение слова: {word_definition}")
        entry_word.delete(0, tk.END)

# Функция для проверки ответа
def check_answer():
    global current_word
    user_word = entry_word.get()
    if user_word.lower() == current_word.lower():
        # root.withdraw()  # Скрыть root window
        custom_messagebox("Результат", "Все верно!")
    else:
        # root.withdraw()  # Скрыть root window
        custom_messagebox("Результат", f"Ответ неверный, было загадано это слово: {current_word}")
    start_game()

# Функция для создания окна вывода результатов проверки ответа
def custom_messagebox(title, message):
    # Создаем новое окно для вывода результатов проверки ответа
    window = Toplevel()
    window.title(title)
    window.geometry("700x120")  # Устанавливаем размер окна
    window.configure(bg="#654321")  # Устанавливаем цвет фона окна

    # Задаем параметры выводимого текста (шрифт, размер, его цвет и цвет фона текста)
    label = Label(window, text=message, font=("Times New Roman", 14), bg="#654321", fg=yellow_color)
    label.pack(pady=20)

    # Добавляем кнопку OK для закрытия окна
    ok_button = Button(window, text="OK", command=window.destroy)
    ok_button.pack(pady=10)


# Создаем основное окно
root = tk.Tk()
root.title("Угадай значение слова")
root.geometry("1200x400")  # Устанавливаем размер окна
root.configure(bg=bg_color)  # Устанавливаем цвет фона

# Создаем виджеты с увеличенным шрифтом
label_instruction = tk.Label(root, text="Введите слово по его значению:", font=font_large, bg=bg_color, fg=green_color)
label_instruction.pack(pady=10)

label_word_definition = tk.Label(root, text="Значение слова:", font=font_bold, bg=bg_color, fg=yellow_color)
label_word_definition.pack(pady=5)

entry_word = tk.Entry(root, font=font_large, bg=fg_color, fg=bg_color)
entry_word.pack(pady=5)

button_start = tk.Button(root, text="Начать игру", font=font_large, width=20, height=2, command=start_game, bg="#00FF00", fg=bg_color)
button_start.pack(pady=5)

button_check = tk.Button(root, text="Отправить ответ", font=font_large, width=20, height=2, command=check_answer, bg=yellow_color, fg=bg_color)
button_check.pack(pady=5)

# Запускаем главный цикл
root.mainloop()