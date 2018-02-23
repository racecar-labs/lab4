#!/usr/bin/env python

import rospy
import numpy as np
import tf.transformations
import tf

def world_to_map(config, map_info):

  # TODO(avk): simple coversion. NOT consistent with APK.
  scale = 0.02

  xPosition = int(np.floor(config[0]/scale))
  yPosition = int(np.floor(config[1]/scale))
  orientation = config[2]

  return [xPosition, yPosition, orientation]


if __name__ == '__main__':
  print world_to_map([64,64,20])


