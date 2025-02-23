import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Portail(Node):
    def __init__(self):
        super().__init__('portail')
        self.etat = "fermé"
        self.sub = self.create_subscription(String, 'commande_portail', self.controler_portail, 10)
        print("Portail prêt.")

    def controler_portail(self, msg):
        if msg.data == "toggle":
            if self.etat == "fermé":
                self.etat = "ouvert"
                print("Ouverture du portail...")
                time.sleep(2)
                print("Portail ouvert.")
            else:
                self.etat = "fermé"
                print("Fermeture du portail...")
                time.sleep(2)
                print("Portail fermé.")

def main():
    rclpy.init()
    node = Portail()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

