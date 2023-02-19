

#!/usr/bin/env python3
import time
import rospy
# import cancellation_order 
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from inputimeout import inputimeout
def movebase_client():

       # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   
    food_menu=[]    
    list_of_table_no = []

    for i in range(0,3):

        print ('                              food you wish ')
        print ('................................................................................')
        
        food = str (input())
        print ('\n\n')
        print ('                        which table are you in now ?')
        print ('................................................................................')
        table_no = int(input())
        food_menu.append(food)
        list_of_table_no.append(table_no)

    print ("                   food will arrive soon THANK YOU for patience" )
    print ('\n\n')
    goal.target_pose.pose.position.x = 0.2255
    goal.target_pose.pose.position.y =  -1.221
    goal.target_pose.pose.orientation.z = -0.7879
    goal.target_pose.pose.orientation.w = 0.6157
    client.send_goal(goal) 
    wait = client.wait_for_result()

    

    try:

        a = inputimeout(prompt='                        is food have been loaded:', timeout=100)
        print ('\n\n')
        if a =='yes':
        
            for table_no in list_of_table_no:
                
                    # if x == 3:
                    #     break

                    if table_no == 3:
                                goal.target_pose.pose.position.x =1.47407
                                goal.target_pose.pose.position.y = 0.2726
                                goal.target_pose.pose.orientation.z = -0.983
                                goal.target_pose.pose.orientation.w =  0.1796
                                client.send_goal(goal) 
                                wait = client.wait_for_result()

                                print("                              table 3 reached")
                                print ('................................................................................')
                                print ('\n\n')
                                try:
                                    f = inputimeout(prompt=' please give acknowledgement that you have taken the food from the robot:', timeout=100)
                                    print ('................................................................................')
                                    print ('\n\n')

                                    if f== 'yes':
                                     print( '                        thank you for your response ')
                                     print ('................................................................................')
                                     print ('\n\n')
                                     print('      Do you want to cancel your order >> then specify your table no ')
                                      
                                     print ('................................................................................')
                                     i = int(input())
                                     print ('\n\n')
                                     if i == 0 or 1 or 2:
                                       list_of_table_no.pop(i)
                                       x= x+1

                                     if x == 3:
                                        goto_home()
                                    continue
                                 
                                except Exception:
                                        
                                        continue
                                
                        

                    if table_no == 2:
                                goal.target_pose.pose.position.x = 0.0302
                                goal.target_pose.pose.position.y =  1.1524
                                goal.target_pose.pose.orientation.z =0.696
                                goal.target_pose.pose.orientation.w = 0.7170
                                
                                client.send_goal(goal) 
                                wait = client.wait_for_result()
                                
                                print("                              table 2 reached")
                                print ('................................................................................')
                                print ('\n\n')
                                try:
                                    e = inputimeout(prompt=' please give acknowledgement that you have taken the food from the robot:', timeout=100)
                                    
                                    print ('................................................................................')
                                    print ('\n\n')
                                    if e== 'yes':
                                       print( '                        thank you for your response ')
                                       print ('................................................................................')
                                       print ('\n\n')
                                       print('     Do you want to cancel your order >> then specify your table no ')
                                       
                                       print ('................................................................................')
                                       i = int(input())
                                       print ('\n\n')
                                       if i == 0 or 1 or 2:
                                        list_of_table_no.pop(i)
                                        x= x+1

                                       if x == 3:
                                        goto_home()
                                    continue

                                except Exception:
                                    
                                        continue
                                
                    
                    if table_no == 1:
                                goal.target_pose.pose.position.x = -1.2816
                                goal.target_pose.pose.position.y =  0.16817
                                goal.target_pose.pose.orientation.z =-0.993
                                goal.target_pose.pose.orientation.w =-0.1156
                                client.send_goal(goal) 
                                wait = client.wait_for_result()

                                print("                              table 1 reached")
                                print ('................................................................................')
                                print ('\n\n')

                                try:
                                    d = inputimeout(prompt=' please give acknowledgement that you have taken the food from the robot:', timeout=100)
                                    print ('................................................................................')
                                    print ('\n\n')
                                    if d== 'yes':
                                     print( '                        thank you for your response ')
                                     print ('................................................................................')
                                     print ('\n\n')
                                     print('     Do you want to cancel your order >> then specify your table no ')
                                     
                                     print ('................................................................................')
                                     i = int(input())
                                     print ('\n\n')
                                     if i == 0 or 1 or 2:
                                       list_of_table_no.pop(i)
                                       x= x+1

                                     if x == 3:
                                        goto_home()
                                    continue
                                    
                                except Exception:
                                    
                                        continue
                            
        print('                              going to kitchen')
        print ('................................................................................')
        print ('\n\n')
        goal.target_pose.pose.position.x = 0.2255
        goal.target_pose.pose.position.y =  -1.221
        goal.target_pose.pose.orientation.z = -0.7879
        goal.target_pose.pose.orientation.w = 0.6157
        client.send_goal(goal) 
        wait = client.wait_for_result()
        print ('                          going to home position')
        print ('................................................................................')
        print ('\n\n')
        goal.target_pose.pose.position.x = 0.08001
        goal.target_pose.pose.position.y = 0.0389
        goal.target_pose.pose.orientation.z =   -0.998
        goal.target_pose.pose.orientation.w = 0.058
        client.send_goal(goal) 
        wait = client.wait_for_result()
                 

    except Exception:
                   
                    print ('going to home position')
                    goal.target_pose.pose.position.x = 0.08001
                    goal.target_pose.pose.position.y = 0.0389
                    goal.target_pose.pose.orientation.z =   -0.998
                    goal.target_pose.pose.orientation.w = 0.058
                    client.send_goal(goal) 
                    wait = client.wait_for_result()
                
    def goto_home():
        print('going to kitchen')
        goal.target_pose.pose.position.x = 0.2255
        goal.target_pose.pose.position.y =  -1.221
        goal.target_pose.pose.orientation.z = -0.7879
        goal.target_pose.pose.orientation.w = 0.6157
        client.send_goal(goal) 
        wait = client.wait_for_result()
        print ('going to home position')
        goal.target_pose.pose.position.x = 0.08001
        goal.target_pose.pose.position.y = 0.0389
        goal.target_pose.pose.orientation.z =   -0.998
        goal.target_pose.pose.orientation.w = 0.058
        client.send_goal(goal) 
        wait = client.wait_for_result()

if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        rospy.loginfo(" Goal execution done!")
      
        if result:
            rospy.loginfo("Goal execution done!"+str(result))
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
