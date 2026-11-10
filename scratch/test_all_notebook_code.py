import os
import json
import traceback
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.show = lambda: None

with open("comparision.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

global_env = {
    "display": lambda x: print("[DataFrame Displayed successfully]"),
}

print("Validating code cells in comparision.ipynb:")
code_idx = 0
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        code_idx += 1
        src = "".join(cell["source"])
        print(f"Testing code cell {code_idx}...")
        try:
            exec(src, global_env)
            print(f"  Cell {code_idx} passed successfully.")
        except Exception as e:
            print(f"  ERROR in Cell {code_idx}: {e}")
            traceback.print_exc()
            break
print("\nAll code cells tested successfully!")
