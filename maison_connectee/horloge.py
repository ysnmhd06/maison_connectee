import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading
import time

class Horloge(Node):
    def __init__(self):
        super().__init__('horloge')
        self.pub_evenement = self.create_publisher(String, 'evenement_horaire', 10)
        self.heure_actuelle = time.strftime('%H:%M')
        threading.Thread(target=self.verifier_heure, daemon=True).start()
        threading.Thread(target=self.choisir_heure_manuelle, daemon=True).start()

    def verifier_heure(self):
        while rclpy.ok():
            if self.heure_actuelle == "06:00":
                self.envoyer_commande("Lever les stores")
                self.envoyer_commande("Arrosage")
            elif self.heure_actuelle == "22:00":
                self.envoyer_commande("Fermer les stores")
            time.sleep(30)

    def choisir_heure_manuelle(self):
        while rclpy.ok():
            heure_manuelle = input("Entrez une nouvelle heure (HH:MM) : ").strip()
            if ":" in heure_manuelle and len(heure_manuelle) == 5:
                self.heure_actuelle = heure_manuelle
                print(f"Heure définie à : {self.heure_actuelle}")
            else:
                print("Format incorrect, utilisez HH:MM")

    def envoyer_commande(self, commande):
        self.pub_evenement.publish(String(data=commande))
        print(f"Commande envoyée : {commande}")

def main():
    rclpy.init()
    node = Horloge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Horloge arrêtée.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

