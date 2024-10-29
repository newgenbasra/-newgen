import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import random
from PIL import Image, ImageTk
import webbrowser


class LotteryApp:

    def open_link(self, url):
        webbrowser.open(url)

    def __init__(self, master):
        self.master = master
        master.title("قرعة الأسماء")
        master.geometry("1400x800")
        master.config(bg="#f0f0f0")

        # إضافة شعارات التواصل
        try:
            # شعار التليجرام
            self.telegram_image = Image.open("D:/gggg/telegram.png")
            self.telegram_image = self.telegram_image.resize((75, 75))
            self.telegram_image = ImageTk.PhotoImage(self.telegram_image)
            self.telegram_button = tk.Label(master, image=self.telegram_image, bg="#f0f0f0")
            self.telegram_button.place(x=620, y=700)
            self.telegram_button.bind("<Button-1>", lambda e: self.open_link("https://t.me/newgen_basra"))

            # شعار الانستقرام
            self.instagram_image = Image.open("D:/gggg/instagram.png")
            self.instagram_image = self.instagram_image.resize((60, 60))
            self.instagram_image = ImageTk.PhotoImage(self.instagram_image)
            self.instagram_button = tk.Label(master, image=self.instagram_image, bg="#f0f0f0")
            self.instagram_button.place(x=860, y=700)
            self.instagram_button.bind("<Button-1>", lambda e: self.open_link("https://www.instagram.com/newgen_basra"))

                    # تحميل الصورة باستخدام Pillow
            self.logo_image = Image.open("D:/gggg/logo.png")
            self.logo_image = self.logo_image.resize((190, 190))  # تغيير الحجم (العرض، الارتفاع)
            self.logo_image = ImageTk.PhotoImage(self.logo_image)

        # إنشاء Label لعرض الصورة
            logo_label = tk.Label(master, image=self.logo_image, bg="#f0f0f0")
            logo_label.pack(pady=10)  # إضافة مسافة عمودية

            # شعار الواتساب
            self.whatsapp_image = Image.open("D:/gggg/whatsapp.png")
            self.whatsapp_image = self.whatsapp_image.resize((75, 75))
            self.whatsapp_image = ImageTk.PhotoImage(self.whatsapp_image)
            self.whatsapp_button = tk.Label(master, image=self.whatsapp_image, bg="#f0f0f0")
            self.whatsapp_button.place(x=740, y=700)
            self.whatsapp_button.bind("<Button-1>", lambda e: self.open_link("https://wa.me/9647725606948"))
        except Exception as e:
            messagebox.showerror("خطأ", f"فشل في تحميل شعارات التواصل: {e}")

        # المتغيرات الرئيسية
        self.names = []
        self.winners = []
        self.draw_button_text = tk.StringVar(value="إجراء القرعة")

        # عنوان التطبيق
        title_label = tk.Label(master, text="NewGen", font=("Arial", 46), bg="#f0f0f0", fg="#4CAF50")
        title_label.pack(pady=20)

        # زر إدراج ملف Excel
        self.upload_button = tk.Button(master, text="إدراج ملف اكسل", command=self.upload_file, width=15, font=("Arial", 24), bg="#4CAF50", fg="white")
        self.upload_button.place(x=500, y=350, width=550, height=50)

        # زر إظهار الأسماء
        self.show_button = tk.Button(master, text="إظهار الأسماء", command=self.show_names, width=15, font=("Arial", 24), bg="#2196F3", fg="white")
        self.show_button.place(x=150, y=670, width=300, height=50)

        # زر إخفاء الأسماء
        self.hide_button = tk.Button(master, text="إخفاء الأسماء", command=self.hide_names, width=15, font=("Arial", 24), bg="#f44336", fg="white")
        self.hide_button.place(x=150, y=730, width=300, height=50)

        # حقل إدخال عدد الفائزين المطلوب
        self.num_winners_label = tk.Label(master, text=":عدد الفائزين المطلوب", bg="#f0f0f0", font=("Arial", 24))
        self.num_winners_label.place(x=790, y=455, width=250, height=50)

        self.num_winners_entry = tk.Entry(master, width=15, font=("Arial", 24))
        self.num_winners_entry.place(x=500, y=455, width=250, height=50)

        # زر إجراء/إعادة القرعة
        self.draw_button = tk.Button(master, textvariable=self.draw_button_text, command=self.draw_lottery, width=15, font=("Arial", 24), bg="#FF9800", fg="white")
        self.draw_button.place(x=500, y=560, width=550, height=50)

        # زر تحميل الفائزين
        self.download_button = tk.Button(master, text="تحميل الفائزين", command=self.download_winners, width=15, font=("Arial", 24), bg="#673AB7", fg="white")
        self.download_button.place(x=1100, y=670, width=300, height=50)

        # زر تصفية القرعة
        self.clear_button = tk.Button(master, text="تصفية القرعة", command=self.clear_lottery, width=15, font=("Arial", 24), bg="#9E9E9E", fg="white")
        self.clear_button.place(x=1100, y=730, width=300, height=50)

        # عنوان حقل عرض الأسماء المدخلة
        self.names_label = tk.Label(master, text="الأسماء المدخلة (عدد الأسماء: 0)", font=("Arial", 20), bg="#f0f0f0", fg="#4CAF50")
        self.names_label.place(x=150, y=140)

        # حقل عرض الأسماء المدخلة
        self.names_display = tk.Text(master, height=15, width=40, bg="#ffffff", font=("Arial", 12), wrap=tk.WORD)
        self.names_display.place(x=150, y=180, width=300, height=490)

        # شريط التمرير لحقل عرض الأسماء
        self.names_scroll = tk.Scrollbar(master, command=self.names_display.yview)
        self.names_scroll.place(x=455, y=180, height=490)
        self.names_display.config(yscrollcommand=self.names_scroll.set)

        # عنوان حقل عرض أسماء الفائزين
        self.winners_label = tk.Label(master, text="اسماء الفائزين (عدد الأسماء: 0)", font=("Arial", 20), bg="#f0f0f0", fg="#4CAF50")
        self.winners_label.place(x=1100, y=140)

        # حقل عرض الفائزين
        self.winners_display = tk.Text(master, height=15, width=40, bg="#ffffff", font=("Arial", 12), wrap=tk.WORD)
        self.winners_display.place(x=1100, y=180, width=300, height=490)
        self.winners_display.config(state=tk.DISABLED)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            try:
                df = pd.read_excel(file_path)
                self.names = df.iloc[:, 0].dropna().tolist()
                self.names_label.config(text=f"الأسماء المدخلة (عدد الأسماء: {len(self.names)})")
                messagebox.showinfo("نجاح", "تم تحميل الملف بنجاح.")
            except Exception as e:
                messagebox.showerror("خطأ", f"فشل في تحميل الملف: {e}")

    def show_names(self):
        self.names_display.delete(1.0, tk.END)
        self.names_display.insert(tk.END, "\n".join(self.names))

    def hide_names(self):
        self.names_display.delete(1.0, tk.END)

    def draw_lottery(self):
        if self.names:
            try:
                num_winners = int(self.num_winners_entry.get())
                if num_winners < 1 or num_winners > len(self.names):
                    messagebox.showwarning("تحذير", "يرجى إدخال عدد صحيح من 1 إلى عدد الأسماء.")
                    return

                self.winners = random.sample(self.names, num_winners)
                self.display_winners()
                self.winners_label.config(text=f"اسماء الفائزين (عدد الأسماء: {len(self.winners)})")
                self.draw_button_text.set("إعادة القرعة")
            except ValueError:
                messagebox.showwarning("تحذير", "يرجى إدخال عدد صحيح.")
        else:
            messagebox.showwarning("تحذير", "يرجى تحميل الأسماء أولاً.")

    def display_winners(self):
        self.winners_display.config(state=tk.NORMAL)
        self.winners_display.delete(1.0, tk.END)
        self.winners_display.insert(tk.END, "\n".join(self.winners))
        self.winners_display.config(state=tk.DISABLED)

    def download_winners(self):
        if self.winners:
            df_winners = pd.DataFrame(self.winners, columns=["اسماء القرعة"])
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx;*.xls")])
            if file_path:
                df_winners.to_excel(file_path, index=False)
                messagebox.showinfo("نجاح", "تم تحميل الفائزين بنجاح.")
        else:
            messagebox.showwarning("تحذير", "لم يتم إجراء القرعة بعد.")

    def clear_lottery(self):
        self.names = []
        self.winners = []
        self.names_label.config(text="الأسماء المدخلة (عدد الأسماء: 0)")
        self.winners_label.config(text="اسماء الفائزين (عدد الأسماء: 0)")
        self.names_display.delete(1.0, tk.END)
        self.winners_display.config(state=tk.NORMAL)
        self.winners_display.delete(1.0, tk.END)
        self.winners_display.config(state=tk.DISABLED)
        self.draw_button_text.set("إجراء القرعة")


# تشغيل التطبيق
root = tk.Tk()
app = LotteryApp(root)
root.mainloop()
