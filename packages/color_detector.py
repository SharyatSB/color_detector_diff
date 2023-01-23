import rospy
import numpy as np
import cv2
from sensor_msgs.msg import CompressedImage

# Image call back function. It takes the CompressedImage message and returns a CV2 image
def image_callback(msg):
    # CVbridge does not support CompressedImage type data therefore, numpy is used.
    # Alternatively, frombuffer can also be used.
    np_arr = np.fromstring(msg.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    Color_detect(image_np)

def Color_detect(image_np):
    # initilize max_count variable to 0
    max_count = 0
    # Convert BGR image to HSV
    img_hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

    # Create a mask with the lower and upper HSV values of red color
    mask = cv2.inRange(img_hsv, (0, 160, 70),(10, 255, 255))
    count = np.sum(mask)
    if count > max_count:
        print("YAYY I can see red!!")
    else:
        print("OOPS! I can no longer see red :(")


# main function to initilize image_listener node that subscribes to the camera topic
def main():
    rospy.init_node('image_listener')
    # subscriber function, first argument is the topic, second argument is the topic message type
    # and the last argument is the callback function
    rospy.Subscriber("/csc22919/camera_node/image/compressed", CompressedImage, image_callback)
    # rospy.spin() makes sure that the node keeps running until the program is manually killed.
    rospy.spin()


if __name__ == '__main__':
    main()
