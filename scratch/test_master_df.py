import os
import tempfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp())

BASE_DIR = os.path.abspath(".")
T_DIR = os.path.join(BASE_DIR, "T-mixer")
Y_DIR = os.path.join(BASE_DIR, "Y-mixer")
SR_DIR = os.path.join(BASE_DIR, "SR-mixer")
OUT_DIR = os.path.join(BASE_DIR, "comparison_outputs")
os.makedirs(OUT_DIR, exist_ok=True)

RE_LIST = [25, 50, 100, 250, 500]
OBS_DIST = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]

# Load mixing CSVs
t_mix = pd.read_csv(os.path.join(T_DIR, "processed_outputs", "mixing_index_results.csv"), index_col=0)
y_mix = pd.read_csv(os.path.join(Y_DIR, "processed_outputs", "mixing_index_results.csv"), index_col=0)
sr_mix = pd.read_csv(os.path.join(SR_DIR, "processed_outputs", "mixing_index_results.csv"), index_col=0)

# Load tradeoff CSVs
t_trade = pd.read_csv(os.path.join(T_DIR, "processed_outputs", "tradeoff_analysis.csv"))
y_trade = pd.read_csv(os.path.join(Y_DIR, "processed_outputs", "tradeoff_analysis.csv"))
sr_trade = pd.read_csv(os.path.join(SR_DIR, "processed_outputs", "tradeoff_analysis.csv"))

print("T mixing shape:", t_mix.shape)
print("Y mixing shape:", y_mix.shape)
print("SR mixing shape:", sr_mix.shape)

# Build Master Comparison DataFrame
records = []
for re in RE_LIST:
    col = f"Re={re}"
    for name, trade_df, mix_df in [("T-Mixer", t_trade, t_mix), ("Y-Mixer", y_trade, y_mix), ("SR-Mixer", sr_trade, sr_mix)]:
        row = trade_df[trade_df["Re"] == re].iloc[0]
        u_in = row["U_in (m/s)"]
        q_tot = row["Q_total (uL/min)"]
        dp_kpa = row["ΔP (kPa)"]
        w_pump = row["Pumping Power (mW)"]
        mi_out = row["Outlet MI (%)"]
        eff = row["Mixing Efficiency (1/kPa)"]
        
        mi_p1 = mix_df.loc["Plane 1 (x=1.5mm)", col] * 100.0
        mi_p6 = mix_df.loc["Plane 6 (x=4.0mm)", col] * 100.0
        delta_mi = mi_p6 - mi_p1
        rate_mi = delta_mi / (4.0 - 1.5) # %/mm
        
        records.append({
            "Mixer Geometry": name,
            "Reynolds Number (Re)": re,
            "Inlet Velocity (m/s)": u_in,
            "Total Flow Rate (uL/min)": q_tot,
            "Pressure Drop (kPa)": dp_kpa,
            "Pumping Power (mW)": w_pump,
            "Plane 1 MI (%)": mi_p1,
            "Outlet Plane 6 MI (%)": mi_p6,
            "Mixing Gain ΔMI (%)": delta_mi,
            "Spatial Rate dMI/dx (%/mm)": rate_mi,
            "Efficiency η (%/kPa)": eff
        })

df_master = pd.DataFrame(records)
print(df_master.head(6))
df_master.to_csv(os.path.join(OUT_DIR, "comparative_mixer_summary.csv"), index=False)
print("Master CSV saved successfully.")

