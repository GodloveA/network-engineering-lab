from netmiko import ConnectHandler
import datetime

devices = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'password',
    }
]

for device in devices:
    conn = ConnectHandler(**device)
    output = conn.send_command("show running-config")
    filename = f"backup_{device['host']}_{datetime.date.today()}.txt"
    with open(filename, "w") as f:
        f.write(output)
    conn.disconnect()
