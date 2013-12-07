mesh
====

Quick mesh network setup for Archlinux.  Once enabled, this service connects a device to a specified mesh network on boot.

Setup
-----
This repo is a pacman package.  You can install it like any other [pacman package](https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages).

```
$ sudo pacman -U https://github.com/mgbelisle/mesh/raw/master/mesh.pkg.tar.xz
```

Enabling the mesh service will start it on boot.

```
$ sudo systemctl enable mesh
```

Once started, machines on the mesh are addressable via `hostname.local`.

```
$ ping ares.local
```

Config
------
Configs are set via [/etc/mesh.conf](src/etc/mesh.conf).

Troubleshooting
---------------
* If a machine is not reachable via `hostname.local`, make sure [mdns](https://wiki.archlinux.org/index.php/avahi#Hostname_resolution) is enabled in `/etc/nsswitch.conf`.

```
hosts: files mdns dns myhostname
```
