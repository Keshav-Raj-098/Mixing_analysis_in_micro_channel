# CLL 770: Microfluidics — Final Submission
## Comparative Hydrodynamic and Mixing Evaluation of Passive Micromixer Geometries
### *T-Mixer vs. Y-Mixer vs. 3D Split-and-Recombine (SR) Mixer*

---

## 1. Project Overview & Research Objectives

In microfluidic lab-on-a-chip and micro-total analysis systems ($\mu\text{TAS}$), fluid flows are strictly laminar ($Re \ll 2000$). At high Péclet numbers ($Pe = Re \cdot Sc \sim 10^3 - 10^5$), molecular diffusion across straight laminar streams is exceedingly slow ($\tau_{\text{diff}} \sim w^2/D$). 

### Core Research Questions:
1. **How do simple passive modifications to the microchannel geometry improve mixing in microchannels?**
2. **Which of the examined geometries is the most effective under practical microfluidic constraints (mixing quality vs. pressure drop penalty)?**

To answer these questions, rigorous 3D Computational Fluid Dynamics (CFD) simulations were conducted in **ANSYS Fluent** across five Reynolds numbers ($Re \in \{25, 50, 100, 250, 500\}$) for three geometries sharing identical cross-sections ($W = 200\,\mu\text{m}, H = 100\,\mu\text{m}$, $D_h = 133.33\,\mu\text{m}$) and total observation lengths ($L = 4.0\text{ mm}$, across Planes 1 to 6).

---

## 2. Interactive Reports & Web Dashboard

