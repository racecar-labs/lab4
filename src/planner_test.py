#!/usr/bin/env python

import rospy 
import numpy as np
from ta_lab4.srv import *

PLANNER_SERVICE_TOPIC = '/planner_node/get_plan' # The topic at which the service is available

SOURCE = [13.76, 44.88, 1.57]   # Where the plan should start
TARGET = [64,    11,    0.5234] # Where the plan should finish

#SOURCE = [62.72,  53.6, 0.0]
#TARGET = [17.52,  26.48,1.57]

#SOURCE = [53.68,  43.12, 0.0]
#TARGET = [51.76,  20.88, 0.0]

if __name__ == '__main__':

  rospy.init_node('planner_test', anonymous=True) # Initialize the node
  rospy.wait_for_service(PLANNER_SERVICE_TOPIC) # Wait for the service to become available if necessary
  get_plan = rospy.ServiceProxy(PLANNER_SERVICE_TOPIC, GetPlan) # Setup a ros service client
  
  try:
    resp = get_plan(SOURCE,TARGET) # Get the plan from the service
    print np.array(resp.plan).reshape(-1,3) # Reshape the plan to be nx3
    print resp.success
  except rospy.ServiceException, e:
    print 'Service call failed: %s'%e
    

