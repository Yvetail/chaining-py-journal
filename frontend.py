import tkinter as tk
from tkinter import messagebox
from backend import infer_disease

# Daftar gejala (G1-G31) beserta penjelasannya
symptoms = {
    'G1': 'Chlorotic Colored Leaves',
    'G2': 'Experiencing stunted growth',
    'G3': 'The white color is like flour on the upper and lower surfaces of the leaves which are chlorotic',
    'G4': 'Leaves curl and twist',
    'G5': 'The formation of the cob is disturbed',
    'G6': 'Affected leaves look wilted',
    'G7': 'Several small spots unite to form a larger spot',
    'G8': 'Elongated light brown spots in the form of a coil or boat',
    'G9': 'Brown spots shaped like an ellipse',
    'G10': 'Leaves look dry',
    'G11': 'Small brown or yellow spots on the leaf surface',
    'G12': 'Red spots on the midrib',
    'G13': 'Irregularly shaped threads that are white and then brown',
    'G14': 'Powder like yellowish brown flour',
    'G15': 'Swelling of the cob',
    'G16': 'White to black fungus on the seeds',
    'G17': 'Swollen seeds',
    'G18': 'Glands are formed in the seeds',
    'G19': 'Kelobot opens and a lot of white to black fungus appears',
    'G20': 'There is a small hole in the leaf',
    'G21': 'Slit on the stem',
    'G22': 'Male flowers or the base of the cob',
    'G23': 'Stems and tassels (male flowers) break easily',
    'G24': 'Pile of broken tassels',
    'G25': 'Male flowers are not formed',
    'G26': 'Flour/dirt around the hoist',
    'G27': 'Slightly yellow leaves',
    'G28': 'Transverse holes in the leaf in the vegetative stage',
    'G29': 'Corn cob hair is cut / reduced / dry',
    'G30': 'The tip of the cob has a quiver',
    'G31': 'Presence of larvae'
}

# Fungsi untuk memproses gejala yang dipilih
def check_disease():
    selected_symptoms = [symptom_listbox.get(i) for i in symptom_listbox.curselection()]
    
    if len(selected_symptoms) < 3:
        messagebox.showwarning("Warning", "Please select at least 3 symptoms.")
        return
    
    # Backend logic untuk inferensi penyakit bisa dipanggil di sini
    result = infer_disease(selected_symptoms)  # Fungsi infer_disease dari backend
    
    # Menampilkan hasil inferensi penyakit
    if result:
        messagebox.showinfo("Possible Disease", f"Possible disease(s): {', '.join(result)}")
    else:
        messagebox.showinfo("No Match", "No disease matched more than 3 symptoms.")

# Membuat aplikasi GUI dengan Tkinter
root = tk.Tk()
root.title("Corn Disease Diagnosis")

# Kolom 1: Listbox untuk memilih gejala
tk.Label(root, text="Pilih Gejala (G1-G31)").grid(row=0, column=0)
symptom_listbox = tk.Listbox(root, selectmode="multiple", height=15, width=25)

for symptom_code in symptoms.keys():
    symptom_listbox.insert(tk.END, symptom_code)

symptom_listbox.grid(row=1, column=0, padx=10, pady=10)

# Kolom 2: Menampilkan deskripsi gejala yang dipilih
tk.Label(root, text="Penjelasan Gejala").grid(row=0, column=1)
description_textbox = tk.Text(root, height=15, width=50)
description_textbox.grid(row=1, column=1, padx=10, pady=10)

# Fungsi untuk memperbarui deskripsi saat gejala dipilih
def update_description(event):
    selected_indices = symptom_listbox.curselection()
    description_textbox.delete(1.0, tk.END)
    
    for i in selected_indices:
        symptom_code = symptom_listbox.get(i)
        description_textbox.insert(tk.END, f"{symptom_code}: {symptoms[symptom_code]}\n\n")

# Menambahkan event handler saat item di listbox dipilih
symptom_listbox.bind('<<ListboxSelect>>', update_description)

# Tombol 'Periksa'
check_button = tk.Button(root, text="Periksa", command=check_disease)
check_button.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi Tkinter
root.mainloop()
