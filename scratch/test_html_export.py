import os
import nbformat
from nbconvert import HTMLExporter

nb_path = r"comparision\Comparative_Mixer_Analysis.ipynb"
html_path = r"comparision\Comparative_Mixer_Analysis.html"

print("Reading notebook:", nb_path)
with open(nb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

print("Exporting to HTML...")
html_exporter = HTMLExporter()
# Use classic or default template
body, resources = html_exporter.from_notebook_node(nb)

print("Writing HTML to:", html_path)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(body)

print("Success! Size of HTML:", os.path.getsize(html_path), "bytes")

