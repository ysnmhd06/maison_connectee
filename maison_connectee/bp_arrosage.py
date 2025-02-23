import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BPArrosage(Node):
    def __init__(self):
        super().__init__('bp_arrosage')
        self.pub = self.create_publisher(String, 'commande_arrosage', 10)

    def envoyer_commande(self):
        while rclpy.ok():
            input("Appuyez sur Entrée pour activer l'arrosage...")
            self.pub.publish(String(data="activer"))
            print("Commande arrosage envoyée.")

def main():
    rclpy.init()
    node = BPArrosage()
    try:
        node.envoyer_commande()
    except KeyboardInterrupt:
        print("Arrêt du bouton arrosage.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

