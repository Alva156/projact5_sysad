from ncclient import manager
from config.device_config import DEVICE
from webex_notify import send_webex_message

def main():
    try:
        with manager.connect(
            host=DEVICE["host"],
            port=DEVICE["port"],
            username=DEVICE["username"],
            password=DEVICE["password"],
            hostkey_verify=False
        ) as mgr:
            print("Connected to device.")
            # Step 1: Verify initial config
            initial_config = mgr.get_config(source="running").data_xml
            print("Initial Configuration:\n", initial_config)

            # Step 2: Make changes
            interfaces = [
                ("GigabitEthernet0/1", "Updated by NETCONF 1"),
                ("GigabitEthernet0/2", "Updated by NETCONF 2"),
                ("GigabitEthernet0/3", "Updated by NETCONF 3")
            ]
            for interface_name, description in interfaces:
                edit_interface_description(mgr, interface_name, description)

            # Step 3: Verify changes
            updated_config = mgr.get_config(source="running").data_xml
            print("Updated Configuration:\n", updated_config)

            # Step 4: Notify WebEx Teams
            message = "Interface descriptions updated successfully by NETCONF automation."
            send_webex_message(message)
            print("Notification sent to WebEx Teams.")

    except Exception as e:
        print(f"An error occurred: {e}")
        send_webex_message("Automation failed. Check logs for details.")

if __name__ == "__main__":
    main()
