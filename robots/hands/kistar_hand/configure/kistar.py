# Copyright (c) 2024
# PRIME Lab at KIST AI Robot Research Center
# Contributor: Chanyoung Ahn

"""Configuration for the KISTAR Hand robots from PRIME Lab.

The following configurations are available:

* :obj:`KISTAR_HAND_CFG`: Allegro Hand with implicit actuator model.

"""


import math

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils.assets import ISAACLAB_ASSETS_PRIME_DIR

##
# Configuration
##

KISTAR_HAND_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ISAACLAB_ASSETS_PRIME_DIR}/kistar_hand/kistar_hand.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            enable_gyroscopic_forces=False,
            max_depenetration_velocity=10.0,
            max_contact_impulse=1e32,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=8,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.0005,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        rot=(0.5, 0.5, -0.5, 0.5),
        joint_pos={".*": 0.0},
    ),
    actuators={
        "fingers": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            effort_limit_sim=2.97,
            velocity_limit_sim=2.66,
            stiffness={
                "index_joint_0": 5.898, "index_joint_1": 2.567,
                "index_joint_2": 3.0,   "index_joint_3": 10.172,
                "middle_joint_0": 3.553, "middle_joint_1": 4.411,
                "middle_joint_2": 3.0,   "middle_joint_3": 10.172,
                "ring_joint_0": 2.888, "ring_joint_1": 3.0,
                "ring_joint_2": 3.0,   "ring_joint_3": 10.760,
                "thumb_joint_0": 5.350, "thumb_joint_1": 3.0,
                "thumb_joint_2": 3.0,   "thumb_joint_3": 7.183,
            },
            damping={
                "index_joint_0": 1.0,    "index_joint_1": 0.8238,
                "index_joint_2": 0.1,    "index_joint_3": 0.01,
                "middle_joint_0": 0.4793, "middle_joint_1": 0.05,
                "middle_joint_2": 0.1,    "middle_joint_3": 2.0,
                "ring_joint_0": 0.8899, "ring_joint_1": 0.1,
                "ring_joint_2": 0.1,    "ring_joint_3": 2.0,
                "thumb_joint_0": 1.0,   "thumb_joint_1": 0.1,
                "thumb_joint_2": 0.1,   "thumb_joint_3": 0.01,
            },
            armature={
                "index_joint_0": 0.02, "index_joint_1": 0.0,
                "index_joint_2": 0.0,  "index_joint_3": 0.03,
                "middle_joint_0": 0.02, "middle_joint_1": 0.0,
                "middle_joint_2": 0.0,  "middle_joint_3": 0.03,
                "ring_joint_0": 0.02, "ring_joint_1": 0.0,
                "ring_joint_2": 0.0,  "ring_joint_3": 0.03,
                "thumb_joint_0": 0.05, "thumb_joint_1": 0.0,
                "thumb_joint_2": 0.0,  "thumb_joint_3": 0.05,
            },
            friction=0.00209,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)
"""Configuration of KISTAR Hand robot."""
