#!/usr/bin/env python

import rospy 
import numpy as np
from ta_lab4.srv import *
import Utils
from nav_msgs.srv import GetMap

PLANNER_SERVICE_TOPIC = '/planner_node/get_plan'

SOURCE = [700,  2250, 0.0]
TARGET = [2600,  2030, 0.0]

if __name__ == '__main__':

  rospy.init_node('planner_test', anonymous=True)

  map_service_name = rospy.get_param("~static_map", "static_map")
  print("Getting map from service: ", map_service_name)
  rospy.wait_for_service(map_service_name)
  map_info = rospy.ServiceProxy(map_service_name, GetMap)().map.info

  rospy.wait_for_service(PLANNER_SERVICE_TOPIC)
  get_plan = rospy.ServiceProxy(PLANNER_SERVICE_TOPIC, GetPlan)
  
  try:
    resp = get_plan(Utils.map_to_world(SOURCE, map_info),Utils.map_to_world(TARGET,map_info))
    print np.array(resp.plan).reshape(-1,3)
    print resp.success
  except rospy.ServiceException, e:
    print 'Service call failed: %s'%e

