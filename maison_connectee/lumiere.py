import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Lumiere(Node):
    def __init__(self):
        super().__init__('lumiere')
        self.sub = self.create_subscription(String, 'detecteur_mouvement', self.activer_lumiere, 10)
        self.etat = "éteinte"
        print("[Lumière] Prête à s'allumer en cas de mouvement.")

    def activer_lumiere(self, msg):
        if msg.data == "détection" and self.etat == "éteinte":
            self.etat = "allumée"
            print("[Lumière] 🔆 Allumée pendant 5 secondes...")
            time.sleep(5)  # Attend 5 secondes
            self.etat = "éteinte"
            print("[Lumière] 💡 Éteinte.")

def main():
    rclpy.init()
    node = Lumiere()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Arrêt de la lumière.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
