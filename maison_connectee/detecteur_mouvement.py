import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DetecteurMouvement(Node):
    def __init__(self):
        super().__init__('detecteur_mouvement')
        self.pub = self.create_publisher(String, 'mouvement', 10)

    def detecter(self):
        while rclpy.ok():
            mouvement = input("Détecteur : Tape 'mouvement' pour activer la lumière : ").strip()
            if mouvement.lower() == 'mouvement':
                self.pub.publish(String(data='mouvement_detecte'))
                self.get_logger().info("Mouvement détecté !")

def main():
    rclpy.init()
    node = DetecteurMouvement()
    try:
        node.detecter()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

