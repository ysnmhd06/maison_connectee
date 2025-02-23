import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Lumiere(Node):
    def __init__(self):
        super().__init__('lumiere')
        self.sub = self.create_subscription(String, 'mouvement', self.allumer_lumiere, 10)
        self.etat = "éteinte"

    def allumer_lumiere(self, msg):
        if msg.data == 'mouvement_detecte':
            self.etat = "allumée"
            self.get_logger().info("💡 Lumière allumée (5s)")
            time.sleep(5)
            self.etat = "éteinte"
            self.get_logger().info("💡 Lumière éteinte")

def main():
    rclpy.init()
    node = Lumiere()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

