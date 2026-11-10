import os
import glob
import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(".")
T_DIR = os.path.join(BASE_DIR, "T-mixer")
Y_DIR = os.path.join(BASE_DIR, "Y-mixer")
SR_DIR = os.path.join(BASE_DIR, "SR-mixer")

RE_LIST = [25, 50, 100, 250, 500]
MIXERS = ["T-mixer", "Y-mixer", "SR-mixer"]

# Verify CSV existence
for m, d in [("T-mixer", T_DIR), ("Y-mixer", Y_DIR), ("SR-mixer", SR_DIR)]:
    mix_csv = os.path.join(d, "processed_outputs", "mixing_index_results.csv")
    dp_csv = os.path.join(d, "processed_outputs", "pressure_drop_summary.csv")
    trade_csv = os.path.join(d, "processed_outputs", "tradeoff_analysis.csv")
    conv_csv = os.path.join(d, "processed_outputs", "fluent_convergence_summary.csv")
    print(f"Checking {m}:")
    print("  mixing_index:", os.path.exists(mix_csv))
    print("  pressure_drop:", os.path.exists(dp_csv))
    print("  tradeoff:", os.path.exists(trade_csv))
    print("  convergence:", os.path.exists(conv_csv))

# Read and print summaries
t_trade = pd.read_csv(os.path.join(T_DIR, "processed_outputs", "tradeoff_analysis.csv"))
y_trade = pd.read_csv(os.path.join(Y_DIR, "processed_outputs", "tradeoff_analysis.csv"))
sr_trade = pd.read_csv(os.path.join(SR_DIR, "processed_outputs", "tradeoff_analysis.csv"))

print("\nOutlet MI Comparison (%):")
for re in RE_LIST:
    t_val = t_trade.loc[t_trade['Re'] == re, 'Outlet MI (%)'].values[0]
    y_val = y_trade.loc[y_trade['Re'] == re, 'Outlet MI (%)'].values[0]
    sr_val = sr_trade.loc[sr_trade['Re'] == re, 'Outlet MI (%)'].values[0]
    print(f"Re={re:3d}: T={t_val:5.2f}%, Y={y_val:5.2f}%, SR={sr_val:5.2f}% | SR Advantage: +{sr_val-max(t_val,y_val):5.2f}%")

print("\nPressure Drop Comparison (kPa):")
for re in RE_LIST:
    t_dp = t_trade.loc[t_trade['Re'] == re, 'ΔP (kPa)'].values[0]
    y_dp = y_trade.loc[y_trade['Re'] == re, 'ΔP (kPa)'].values[0]
    sr_dp = sr_trade.loc[sr_trade['Re'] == re, 'ΔP (kPa)'].values[0]
    print(f"Re={re:3d}: T={t_dp:6.2f} kPa, Y={y_dp:6.2f} kPa, SR={sr_dp:6.2f} kPa")

