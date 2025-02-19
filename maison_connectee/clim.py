import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Clim(Node):
    def __init__(self):
        super().__init__('clim')
        self.sub = self.create_subscription(Float32, 'temp', self.reagir_temp, 10)

    def reagir_temp(self, msg):
        t = msg.data
        if t > 25.0:
            self.get_logger().info(f'Temp : {t}°C -> Clim activée')
        elif t < 18.0:
            self.get_logger().info(f'Temp : {t}°C -> Chauffage activé')
        else:
            self.get_logger().info(f'Temp : {t}°C -> Système en veille')

def main():
    rclpy.init()
    node = Clim()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
