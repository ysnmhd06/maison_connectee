import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BPArrosage(Node):
    def __init__(self):
        super().__init__('bp_arrosage')
        self.pub = self.create_publisher(String, 'evenement_horaire', 10)

    def envoyer_commande(self):
        while rclpy.ok():
            commande = input("\nBP Arrosage Tapez 'activer' ou 'arreter' : ").strip().lower()
            if commande in ['activer', 'arrêter']:
                self.pub.publish(String(data=f"BP Arrosage : {commande}"))
                print(f"BP Arrosage Commande envoyée : {commande}")
            else:
                print("BP Arrosage Commande invalide.")

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
