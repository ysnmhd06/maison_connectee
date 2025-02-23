from flask import Flask, render_template, request, redirect, url_for
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32

app = Flask(__name__)
rclpy.init()

class WebNode(Node):
    def __init__(self):
        super().__init__('web_node')
        self.temp = 0.0
        self.clim = "Système en veille"
        self.portail = "Fermé"
        self.store = "Baissé"
        self.arrosage = "Désactivé"
        self.lumiere = "Éteinte"

        self.create_subscription(Float32, 'temp', self.update_temp, 10)
        self.create_subscription(String, 'etat_clim', self.update_clim, 10)
        self.create_subscription(String, 'etat_portail', self.update_portail, 10)
        self.create_subscription(String, 'etat_store', self.update_store, 10)
        self.create_subscription(String, 'etat_arrosage', self.update_arrosage, 10)
        self.create_subscription(String, 'etat_lumiere', self.update_lumiere, 10)

        self.pub_portail = self.create_publisher(String, 'commande_portail', 10)
        self.pub_store = self.create_publisher(String, 'commande_store', 10)
        self.pub_arrosage = self.create_publisher(String, 'commande_arrosage', 10)

    def update_temp(self, msg):
        self.temp = msg.data

    def update_clim(self, msg):
        self.clim = msg.data

    def update_portail(self, msg):
        self.portail = msg.data

    def update_store(self, msg):
        self.store = msg.data

    def update_arrosage(self, msg):
        self.arrosage = msg.data

    def update_lumiere(self, msg):
        self.lumiere = msg.data

web_node = WebNode()

@app.route('/')
def index():
    return render_template('index.html',
                           temperature=web_node.temp,
                           clim=web_node.clim,
                           portail=web_node.portail,
                           store=web_node.store,
                           arrosage=web_node.arrosage,
                           lumiere=web_node.lumiere)

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    if action == 'portail':
        web_node.pub_portail.publish(String(data="toggle"))
    elif action == 'store':
        web_node.pub_store.publish(String(data="toggle"))
    elif action == 'arrosage':
        web_node.pub_arrosage.publish(String(data="toggle"))
    return redirect(url_for('index'))

def ros_spin():
    rclpy.spin(web_node)

if __name__ == '__main__':
    threading.Thread(target=ros_spin, daemon=True).start()
    app.run(debug=False, use_reloader=False)

