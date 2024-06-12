from tkinter import Tk, Label, Button, messagebox
import tkinter as tk
import fitz
from PIL import Image, ImageTk
from os import path

window = Tk()
abs_path_files = f'{str(path.dirname(path.abspath(__file__)))}{path.sep}files{path.sep}'


class MainMenu:
    def __init__(self):
        self.theme_Button = None
        self.canvas = tk.Canvas(window, bg='#FFDEAD')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.main_menu()
        window.mainloop()

    def main_menu(self):
        window.title("Главное меню")
        window.geometry("700x1000+500+0")
        Label(self.canvas, text="Topics for review", font=("Arial Bold", 20), background='#FFDEAD').place(x=20, y=10)
        Button(self.canvas, text="Unit 1", command=lambda: self.start_theme("1"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=60)
        Button(self.canvas, text="Unit 2", command=lambda: self.start_theme("2"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=100)
        Button(self.canvas, text="Unit 3", command=lambda: self.start_theme("3"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=140)
        Button(self.canvas, text="Unit 4", command=lambda: self.start_theme("4"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=180)
        Button(self.canvas, text="Unit 5", command=lambda: self.start_theme("5"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=220)
        Button(self.canvas, text="Unit 6", command=lambda: self.start_theme("6"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=260)
        Button(self.canvas, text="Unit 7", command=lambda: self.start_theme("7"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=300)
        Button(self.canvas, text="Unit 8", command=lambda: self.start_theme("8"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=340)
        Button(self.canvas, text="Unit 9", command=lambda: self.start_theme("9"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=380)
        Button(self.canvas, text="Unit 10", command=lambda: self.start_theme("10"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=420)
        Button(self.canvas, text="Unit 11", command=lambda: self.start_theme("11"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=460)
        Button(self.canvas, text="Unit 12", command=lambda: self.start_theme("12"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=500)
        Button(self.canvas, text="Unit 13", command=lambda: self.start_theme("13"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=540)
        Button(self.canvas, text="Unit 14", command=lambda: self.start_theme("14"), bd=1, bg='#D2B48C', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3").place(x=20, y=580)
        Button(self.canvas, text="Dictionary", command=self.start_dictionary, bd=1, bg='#FFE4B5', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#FFE4C4").place(x=20, y=660)
        Button(self.canvas, text="Exit", command=window.destroy, bd=1, bg='#8B0000', width=20,
               font=("Times New Roman", 12), overrelief="ridge", activebackground="#B22222").place(x=20, y=700)

    def start_theme(self, theme):
        destroy_canvas(self.canvas)
        pdf_file = f'{abs_path_files}pdf{path.sep}{theme}.pdf'
        TeachBook(theme, pdf_file)

    def start_dictionary(self):
        destroy_canvas(self.canvas)
        pdf_file = f'{abs_path_files}pdf{path.sep}vocabulary.pdf'
        Dictionary(pdf_file)


class Dictionary:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.page_num = 0
        self.img_tk = tk.Image

        self.canvas = tk.Canvas(window, bg='#FFDEAD')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        window.geometry("700x1000+500+0")

        self.render_page()

        window.bind("<Left>", self.prev_page)
        window.bind("<Right>", self.next_page)

        self.button_glav = tk.Button(self.canvas, text="Главное меню", command=self.glav_men, bd=1, bg='#D2B48C',
                                     width=11, font=("Times New Roman", 11), overrelief="ridge",
                                     activebackground="#F5DEB3")
        self.button_glav.place(x=602, y=10)

    def render_page(self):
        pdf_document = fitz.open(self.pdf_file)
        page = pdf_document[self.page_num]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img = img.resize((600, 800))
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.img_tk = img_tk

    def prev_page(self, event):
        if self.page_num > 0:
            self.page_num -= 1
            self.render_page()

    def next_page(self, event):
        pdf_document = fitz.open(self.pdf_file)
        if self.page_num < pdf_document.page_count - 1:
            self.page_num += 1
            self.render_page()

    def glav_men(self):
        destroy_canvas(self.canvas)
        MainMenu()


class TeachBook:
    def __init__(self, theme, pdf_file):
        self.theme = theme
        self.pdf_file = pdf_file
        self.page_num = 0
        self.img_tk = tk.Image

        self.root = window
        self.canvas = tk.Canvas(self.root, bg='#FFDEAD')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.root.geometry("700x1000+500+0")

        self.render_page()

        self.root.bind("<Left>", self.prev_page)
        self.root.bind("<Right>", self.next_page)

        self.button = tk.Button(self.canvas, text="Тестирование", command=self.start_test, bd=1, bg='#D2B48C', width=15,
                                font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3")
        self.button.place(x=553, y=740)

        self.button_glav = tk.Button(self.canvas, text="Главное меню", command=self.glav_men, bd=1, bg='#D2B48C',
                                     width=15, font=("Times New Roman", 12), overrelief="ridge",
                                     activebackground="#F5DEB3")
        self.button_glav.place(x=553, y=10)

    def render_page(self):
        pdf_document = fitz.open(self.pdf_file)
        page = pdf_document[self.page_num]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img = img.resize((550, 800))
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.img_tk = img_tk

    def prev_page(self, event):
        if self.page_num > 0:
            self.page_num -= 1
            self.render_page()

    def next_page(self, event):
        pdf_document = fitz.open(self.pdf_file)
        if self.page_num < pdf_document.page_count - 1:
            self.page_num += 1
            self.render_page()

    def start_test(self):
        test_file = f'{abs_path_files}txt{path.sep}Tester{path.sep}{self.theme}.txt'
        if not path.exists(test_file):
            messagebox.showerror("Внимание!", "Файл с тестированием отсутствует!")
            return  # Stay in TeachBook
        destroy_canvas(self.canvas)
        TestApp(self.theme)

    def glav_men(self):
        destroy_canvas(self.canvas)
        MainMenu()


class Tester:
    def __init__(self, theme, score=0, all_questions=0):
        self.root = window
        self.theme = theme
        self.questions = self.load_questions(f'{abs_path_files}txt{path.sep}Tester{path.sep}{self.theme}.txt')
        self.current_question = 0
        self.score = 0
        self.false = 0
        self.first_test_score = score
        self.first_test_questions = all_questions
        self.history = []
        self.load_file()
        self.setup_ui()

    def load_file(self):
        self.file = open(f'{abs_path_files}txt{path.sep}Tester{path.sep}{self.theme}.txt', "r")

    def load_questions(self, filename):
        questions = []
        with open(filename, "r") as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                if i + 5 >= len(lines):
                    break
                theme = lines[i].strip()
                i += 1
                question_text = lines[i].strip()
                i += 1
                answers = []
                for _ in range(4):
                    if i < len(lines):
                        answers.append(lines[i].strip())
                        i += 1
                if i < len(lines):
                    correct_answer = lines[i].strip()
                    i += 1
                    question = {
                        "theme": theme,
                        "question_text": question_text,
                        "answers": answers,
                        "correct_answer": correct_answer
                    }
                    questions.append(question)
                else:
                    break
        return questions

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='#FFDEAD', highlightthickness=0)
        self.canvas.pack(side=tk.TOP)

        self.buttons_frame = tk.Frame(self.root, bg='#FFDEAD', highlightthickness=0, bd=0)
        self.buttons_frame.pack(side=tk.TOP)

        self.assignment_label = Label(self.canvas, text="", font=("Times New Roman", 16, "bold"),
                                      wraplength=380, bg='#FFDEAD', highlightthickness=0, bd=0)
        self.assignment_label.pack(fill=tk.BOTH, expand=True, pady=(10, 5))

        self.question_label = Label(self.canvas, text="", font=("Times New Roman", 14), wraplength=380, bg='#FFDEAD',
                                    highlightthickness=0, bd=0)
        self.question_label.pack(fill=tk.BOTH, expand=True, pady=(20, 10))

        self.back_button = Button(self.buttons_frame, text="Назад", command=self.prev_question, bd=1, bg='#D2B48C',
                                  width=15,
                                  font=("Times New Roman", 11), overrelief="ridge", activebackground="#F5DEB3")
        self.back_button.pack(side=tk.BOTTOM, pady=10)

        self.buttons = []
        for j in range(4):
            button = Button(self.buttons_frame, text=f"Answer {chr(65 + j)}",
                            command=lambda i=j: self.check_answer(chr(65 + i)), bd=1, bg='#D2B48C', width=15,
                            font=("Times New Roman", 11), overrelief="ridge", activebackground="#F5DEB3")
            button.pack(side=tk.LEFT, padx=5)

            self.buttons.append(button)

        self.show_question()

    def show_question(self):
        self.canvas.delete("all")
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]

            self.assignment_label.config(text=question["theme"])
            self.canvas.create_window(200, 50, window=self.assignment_label)

            self.question_label.config(text=question["question_text"])
            self.canvas.create_window(200, 100, window=self.question_label)

            for i, answer in enumerate(question["answers"]):
                self.buttons[i].config(text=answer)
            for i in range(len(question["answers"]), 4):
                self.buttons[i].config(text="", state=tk.DISABLED)
        else:
            self.show_results()
            self.buttons_frame.destroy()

    def show_results(self):
        self.allq = self.score + self.false

        result_label = tk.Label(self.canvas, text='Правильных ответов '
                                                  + str(self.score + self.first_test_score) + ' ', font='Arial 14',
                                bg='#FFDEAD')
        result_label.pack()
        proc = tk.Label(self.canvas, text='Процент правильных ответов =  '
                                          + str(int(((self.score + self.first_test_score) /
                                                     (self.allq + self.first_test_questions)) * 100)) + ' %',
                        font='Arial 14', bg='#FFDEAD')
        proc.pack()

        def glav_men():
            destroy_canvas(self.canvas)
            self.file.seek(0)
            MainMenu()

        def restart():
            destroy_canvas(self.canvas)
            self.file.seek(0)
            TestApp(self.theme)

        Glav_menu = tk.Button(self.canvas, text='Перейти в главное меню', command=glav_men, bd=1, bg='#D2B48C',
                              width=20, font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3")
        Glav_menu.pack(side=tk.LEFT, padx=10)

        restart_button = tk.Button(self.canvas, text='Начать тест заново', command=restart, bd=1, bg='#D2B48C',
                                   width=20, font=("Times New Roman", 12), overrelief="ridge",
                                   activebackground="#F5DEB3")
        restart_button.pack(side=tk.LEFT, padx=5)

    def check_answer(self, answer):
        question = self.questions[self.current_question]
        self.history.append((self.current_question, self.score, self.false))
        if answer == question["correct_answer"]:
            self.score += 1
        else:
            self.false += 1
        self.current_question += 1
        self.show_question()

    def prev_question(self):
        if self.history:
            self.current_question, self.score, self.false = self.history.pop()
            self.show_question()


class TestApp:
    def __init__(self, theme):
        self.root = window
        self.root.configure(bg='#FFDEAD')
        self.theme = theme
        self.current_block = 0
        self.questions_blocks = []
        self.answers_blocks = []
        self.user_answers = []
        self.scores = []
        self.block_titles = []  # Хранение названий блоков
        self.load_questions_from_file(f'{abs_path_files}txt{path.sep}TestApp{path.sep}{self.theme}.txt')
        self.init_ui()
        self.total_score = 0
        self.total_questions = sum(len(block) for block in self.questions_blocks)
        self.display_questions()

    def init_ui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='#FFDEAD', highlightthickness=0)
        self.canvas.pack(side=tk.TOP)

        self.frame = tk.Frame(self.canvas, bg='#FFDEAD', highlightthickness=0, bd=0)
        self.frame.pack(side=tk.TOP)

        self.next_button = tk.Button(self.canvas, text="Следующий блок", command=self.next_block, bd=1, bg='#D2B48C',
                                     width=20, font=("Times New Roman", 12), overrelief="ridge",
                                     activebackground="#F5DEB3")
        self.next_button.pack(side=tk.TOP, pady=10)

        self.prev_button = tk.Button(self.canvas, text="Назад", command=self.prev_block, bd=1, bg='#D2B48C', width=20,
                                     font=("Times New Roman", 12), overrelief="ridge", activebackground="#F5DEB3")
        self.prev_button.pack(side=tk.TOP, pady=10)

    def load_questions_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            current_questions = []
            current_answers = []
            current_title = None  # Для хранения текущего названия блока
            for line in lines:
                line = line.strip()
                if line.startswith("Название:"):
                    current_title = line[len("Название:"):].strip()
                elif line.startswith("Вопрос:"):
                    current_questions.append({"question": line[len("Вопрос:"):].strip(), "options": []})
                elif line.startswith("Ответ:"):
                    current_answers.append(line[len("Ответ:"):].strip().lower())
                elif line == "Next":
                    if current_questions and current_answers and current_title:
                        self.questions_blocks.append(current_questions)
                        self.answers_blocks.append(current_answers)
                        self.block_titles.append(current_title)
                        self.user_answers.append([""] * len(current_questions))
                        self.scores.append(0)
                        current_questions = []
                        current_answers = []
                        current_title = None
            if current_questions and current_answers and current_title:
                self.questions_blocks.append(current_questions)
                self.answers_blocks.append(current_answers)
                self.block_titles.append(current_title)
                self.user_answers.append([""] * len(current_questions))
                self.scores.append(0)

    def display_questions(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        self.question_labels = []
        self.answer_entries = []

        block_title = self.block_titles[self.current_block]
        block_label = tk.Label(self.frame, text=block_title, font='Arial 12 bold', bg='#FFDEAD', wraplength=400)
        block_label.pack(pady=(0, 10))

        for i, question in enumerate(self.questions_blocks[self.current_block]):
            question_label = tk.Label(self.frame, text=question["question"], font='Arial 10', bg='#FFDEAD',
                                      wraplength=600)
            question_label.pack()
            self.question_labels.append(question_label)

            answer_entry = tk.Entry(self.frame)
            answer_entry.pack()
            answer_entry.insert(0, self.user_answers[self.current_block][i])
            self.answer_entries.append(answer_entry)

    def next_block(self):
        self.save_current_answers()
        if self.current_block < len(self.questions_blocks) - 1:
            self.scores[self.current_block] = self.calculate_block_score(self.current_block)
            self.total_score = sum(self.scores)
            self.current_block += 1
            self.display_questions()
        else:
            self.scores[self.current_block] = self.calculate_block_score(self.current_block)
            self.total_score = sum(self.scores)
            destroy_canvas(self.canvas)
            Tester(self.theme, score=self.total_score, all_questions=self.total_questions)

    def prev_block(self):
        if self.current_block > 0:
            self.save_current_answers()
            self.scores[self.current_block] = self.calculate_block_score(self.current_block)
            self.total_score = sum(self.scores)
            self.current_block -= 1
            self.display_questions()
        else:
            destroy_canvas(self.canvas)
            TeachBook(self.theme, f'{abs_path_files}pdf{path.sep}{self.theme}.pdf')

    def save_current_answers(self):
        self.user_answers[self.current_block] = [entry.get().strip().lower() for entry in self.answer_entries]

    def calculate_block_score(self, block_index):
        user_answers = self.user_answers[block_index]
        correct_answers = self.answers_blocks[block_index]
        return sum(
            1 for user_answer, correct_answer in zip(user_answers, correct_answers) if user_answer == correct_answer)


def destroy_canvas(canvas: tk.Canvas) -> None:
    window.unbind("<Left>")
    window.unbind("<Right>")
    canvas.destroy()


if __name__ == "__main__":
    MainMenu()
