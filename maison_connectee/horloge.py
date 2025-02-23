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
        self.mode_auto = True  # Par défaut, l'heure suit l'horloge système
        self.get_logger().info("Horloge démarrée. En attente des heures 06:00, 18:00 et 22:00...")

        threading.Thread(target=self.verifier_heure, daemon=True).start()
        threading.Thread(target=self.choisir_heure_manuelle, daemon=True).start()

    def verifier_heure(self):
        heures_cibles = ["06:00", "18:00", "22:00"]
        while rclpy.ok():
            if self.mode_auto:
                self.heure_actuelle = time.strftime('%H:%M')

            self.get_logger().info(f"Heure actuelle : {self.heure_actuelle}")

            if self.heure_actuelle == "06:00":
                self.envoyer_commande("Arrosage")
                self.envoyer_commande("Lever les stores")
            elif self.heure_actuelle == "18:00":
                self.envoyer_commande("Arrosage")
            elif self.heure_actuelle == "22:00":
                self.envoyer_commande("Fermer les stores")

            time.sleep(30)

    def choisir_heure_manuelle(self):
        while rclpy.ok():
            heure_manuelle = input("\nEntrez une nouvelle heure (HH:MM) ou tapez 'auto' pour revenir à l'heure système : ").strip()
            if heure_manuelle.lower() == 'auto':
                self.mode_auto = True
                self.get_logger().info("Mode automatique activé (heure système).")
            elif len(heure_manuelle) == 5 and heure_manuelle[2] == ":" and heure_manuelle[:2].isdigit() and heure_manuelle[3:].isdigit():
                self.heure_actuelle = heure_manuelle
                self.mode_auto = False
                self.get_logger().info(f"Heure manuelle définie : {self.heure_actuelle}")
            else:
                self.get_logger().error("Format incorrect, entrez HH:MM ou 'auto'.")

    def envoyer_commande(self, commande):
        self.pub_evenement.publish(String(data=commande))
        self.get_logger().info(f"Commande envoyée : {commande}")

def main():
    rclpy.init()
    node = Horloge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nHorloge arrêtée.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

