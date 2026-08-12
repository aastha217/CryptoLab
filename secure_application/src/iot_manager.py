import os

devices = {}


def register():
    device_id = input("Enter device ID: ")
    name = input("Enter device name: ")
    device_type = input("Enter device type: ")

    devices[device_id] = {
        "name": name,
        "type": device_type,
        "status": "ONLINE",
        "config": ""
    }

    print("Device registered successfully.")


def status():
    device_id = input("Enter device ID: ")

    if device_id in devices:
        print("Device Name:", devices[device_id]["name"])
        print("Device Type:", devices[device_id]["type"])
        print("Status:", devices[device_id]["status"])
    else:
        print("Device not found.")


def firmware():
    device_id = input("Enter device ID: ")
    path = input("Enter firmware file path: ")

    if device_id not in devices:
        print("Device not found.")
        return

    try:
        file = open(path, "r") #vulnerability
        data = file.read()
        file.close()

        print("Firmware uploaded successfully.")
        print("Size:", len(data), "bytes")

    except:
        print("Firmware upload failed.")


def configure():
    device_id = input("Enter device ID: ")

    if device_id not in devices:
        print("Device not found.")
        return

    config = input("Enter configuration: ")
    devices[device_id]["config"] = config

    print("Configuration updated.")


def check_connection():
    device = input("Enter device address: ")

    command = "ping -c 1 " + device #vulnerability
    os.system(command)


while True:

    print("\n==============================")
    print("     IoT DEVICE MANAGEMENT")
    print("==============================")
    print("1. Register Device")
    print("2. View Device Status")
    print("3. Upload Firmware")
    print("4. Configure Device")
    print("5. Check Device Connection")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        status()

    elif choice == "3":
        firmware()

    elif choice == "4":
        configure()

    elif choice == "5":
        check_connection()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")