An interactive welcome portal is available at [**`index.html`**](file:///c:/Users/Keshav%20Raj/Desktop/Sem-7/CLL%20770%20-%20MicroFluids/Final-submission/post-processing/index.html). Double-click or open it in any browser to navigate to all standalone HTML reports:

| Report / Dashboard | File Link | Focus & Highlights |
| :--- | :--- | :--- |
| **Welcome Portal & Dashboard** | [`index.html`](file:///c:/Users/Keshav%20Raj/Desktop/Sem-7/CLL%20770%20-%20MicroFluids/Final-submission/post-processing/index.html) | Interactive navigation hub, summary tables, and physical conclusions. |
| **Comparative Master Study** | [`comparision/Comparative_Mixer_Analysis.html`](file:///c:/Users/Keshav%20Raj/Desktop/Sem-7/CLL%20770%20-%20MicroFluids/Final-submission/post-processing/comparision/Comparative_Mixer_Analysis.html) | Unified benchmarking, $MI(x)$ development, $\Delta P$ scaling, and Pareto frontier. |
| **Split-and-Recombine (SR)** | [`SR-mixer/SR_Mixer_Analysis.html`](file:///c:/Users/Keshav%20Raj/Desktop/Sem-7/CLL%20770%20-%20MicroFluids/Final-submission/post-processing/SR-mixer/SR_Mixer_Analysis.html) | 3D Baker's transformation, multi-lamellar fluid folding, and Dean vortices. |
| **T-Shaped Mixer** | [`T-mixer/T_Mixer_Analysis.html`](file:///c:/Users/Keshav%20Raj/Desktop/Sem-7/CLL%20770%20-%20MicroFluids/Final-submission/post-processing/T-mixer/T_Mixer_Analysis.html) | Opposed 180° impinging inlets, vortex engulfment, and viscous decay. |
| **Y-Shaped Mixer** | [`Y-mixer/Y_Mixer_Analysis.html`](file:///c:/Users/Keshav%20Raj/Desktop/Sem-7/CLL%20770%20-%20MicroFluids/Final-submission/post-processing/Y-mixer/Y_Mixer_Analysis.html) | Converging 45°/120° co-laminar parallel streams and diffusion limits. |

> **PDF Generation:** Open any `.html` file above in Google Chrome or Microsoft Edge, press **`Ctrl + P`**, set destination to **"Save as PDF"**, check **"Background graphics"**, and save.

---

## 3. Mathematical Foundations & Metrics

### 3.1 Transport Equations
- **Continuity:** $\nabla \cdot \vec{u} = 0$
- **Momentum:** $\rho (\vec{u} \cdot \nabla) \vec{u} = -\nabla P + \mu \nabla^2 \vec{u}$
- **Advection-Diffusion:** $\vec{u} \cdot \nabla c = D \nabla^2 c$
  - Fluid properties: $\rho = 998.2\text{ kg/m}^3$, $\mu = 1.003 \times 10^{-3}\text{ Pa}\cdot\text{s}$, $D = 1.0 \times 10^{-9}\text{ m}^2/\text{s}$.

### 3.2 Mixing and Hydraulic Metrics
- **Cross-Sectional Standard Deviation ($\sigma$):**
  $$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (c_i - \bar{c})^2}$$
- **Mixing Index ($MI$):**
  $$MI = 1 - \frac{\sigma}{\sigma_0} \quad \text{with } \sigma_0 = \sqrt{\bar{c}(1 - \bar{c})} = 0.50 \quad (c_1=1, c_2=0, \bar{c}=0.50)$$
  - $MI = 0$: Completely separated unmixed streams.
  - $MI = 1.0$ ($100\%$): Completely homogeneous mixture at molecular level.
- **Hydraulic Pressure Drop ($\Delta P$):**
  $$\Delta P = \frac{P_{\text{in1}} + P_{\text{in2}}}{2} - P_{\text{out}} \quad (P_{\text{out}} = 0\text{ Pa})$$
- **Hydraulic Pumping Power ($W_{\text{pump}}$):**
  $$W_{\text{pump}} = Q_{\text{total}} \cdot \Delta P = (2 \cdot \bar{u}_{\text{in}} \cdot A_{\text{in}}) \cdot \Delta P$$
- **Mixing Energy Efficiency ($\eta$):**
  $$\eta = \frac{MI}{\Delta P} \quad [\%/\text{kPa}], \quad \eta_W = \frac{MI}{W_{\text{pump}}} \quad [\%/\text{mW}]$$

---

## 4. Performance Comparison Matrix

| Reynolds Number ($Re$) | Inlet $U_{\text{in}}$ (m/s) | T-Mixer Outlet $MI$ | T-Mixer $\Delta P$ (kPa) | Y-Mixer Outlet $MI$ | Y-Mixer $\Delta P$ (kPa) | SR-Mixer Outlet $MI$ | SR-Mixer $\Delta P$ (kPa) | SR Advantage over Best Planar ($\Delta MI$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$Re = 25$** | 0.1675 | 13.37% | 2.19 | 15.48% | 1.45 | **57.71%** | **1.95** | **+42.23%** *(at lower $\Delta P$ than T)* |
| **$Re = 50$** | 0.3349 | 17.05% | 4.65 | 14.86% | 3.02 | **62.03%** | **5.04** | **+44.99%** *(comparable $\Delta P$ to T)* |
| **$Re = 100$** | 0.6698 | 24.75% | 10.41 | 14.43% | 6.55 | **65.37%** | **14.43** | **+40.62%** *(Peak Energy Efficiency)* |
| **$Re = 250$** | 1.6745 | 30.73% | 34.88 | 14.26% | 20.14 | **73.02%** | **70.21** | **+42.29%** *(Breaks $70\%$ threshold)* |
| **$Re = 500$** | 3.3490 | 32.67% | 96.05 | 14.55% | 52.48 | **79.47%** | **255.49** | **+46.79%** *(Maximum mixing quality)* |

---

## 5. Physical Mechanisms & Research Conclusions

### 5.1 How Geometry Modifies the Mixing Physics
1. **Y-Mixer (Converging Co-Flow):**
   - Inlets merge at an acute angle ($45^\circ/120^\circ$) without flow separation or impingement. Flow remains strictly parallel and laminar.
   - Scalar transport relies entirely on 1D molecular diffusion across a vertical planar contact surface.
   - As $Re$ increases, the fluid moves faster, reducing residence time ($\tau_{\text{res}} = L/\bar{u} \approx 23.9\text{ ms} \to 1.2\text{ ms}$). The diffusion layer thickness $\delta \approx \sqrt{D \tau_{\text{res}}}$ contracts, keeping the outlet mixing index stuck at an ineffective **$14.3\% - 15.5\%$**.
2. **T-Mixer (180° Impinging Inlets):**
   - Opposed streams collide head-on at the stagnation point.
   - At $Re \le 50$, flow is symmetric and diffusion-dominated ($MI \approx 13-17\%$).
   - At $Re \ge 100$, inertial forces induce a symmetry-breaking engulfment transition and secondary Dean-like vortices at the junction that fold the interface, boosting mixing to **$24.7\%$ ($Re=100$)** and **$32.7\%$ ($Re=500$)**.
   - However, in the straight downstream channel, these vortices quickly dissipate due to viscous friction, causing $MI$ to plateau near $\sim 33\%$.
3. **Split-and-Recombine (SR) Mixer (3D Baker's Transformation + Dean Flow):**
   - Repeatedly splits the fluid into sub-channels, rotates them out-of-plane, and recombines them. This multiplies the number of fluid lamellae as $2^n$ and halves the characteristic diffusion distance ($w_{\text{lamella}} = w/2^n$).
   - Because diffusion time scales with distance squared ($\tau \sim w^2/D$), halving the distance speeds up diffusion by **$4\times$**.
   - Simultaneously, channel curvature generates centrifugal **Dean vortices** ($De = Re\sqrt{D_h/2R}$) that induce chaotic advection, maintaining steep concentration gradients throughout the entire channel.
   - Result: Outstanding mixing of **$57.7\%$ at $Re=25$** reaching **$79.5\%$ at $Re=500$**.

---

### 5.2 Definitive Design Recommendation
- **Most Effective Design Overall:** The **Split-and-Recombine (SR) Mixer is overwhelmingly superior** for scalar homogenization, delivering up to **$5.5\times$ higher mixing** than the planar alternatives.
- **Optimal Operational Sweet-Spot:** Operating the SR-mixer at **$Re = 50 - 100$** delivers $62\% - 65\%$ mixing with an extremely modest pressure drop of only $5.0 - 14.4\text{ kPa}$ ($0.05 - 0.14\text{ bar}$) and minimal pumping power ($< 0.4\text{ mW}$), providing the highest cost-benefit mixing energy efficiency ($\eta = 0.045 - 0.123\text{ \%/kPa}$).
- **High-Throughput Chemical Synthesis:** Use the SR-mixer at $Re = 250 - 500$ ($MI \ge 73\% - 80\%$) with high-pressure syringe pumps capable of overcoming $\Delta P \approx 70 - 255\text{ kPa}$.
- **Non-Mixing Parallel Flows / Cell Focusing:** Use the Y-mixer for applications requiring unperturbed parallel laminar streams without mixing.

---

## 6. Repository Layout & Artifact Directory

```text
post-processing/
│
├── index.html                           <- Interactive web dashboard & portal linking all reports
├── README.md                            <- Comprehensive academic & technical documentation
├── constants.py                         <- Channel geometry & discretization mesh constants
├── export.py                            <- Automated HTML exporter for all Jupyter notebooks
│
├── comparision/
│   ├── Comparative_Mixer_Analysis.ipynb <- Master comparative analysis notebook
│   └── Comparative_Mixer_Analysis.html  <- Standalone interactive HTML report
│
├── comparison_outputs/                  <- 300 DPI comparative figures and CSV datasets
│   ├── fig01_geometric_mesh_comparison.png
│   ├── fig02_streamline_topology_comparison.png
│   ├── fig03_longitudinal_concentration_matrix.png
│   ├── fig04_cross_sectional_concentration_comparison.png
│   ├── fig05_spatial_mixing_index_development.png
│   ├── fig06_outlet_mi_vs_re.png
│   ├── fig07_pressure_drop_scaling.png
│   ├── fig08_pumping_power_vs_re.png
│   ├── fig09_mixing_efficiency_comparison.png
│   ├── fig10_pareto_tradeoff_frontier.png
│   └── comparative_mixer_summary.csv
│
├── T-mixer/                             <- T-Mixer analysis, raw Fluent outputs, and processed figures
│   ├── T_Mixer_Analysis.ipynb
│   ├── T_Mixer_Analysis.html
│   ├── observations/ (Re-25, 50, 100, 250, 500)
│   └── processed_outputs/ (fig01 to fig14 + 4 CSV summaries)
│
├── Y-mixer/                             <- Y-Mixer analysis, raw Fluent outputs, and processed figures
│   ├── Y_Mixer_Analysis.ipynb
│   ├── Y_Mixer_Analysis.html
│   ├── observations/ (Re-25, 50, 100, 250, 500)
│   └── processed_outputs/ (fig01 to fig14 + 4 CSV summaries)
│
└── SR-mixer/                            <- SR-Mixer analysis, raw Fluent outputs, and processed figures
    ├── SR_Mixer_Analysis.ipynb
    ├── SR_Mixer_Analysis.html
    ├── observations/ (Re-25, 50, 100, 250, 500)
    └── processed_outputs/ (fig01 to fig14 + 4 CSV summaries)
```

---

## 7. How to Re-Run & Re-Generate Reports

If you modify raw ANSYS Fluent `.out` files or channel parameters in `constants.py`:

```powershell
# 1. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 2. Run any individual mixer notebook in VS Code or execute the comparative analysis:
# Open comparision/Comparative_Mixer_Analysis.ipynb and click "Run All"

# 3. Export all notebooks to standalone HTML files:
python export.py

# 4. Open the web portal:
# Double-click index.html in Windows Explorer
```

