import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading
import time

class Horloge(Node):
    def __init__(self):
        super().__init__('horloge')
        self.pub_evenement = self.create_publisher(String, 'evenement_horaire', 10)
        self.heure_actuelle = time.strftime('%H:%M')  # Heure système
        print("[Horloge] Démarrée. En attente des heures 06:00, 18:00 et 22:00...")

        # Lancer deux threads : un pour surveiller l'heure, un pour modifier l'heure manuellement
        threading.Thread(target=self.verifier_heure, daemon=True).start()
        threading.Thread(target=self.choisir_heure_manuelle, daemon=True).start()

    def verifier_heure(self):
        """ Vérifie l'heure et déclenche les événements aux heures définies """
        while rclpy.ok():
            print(f"[Horloge] Heure actuelle : {self.heure_actuelle}")

            if self.heure_actuelle == "06:00":
                self.envoyer_commande("Arrosage")
                self.envoyer_commande("Lever les stores")

            elif self.heure_actuelle == "18:00":
                self.envoyer_commande("Arrosage")

            elif self.heure_actuelle == "22:00":
                self.envoyer_commande("Fermer les stores")

            time.sleep(30)  # Vérification toutes les 30 secondes

    def choisir_heure_manuelle(self):
        """ Permet de modifier l'heure pour tester immédiatement """
        while rclpy.ok():
            heure_manuelle = input("\n[Manuel] Entrez une nouvelle heure (HH:MM) : ").strip()
            if ":" in heure_manuelle and len(heure_manuelle) == 5:
                self.heure_actuelle = heure_manuelle
                print(f"[Horloge] ⏳ Nouvelle heure définie : {self.heure_actuelle}")
            else:
                print("[Erreur] Format incorrect, entrez HH:MM")

    def envoyer_commande(self, commande):
        """ Envoie une commande sur le topic `evenement_horaire` """
        self.pub_evenement.publish(String(data=commande))
        print(f"[Horloge] ✅ Commande envoyée : {commande}")

def main():
    rclpy.init()
    node = Horloge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Arrêt de l'horloge.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
