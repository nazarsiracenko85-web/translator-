from customtkinter import *
import requests

set_appearance_mode("dark")
set_default_color_theme("blue")

window = CTk()
window.title("Перекладач")
window.geometry("450x550")

langs = {
    "Англійська": "en",
    "Німецька": "de",
    "Польська": "pl",
    "Французька": "fr",
    "Іспанська": "es",
    "Італійська": "it"
}


def set_output(text):
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", text)
    output_box.configure(state="disabled")


def translate():
    # Отримати введений текст
    text = input_box.get("1.0", "end").strip()

    if text == "":
        set_output("Введіть текст ...")
        return
    
    lang = menu.get()
    code = langs[lang]

    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=uk|{code}"

    # Перекласти
    try:
        res = requests.get(url).json()
        r = res["responseData"]["translatedText"]
        set_output(r)
    except:
        set_output("Помилка")


# Заголовок "Перекладач"  шрифт ("Arial", 24, "bold")
CTkLabel(window, text="Перекладач", font=("Arial", 24, "bold")).pack(pady=15)

# Контейнер для вводу
input_frame = CTkFrame(window, fg_color="transparent")
input_frame.pack(padx=30, fill="x")

# "Введіть текст українською:"  шрифт ("Arial", 13, "bold")
CTkLabel(input_frame, 
         text="Введіть текст українською:", 
         font=("Arial", 13, "bold")).pack(padx=5, anchor="w")

# Поле для введення тексту. Колір рамки #3B8ED0
input_box = CTkTextbox(input_frame,
                       height=20,
                       border_width=2,
                       border_color="#3B8ED0",
                       corner_radius=10
                       )
input_box.pack(pady=5, fill="x")


# Фрейм для меню і кнопки
action_frame = CTkFrame(window, fg_color="transparent")
action_frame.pack(padx=30, fill="x", pady=20)

# Випадаючий список
menu= CTkOptionMenu(action_frame,
                    values=list(langs.keys()),
                    corner_radius=8
                    )
menu.pack(side="left", padx=(0, 10), expand=True, fill="x")
menu.set("Англіська")

# Кнопка. шрифт ("Arial", 14)
btn = CTkButton(action_frame,
                text="Перекласти",
                font=("Arial", 14),
                command=translate,
                corner_radius=8
                )
btn.pack(side="left", expand=True, fill="x")
# Текст "Результат:"
CTkLabel(window, text="Результат:",).pack(anchor="w", padx=30)

# Поле з перекладом. Колір рамки #553fab
output_box = CTkTextbox(window,
                       height=150,
                       border_width=2,
                       border_color="#553fab",
                       corner_radius=10
                       )
output_box.pack(pady=5, fill="x", padx=30)

# Запуск
window.mainloop()