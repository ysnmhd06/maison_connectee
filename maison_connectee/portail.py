import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Portail(Node):
    def __init__(self):
        super().__init__('portail')
        self.etat = "fermé"
        self.sub = self.create_subscription(String, 'commande_portail', self.controler_portail, 10)
        print("Portail prêt à être commandé.")

    def controler_portail(self, msg):
        if msg.data == "toggle":
            if self.etat == "fermé":
                self.etat = "ouvert"
                print("Portail 🚪 En train de s'ouvrir...")
                time.sleep(2)  # Simulation de l'ouverture
                print("Portail ✅ Ouvert.")
            else:
                self.etat = "fermé"
                print("Portail 🚪 En train de se fermer...")
                time.sleep(2)  # Simulation de la fermeture
                print("Portail ❌ Fermé.")

def main():
    rclpy.init()
    node = Portail()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Arrêt du portail.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
