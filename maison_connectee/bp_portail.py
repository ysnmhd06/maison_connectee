import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BPPortail(Node):
    def __init__(self):
        super().__init__('bp_portail')
        self.pub = self.create_publisher(String, 'commande_portail', 10)

    def envoyer_commande(self):
        while rclpy.ok():
            input("Appuyez sur Entrée pour ouvrir/fermer le portail...")
            self.pub.publish(String(data="toggle"))
            print("Commande envoyée : toggle")

def main():
    rclpy.init()
    node = BPPortail()
    try:
        node.envoyer_commande()
    except KeyboardInterrupt:
        print("Arrêt du bouton portail.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

