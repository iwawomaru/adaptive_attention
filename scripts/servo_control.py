#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
import wiringpi2
import signal


class ServoControl(object):

    def __init__(self, node_name="servo_control"):

        rospy.init_node(node_name)
        sub = rospy.Subscriber("deg_control", Int16, self.callback)
      
        signal.signal(signal.SIGINT, self.exit_handler)

        self.gp_out = 18
        wiringpi2.wiringPiSetupGpio()
        wiringpi2.pinMode(self.gp_out, wiringpi2.GPIO.PWM_OUTPUT)
        wiringpi2.pwmSetMode(wiringpi2.GPIO.PWM_MODE_MS)
        wiringpi2.pwmSetClock(375)

        self.RIGHT = 56
        self.CENTER = 76
        self.LEFT = 96

        self.current_deg = self.CENTER
        wiringpi2.pwmWrite(self.gp_out, self.current_deg)
        wiringpi2.delay(500)

    def exit_handler(self, signal, frame):
        print ("\nExit")
        wiringpi2.pwmWrite(self.gp_out, self.CENTER)
        wiringpi2.delay(500)
        sys.exit(0)

    def callback(self, deg_control):

        self.current_deg += deg_control
        self.current_deg = min(max(self.RIGHT, self.current_deg), self.LEFT)
        wiringpi2.pwmWrite(self.gp_out, self.current_deg)
        wiringpi2.delay(500)

if __name__ == "__main__":
    obj = ServoControl()
    rospy.spin()

