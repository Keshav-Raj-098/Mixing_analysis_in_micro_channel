import os
import nbformat
from nbconvert import HTMLExporter

notebooks = [
    (r"comparision\Comparative_Mixer_Analysis.ipynb", r"comparision\Comparative_Mixer_Analysis.html"),
    (r"T-mixer\T_Mixer_Analysis.ipynb", r"T-mixer\T_Mixer_Analysis.html"),
    (r"Y-mixer\Y_Mixer_Analysis.ipynb", r"Y-mixer\Y_Mixer_Analysis.html"),
    (r"SR-mixer\SR_Mixer_Analysis.ipynb", r"SR-mixer\SR_Mixer_Analysis.html"),
]

html_exporter = HTMLExporter()
print("Starting HTML extraction for all micromixer notebooks...")

for nb_rel, html_rel in notebooks:
    nb_path = os.path.abspath(nb_rel)
    html_path = os.path.abspath(html_rel)
    
    if not os.path.exists(nb_path):
        print(f"Skipping {nb_rel} (file not found)")
        continue
        
    print(f"Extracting {nb_rel} -> {html_rel}...")
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        
    body, resources = html_exporter.from_notebook_node(nb)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(body)
        
    file_size_mb = os.path.getsize(html_path) / (1024 * 1024)
    print(f"  Successfully saved: {html_rel} ({file_size_mb:.2f} MB)")

print("\nAll HTML files successfully extracted!")

