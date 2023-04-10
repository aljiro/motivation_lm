#!/usr/bin/python
'''
This is the full robot replay script using the first learning rule for the weights. It subscribes (
via ROS) to the robot's
coordinates, produces the rate
activities according to the model, and replays once a reward has been reached, which is gathered by subscribing to
the reward topic.
'''

import rospy
from std_msgs.msg import UInt8
from geometry_msgs.msg import Pose2D, TwistStamped
import numpy as np
import os
import signal
import sys
import time
import miro2 as miro
import robot_reply_RL
import gc
import json
from rl_logger import RLLogger

logger = RLLogger( False )

class NavigationModel:
	# Inherits the methods from the NetworkSetup class in the main "robot_replay_RL" module. That provides all the
	# methods for network setup and dynamics. See class for a full list of variable names and methods.
	def __init__(self, tau_elig, eta):
		self.t = 0
		self.reward_val = 0

########################################################################################################################
# The main portion of the program that starts the ROS loop, runs the MiRo controller and updates all the model variables
	def step(self, dopamine, ach):
		self.t += 0.01
		coords = np.zeros(2)

		if np.abs(np.sin(self.t/20)) < 0.15:
			self.reward_val = 1
		else:
			self.reward_val = 0

		return self.reward_val, coords



