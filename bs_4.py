from bs4 import BeautifulSoup
import requests
from googletrans import Translator
import tkinter as tk
from tkinter import messagebox

# Создаем объект Translator
translator = Translator()

# Инициализация глобальной переменной
current_word = ""


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
    # Функция, которая сообщит об ошибке, но не остановит программу
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
        messagebox.showinfo("Результат", "Все верно!")
    else:
        messagebox.showinfo("Результат", f"Ответ неверный, было загадано это слово: {current_word}")
    start_game()


# Создаем основное окно
root = tk.Tk()
root.title("Угадай значение слова")
root.geometry("800x400")  # Устанавливаем размер окна

# Создаем виджеты с увеличенным шрифтом
font_large = ("Helvetica", 14)

label_instruction = tk.Label(root, text="Введите слово по его значению:", font=font_large)
label_instruction.pack(pady=10)

label_word_definition = tk.Label(root, text="Значение слова:", font=font_large)
label_word_definition.pack(pady=5)

entry_word = tk.Entry(root, font=font_large)
entry_word.pack(pady=5)

button_start = tk.Button(root, text="Начать игру", font=font_large, width=20, height=2, command=start_game)
button_start.pack(pady=5)

button_check = tk.Button(root, text="Отправить ответ", font=font_large, width=20, height=2, command=check_answer)
button_check.pack(pady=5)

# Запускаем главный цикл
root.mainloop()


