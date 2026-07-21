$ ping -c 18  google.com

ping -c 9 8.8.8.8

ping -c 9 192.168.5.1


└─▶ $ nmcli device status

DEVICE             TYPE      STATE                   CONNECTION      
wlp0s20f3          wifi      connected               DelhiOffice 1   









└─▶ $ sudo iwconfig wlp0s20f3 power off      (Disable power management:)



$ sudo systemctl restart NetworkManager



sudo nmcli device disconnect wlp0s20f3
sudo nmcli device connect wlp0s20f3



└─▶ $  echo "=== Ping Test ==="; ping -c 10 8.8.8.8; echo "=== WiFi Config ==="; iwconfig; echo "=== WiFi List ==="; nmcli device wifi list



└─▶ $ iwconfig wlp0s20f3    				(Check Power Management)



sudo nmcli connection modify "DelhiOffice 1" 802-11-wireless.bssid D2:21:F9:92:9D:BF
nmcli connection down "DelhiOffice 1"
nmcli connection up "DelhiOffice 1"