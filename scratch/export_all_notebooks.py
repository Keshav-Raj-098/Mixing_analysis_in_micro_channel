import os
import subprocess
import nbformat
from nbconvert import HTMLExporter

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

notebooks = [
    (r"comparision\Comparative_Mixer_Analysis.ipynb", r"comparision\Comparative_Mixer_Analysis.html", r"comparision\Comparative_Mixer_Analysis.pdf"),
    (r"T-mixer\T_Mixer_Analysis.ipynb", r"T-mixer\T_Mixer_Analysis.html", r"T-mixer\T_Mixer_Analysis.pdf"),
    (r"Y-mixer\Y_Mixer_Analysis.ipynb", r"Y-mixer\Y_Mixer_Analysis.html", r"Y-mixer\Y_Mixer_Analysis.pdf"),
    (r"SR-mixer\SR_Mixer_Analysis.ipynb", r"SR-mixer\SR_Mixer_Analysis.html", r"SR-mixer\SR_Mixer_Analysis.pdf"),
]

html_exporter = HTMLExporter()

for nb_rel, html_rel, pdf_rel in notebooks:
    nb_path = os.path.abspath(nb_rel)
    html_path = os.path.abspath(html_rel)
    pdf_path = os.path.abspath(pdf_rel)
    
    if not os.path.exists(nb_path):
        print(f"Skipping {nb_rel} (not found)")
        continue
        
    print(f"\nProcessing {nb_rel}...")
    try:
        with open(nb_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        
        body, resources = html_exporter.from_notebook_node(nb)
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(body)
        print(f"  -> Generated HTML: {html_rel} ({os.path.getsize(html_path):,} bytes)")
        
        # Now convert to PDF via Edge
        if os.path.exists(EDGE_PATH):
            cmd = [
                EDGE_PATH,
                "--headless",
                "--disable-gpu",
                f"--print-to-pdf={pdf_path}",
                html_path
            ]
            res = subprocess.run(cmd, capture_output=True, timeout=30)
            if os.path.exists(pdf_path):
                print(f"  -> Generated PDF:  {pdf_rel} ({os.path.getsize(pdf_path):,} bytes)")
            else:
                print(f"  -> PDF generation via Edge did not produce file. Return code: {res.returncode}")
    except Exception as e:
        print(f"  Error processing {nb_rel}: {e}")

print("\nAll exports finished!")

