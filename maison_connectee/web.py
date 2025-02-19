from flask import Flask, render_template
import os

# Définir le bon chemin des templates
template_dir = "/home/yassin/ros2_ws/install/maison_connectee/share/maison_connectee/templates"

# Vérifier si le répertoire existe
if not os.path.exists(template_dir):
    print(f"❌ ERREUR : Le dossier des templates n'existe pas ! Vérifie ton installation.")
else:
    print(f"✅ Flask trouve les templates ici : {template_dir}")

# Créer l'application Flask avec le bon chemin
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"❌ ERREUR : {e}")
        return f"Erreur : {e}", 500

if __name__ == "__main__":
    print("✅ Serveur Flask prêt ! Ouvre ton navigateur sur http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
