import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String

message = "Hi, this works"
print(message)


def image_callback(msg):
    # cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    # print(cv2_img)
    np_arr = np.fromstring(msg.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # print("Received an image!")
    Color_detect(image_np)
    # return image_np;

def Color_detect(image_np):
    max_count = 0
    img_hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img_hsv, (0, 160, 70),(10, 255, 255))
    count = np.sum(mask)
    if count > max_count:
        print("YAYY I can see red!!")
    else:
        print("OOPS! I can no longer see red :(")



def main():
    rospy.init_node('image_listener')
    rospy.Subscriber("/csc22919/camera_node/image/compressed", CompressedImage, image_callback)
    # print("main function works")
    rospy.spin()


if __name__ == '__main__':
    main()
