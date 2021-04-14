from access_points import get_scanner
import os
import getpass

wifi_scanner = get_scanner()
points=wifi_scanner.get_access_points()

if points:
    print('Your available wifi networks are:')
    for index,i in enumerate(points[:3]):
        print(f">[{index+1}] {i.get('ssid')}")

    n=int(input('Your choice? '))
    password=getpass.getpass('Password:')
    bssid=points[n-1].get('bssid')

    if not os.system(f'nmcli dev wifi connect {bssid} password > /dev/null 2>&1'):
        print('connected!')
    else:print('INVALID')
else:
    print('No Wifi networks found!')