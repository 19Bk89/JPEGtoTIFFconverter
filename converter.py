import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_image():
    file_path = filedialog.askopenfilename(
        title="Wähle eine JPEG-Datei",
        filetypes=[("JPEG files", "*.jpg;*.jpeg")]
    )
    
    if not file_path:
        return  # Benutzer hat abgebrochen

    try:
        img = Image.open(file_path)
    except Exception as e:
        messagebox.showerror("Fehler", f"Bild konnte nicht geöffnet werden:\n{e}")
        return

    try:
        # In CMYK konvertieren
        img_cmyk = img.convert('CMYK')

        # Zielpfad erzeugen
        base, _ = os.path.splitext(file_path)
        output_path = base + "_converted.tiff"

        # Speichern
        img_cmyk.save(output_path, format="TIFF")

        messagebox.showinfo("Erfolg", f"Bild erfolgreich konvertiert und gespeichert als:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Fehler beim Konvertieren", str(e))

# GUI erstellen
root = tk.Tk()
root.title("JPEG zu CMYK-TIFF Konverter")

root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text="Klicke auf den Button, um ein JPEG zu laden und als CMYK-TIFF zu speichern.")
label.pack(pady=20)

button = tk.Button(root, text="Bild auswählen & konvertieren", command=convert_image, bg="#4CAF50", fg="white", padx=10, pady=5)
button.pack()

root.mainloop()
