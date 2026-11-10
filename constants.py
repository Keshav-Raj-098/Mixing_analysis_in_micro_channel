observation_surface_distance = [1.5,2.0,2.5,3.0,3.5,4.0]  # in mm  

width_cross_section = 0.2 # in mm
height_cross_section = 0.1 # in mm

L_mixing = 3 # in mm
L_in = 1 # in mm
L_total = 1 # in mm


# reynold's number vs velocity
RE_VS_VEL = {
    25 : 0.1675,
    50 : 0.3349,
    100 : 0.6698,
    250 : 1.6745,
    500 : 3.3490
}



# Mesh STATS

# ------------- T_MIXER_MESH ---------------- 

T_MESH_SIZE = 0.00001  # in m
T_MESH_NODES = 115731
T_MESH_ELEMENTS = 100000


# ----------------- Y_Mixer_MESH ------------

Y_MESH_ELEMNET_SIZE = 0.00005 # in m
Y_MESH_NODES = 1539
Y_MESH_ELEMENTS = 814

# ----------------- SR_Mixer_MESH ------------

SR_MESH_ELEMNET_SIZE = 0.000025 # in m
SR_MESH_NODES = 14400
SR_MESH_ELEMENTS = 10344
