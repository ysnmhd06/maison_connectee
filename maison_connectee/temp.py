import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Temp(Node):
    def __init__(self):
        super().__init__('temp')
        self.pub = self.create_publisher(Float32, 'temp', 10)
        self.timer = self.create_timer(5.0, self.envoi_temp)

    def envoi_temp(self):
        valeur = random.uniform(15.0, 30.0)
        self.pub.publish(Float32(data=valeur))
        self.get_logger().info(f'Température : {valeur}')

def main():
    rclpy.init()
    node = Temp()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
