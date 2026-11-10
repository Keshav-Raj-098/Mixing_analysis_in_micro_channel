import os

BASE_DIR = os.path.abspath(".")
T_DIR = os.path.join(BASE_DIR, "T-mixer", "observations")
Y_DIR = os.path.join(BASE_DIR, "Y-mixer", "observations")
SR_DIR = os.path.join(BASE_DIR, "SR-mixer", "observations")

RE_LIST = [25, 50, 100, 250, 500]

print("Checking mesh/model images:")
print("  T-mixer mesh:", os.path.exists(os.path.join(T_DIR, "mesh-image.png")))
print("  Y-mixer mesh:", os.path.exists(os.path.join(Y_DIR, "Y-mesh.png")))
print("  SR-mixer mesh:", os.path.exists(os.path.join(SR_DIR, "mesh.png")))

print("\nChecking longitudinal concentration contours:")
for re in [25, 100, 500]:
    for name, d in [("T", T_DIR), ("Y", Y_DIR), ("SR", SR_DIR)]:
        p1 = os.path.join(d, f"Re-{re}", "contours", "longitudinal", "conc_longitudinal.png")
        p2 = os.path.join(d, f"Re-{re}", "contours", "longitudinal", "conc_longitudinal.jpg")
        exists = os.path.exists(p1) or os.path.exists(p2)
        print(f"  {name} Re={re}: {exists}")

print("\nChecking cross-sectional concentration contours at Plane 1, 3, 6:")
for re in [25, 100, 500]:
    for p in [1, 3, 6]:
        for name, d in [("T", T_DIR), ("Y", Y_DIR), ("SR", SR_DIR)]:
            p1 = os.path.join(d, f"Re-{re}", "contours", "conc", f"conc_plane{p}.png")
            p2 = os.path.join(d, f"Re-{re}", "contours", "conc", f"conc_plane{p}.jpg")
            exists = os.path.exists(p1) or os.path.exists(p2)
            if not exists:
                print(f"  MISSING: {name} Re={re} Plane {p}")
print("Done checking.")

