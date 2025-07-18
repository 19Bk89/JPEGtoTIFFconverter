import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, TiffImagePlugin
import os

def convert_image_better():
    file_path = filedialog.askopenfilename(
        title="Wähle eine JPEG-Datei",
        filetypes=[("JPEG-Dateien", "*.jpg;*.jpeg")]
    )

    if not file_path:
        return

    try:
        img = Image.open(file_path)
        img_cmyk = img.convert('CMYK')

        base, _ = os.path.splitext(file_path)
        output_path = base + "_converted_better.tiff"

        # TIFF-Metadaten (z. B. DPI)
        tiffinfo = TiffImagePlugin.ImageFileDirectory_v2()
        tiffinfo[282] = 300  # X-DPI
        tiffinfo[283] = 300  # Y-DPI

        img_cmyk.save(
            output_path,
            format='TIFF',
            compression='tiff_lzw',  # verlustfreie Komprimierung
            dpi=(300, 300),
            tiffinfo=tiffinfo
        )

        messagebox.showinfo("Erfolg", f"Bild erfolgreich konvertiert:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Fehler", f"Beim Konvertieren ist ein Fehler aufgetreten:\n{e}")

# GUI aufbauen
root = tk.Tk()
root.title("JPEG zu CMYK-TIFF Konverter (bessere Qualität)")
root.geometry("450x160")
root.resizable(False, False)

label = tk.Label(root, text="Wähle ein JPEG aus, das als CMYK-TIFF mit besserer Qualität gespeichert wird.")
label.pack(pady=20, padx=20)

button = tk.Button(root, text="JPEG auswählen & konvertieren", command=convert_image_better, bg="#4CAF50", fg="white", padx=10, pady=6)
button.pack()

root.mainloop()
