import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BPStore(Node):
    def __init__(self):
        super().__init__('bp_store')
        self.pub = self.create_publisher(String, 'evenement_horaire', 10)

    def envoyer_commande(self):
        while rclpy.ok():
            commande = input("\n[BP Store] Tapez 'monter' ou 'descendre' : ").strip().lower()
            if commande in ['monter', 'descendre']:
                self.pub.publish(String(data=f"BP Store : {commande}"))
                print(f"[BP Store] ✅ Commande envoyée : {commande}")
            else:
                print("[BP Store] ❌ Commande invalide.")

def main():
    rclpy.init()
    node = BPStore()
    try:
        node.envoyer_commande()
    except KeyboardInterrupt:
        print("Arrêt du bouton store.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
