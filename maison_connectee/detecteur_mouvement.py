import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DetecteurMouvement(Node):
    def __init__(self):
        super().__init__('detecteur_mouvement')
        self.pub = self.create_publisher(String, 'detecteur_mouvement', 10)

    def simuler_mouvement(self):
        while rclpy.ok():
            mouvement = input("\n[Détecteur] Tapez 'mouvement' pour simuler une détection : ").strip().lower()
            if mouvement == "mouvement":
                self.pub.publish(String(data="détection"))
                print("[Détecteur] Mouvement détecté !")
            else:
                print("[Détecteur] Commande invalide.")

def main():
    rclpy.init()
    node = DetecteurMouvement()
    try:
        node.simuler_mouvement()
    except KeyboardInterrupt:
        print("Arrêt du détecteur de mouvement.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
