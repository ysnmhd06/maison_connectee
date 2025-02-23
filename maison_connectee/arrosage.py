import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading
import time

class Arrosage(Node):
    def __init__(self):
        super().__init__('arrosage')
        self.etat = 'arrêté'
        self.sub = self.create_subscription(String, 'evenement_horaire', self.controler_arrosage, 10)
        print("Arrosage prêt à recevoir des commandes.")

    def controler_arrosage(self, msg):
        commande = msg.data
        print(f"Arrosage Commande reçue : {commande}")

        if "Arrosage" in commande and self.etat == 'arrêté':
            self.etat = 'activé'
            print("Arrosage Activé pour 5 minutes.")
            threading.Thread(target=self.eteindre_apres_delai, daemon=True).start()

        elif "BP Arrosage : arrêter" in commande and self.etat == 'activé':
            self.etat = 'arrêté'
            print("Arrosage Arrêté manuellement via bouton.")

    def eteindre_apres_delai(self):
        time.sleep(300)  #5 min
        if self.etat == 'activé':
            self.etat = 'arrêté'
            print("Arrosage eteint après 5 minutes.")

def main():
    rclpy.init()
    node = Arrosage()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Arrêt de l'arrosage.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
