import os
import tempfile
import subprocess

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_path = os.path.abspath(r"comparision\Comparative_Mixer_Analysis.html")
pdf_path = os.path.abspath(r"comparision\Comparative_Mixer_Analysis.pdf")
user_data = tempfile.mkdtemp()

cmd = [
    EDGE_PATH,
    "--headless",
    "--disable-gpu",
    f"--user-data-dir={user_data}",
    f"--print-to-pdf={pdf_path}",
    f"file:///{html_path.replace(os.sep, '/')}"
]

print("Running Edge PDF command...")
try:
    res = subprocess.run(cmd, timeout=15)
    print("Edge finished with code:", res.returncode)
    print("PDF exists:", os.path.exists(pdf_path))
    if os.path.exists(pdf_path):
        print("PDF size:", os.path.getsize(pdf_path), "bytes")
except Exception as e:
    print("Error:", e)

