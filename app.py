from flask import Flask, request

app = Flask(__name__)

# Лог IP-адрес у файл
def log_ip(ip):
    with open("ips.txt", "a") as file:
        file.write(f"IP: {ip} - Запит на сервер\n")

@app.route('/')
def home():
    # Отримуємо IP клієнта
    user_ip = request.remote_addr
    log_ip(user_ip)
    return "Дякую за візит! Ваш IP записаний :)"

@app.route('/logs')
def logs():
    # Читаємо всі збережені IP-адреси
    with open("ips.txt", "r") as file:
        logs = file.read()
    return f"<pre>{logs}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
