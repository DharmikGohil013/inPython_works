import subprocess


def show_wifi_networks():
    try:
        # Run the 'netsh wlan show networks' command
        result = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True, shell=True)

        # Print the result
        print("Available Wi-Fi Networks:\n")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function
show_wifi_networks()
