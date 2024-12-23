import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(base_folder):
    """
    Per ogni cartella principale, unisce i PDF presenti nelle sottocartelle in ordine di nome e salva il risultato
    nella cartella principale con il nome della cartella principale.

    :param base_folder: Il percorso della cartella principale contenente le altre cartelle.
    """
    # Naviga tra tutte le cartelle principali in ordine
    for main_folder in sorted(os.listdir(base_folder)):
        main_folder_path = os.path.join(base_folder, main_folder)

        # Verifica se è una directory
        if os.path.isdir(main_folder_path):
            merger = PdfMerger()
            
            # Naviga tra le sottocartelle in ordine
            for sub_folder in sorted(os.listdir(main_folder_path)):
                sub_folder_path = os.path.join(main_folder_path, sub_folder)

                # Verifica se è una directory
                if os.path.isdir(sub_folder_path):
                    
                    # Aggiunge tutti i PDF nella sottocartella in ordine
                    for file in sorted(os.listdir(sub_folder_path)):
                        if file.endswith('.pdf'):
                            pdf_path = os.path.join(sub_folder_path, file)
                            merger.append(pdf_path)

            # Salva il PDF risultante con il nome della cartella principale
            output_pdf_path = os.path.join(base_folder, f"{main_folder}.pdf")
            merger.write(output_pdf_path)
            merger.close()
            print(f"Creato: {output_pdf_path}")

# Utilizzo dello script
# Specifica il percorso della cartella base
base_folder_path = "."  # Sostituisci con il percorso corretto
merge_pdfs_in_folder(base_folder_path)
