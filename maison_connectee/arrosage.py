import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Arrosage(Node):
    def __init__(self):
        super().__init__('arrosage')
        self.sub = self.create_subscription(String, 'commande_arrosage', self.controler_arrosage, 10)
        print("Système d'arrosage prêt.")

    def controler_arrosage(self, msg):
        if msg.data == "activer":
            print("Arrosage activé pour 5 minutes.")
            time.sleep(300)
            print("Arrosage terminé.")

def main():
    rclpy.init()
    node = Arrosage()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

