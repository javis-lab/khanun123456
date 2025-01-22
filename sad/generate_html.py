from tkinter import *
from tkinter import messagebox

def calculate_price():
    try:
        # รับค่าจากช่องป้อนข้อมูล
        name1 = entry_name1.get()
        price1 = float(entry_price1.get())
        quantity1 = float(entry_quantity1.get())

        name2 = entry_name2.get()
        price2 = float(entry_price2.get())
        quantity2 = float(entry_quantity2.get())

        # คำนวณราคาเฉลี่ยต่อหน่วย
        unit_price1 = price1 / quantity1
        unit_price2 = price2 / quantity2

        # เปรียบเทียบราคาและแสดงผล
        if unit_price1 < unit_price2:
            result = f"{name1} ถูกกว่าที่ {unit_price1:.2f} ต่อบาท"
        elif unit_price1 > unit_price2:
            result = f"{name2} ถูกกว่าที่ {unit_price2:.2f} ต่อบาท"
        else:
            result = f"{name1} และ {name2} มีราคาเฉลี่ยเท่ากันที่ {unit_price1:.2f} ต่อบาท"

        # แสดงผลลัพธ์
        label_result.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "กรุณาป้อนตัวเลขในช่องราคาและปริมาณสินค้า")

# สร้างหน้าต่างหลัก
root = Tk()
root.title("โปรแกรมเปรียบเทียบราคาสินค้า")
root.geometry("700x700")  # ตั้งขนาดหน้าต่างเป็น 700x700
root.config(bg="#f0f4f8")

# ส่วนหัวโปรแกรม
header = Label(root, text="เปรียบเทียบราคาสินค้า", font=("Arial", 26, "bold"), fg="#ffffff", bg="#4a90e2", pady=20)
header.pack(fill=X)

# สร้างเฟรมกลาง
frame = Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(expand=True)

# ส่วนที่ 1: ป้อนข้อมูลสินค้าชิ้นที่ 1
Label(frame, text="สินค้าชิ้นที่ 1", bg="#ffffff", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
Label(frame, text="ชื่อสินค้า:", bg="#ffffff", font=("Arial", 14)).grid(row=1, column=0, sticky=E, pady=10)
entry_name1 = Entry(frame, font=("Arial", 14))
entry_name1.grid(row=1, column=1, pady=10)

Label(frame, text="ราคา (บาท):", bg="#ffffff", font=("Arial", 14)).grid(row=2, column=0, sticky=E, pady=10)
entry_price1 = Entry(frame, font=("Arial", 14))
entry_price1.grid(row=2, column=1, pady=10)

Label(frame, text="ปริมาณ:", bg="#ffffff", font=("Arial", 14)).grid(row=3, column=0, sticky=E, pady=10)
entry_quantity1 = Entry(frame, font=("Arial", 14))
entry_quantity1.grid(row=3, column=1, pady=10)

# ส่วนที่ 2: ป้อนข้อมูลสินค้าชิ้นที่ 2
Label(frame, text="สินค้าชิ้นที่ 2", bg="#ffffff", font=("Arial", 16, "bold")).grid(row=4, column=0, columnspan=2, pady=20)
Label(frame, text="ชื่อสินค้า:", bg="#ffffff", font=("Arial", 14)).grid(row=5, column=0, sticky=E, pady=10)
entry_name2 = Entry(frame, font=("Arial", 14))
entry_name2.grid(row=5, column=1, pady=10)

Label(frame, text="ราคา (บาท):", bg="#ffffff", font=("Arial", 14)).grid(row=6, column=0, sticky=E, pady=10)
entry_price2 = Entry(frame, font=("Arial", 14))
entry_price2.grid(row=6, column=1, pady=10)

Label(frame, text="ปริมาณ:", bg="#ffffff", font=("Arial", 14)).grid(row=7, column=0, sticky=E, pady=10)
entry_quantity2 = Entry(frame, font=("Arial", 14))
entry_quantity2.grid(row=7, column=1, pady=10)

# ปุ่มคำนวณ
button_calculate = Button(frame, text="เปรียบเทียบราคา", command=calculate_price, bg="#4caf50", fg="#ffffff",
                          font=("Arial", 16), relief="flat", padx=10, pady=10)
button_calculate.grid(row=8, column=0, columnspan=2, pady=30)

# แสดงผลลัพธ์
label_result = Label(frame, text="", fg="#4a90e2", bg="#ffffff", font=("Arial", 14, "bold"))
label_result.grid(row=9, column=0, columnspan=2, pady=10)

# เพิ่ม footer
footer = Label(root, text="สร้างโดย: EDU COM NU 65", font=("Arial", 8), bg="#4a90e2", fg="#ffffff", pady=8)
footer.place(relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()
