import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class Store(Node):
    def __init__(self):
        super().__init__('store')
        self.etat = "monté"  # Par défaut, les stores sont ouverts
        self.sub = self.create_subscription(String, 'evenement_horaire', self.controler_store, 10)
        print("Store prêt à recevoir des commandes.")

    def controler_store(self, msg):
        commande = msg.data
        print(f"Store Commande reçue : {commande}")

        if commande == "Lever les stores" and self.etat == "descendu":
            self.etat = "monté"
            print("Store 📶 En train de monter...")
            time.sleep(2)
            print("Store ✅ Monté complètement.")

        elif commande == "Fermer les stores" and self.etat == "monté":
            self.etat = "descendu"
            print("Store 📶 En train de descendre...")
            time.sleep(2)
            print("Store ❌ Descendu complètement.")

        elif "BP Store : monter" in commande and self.etat == "descendu":
            self.etat = "monté"
            print("Store 📶 En train de monter via le bouton...")
            time.sleep(2)
            print("Store ✅ Monté complètement.")

        elif "BP Store : descendre" in commande and self.etat == "monté":
            self.etat = "descendu"
            print("Store 📶 En train de descendre via le bouton...")
            time.sleep(2)
            print("Store ❌ Descendu complètement.")

def main():
    rclpy.init()
    node = Store()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Arrêt du store.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
