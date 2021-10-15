#!/usr/bin/env python3
"""Exercice 2 (Partie 4) du TP6"""

def get_login(uid, liste):
    assert isinstance(uid, int)
    assert isinstance(liste, list) 
    for users in liste:
        info = users.split(':')
        if uid == info[2]:
            return info[0]

def main():
    utilisateurs = [
        "usbmux:x:107:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin",
        "dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin",
        "rtkit:x:109:114:RealtimeKit,,,:/proc:/usr/sbin/nologin",
        "lightdm:x:110:115:Light Display Manager:/var/lib/lightdm:/bin/false",
        "cups-pk-helper:x:111:118:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin",
        "speech-dispatcher:x:112:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/false",
        "whoopsie:x:113:119::/nonexistent:/bin/false",
        "kernoops:x:114:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin",
        "saned:x:115:121::/var/lib/saned:/usr/sbin/nologin",
        "pulse:x:116:122:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin",
        "avahi:x:117:124:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin",
        "colord:x:118:125:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin",
        "hplip:x:119:7:HPLIP system user,,,:/var/run/hplip:/bin/false",
        "wurbel:x:1000:1000:Éric Würbel,,,:/home/wurbel:/bin/bash",
    ]

    print(get_login(1000, utilisateurs))
    print(get_login(109, utilisateurs))
    print(get_login(111, utilisateurs))
    print(get_login(1125, utilisateurs))

if __name__ == '__main__':
    main()