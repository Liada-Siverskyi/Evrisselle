# Evrisselle Ionis Undecima

Evrisselle is the project umbrella. **Ionis Undecima** is its first product: a separately selectable KDE Plasma X11 session alongside the system's Plasma Wayland session.

The first target is openSUSE Tumbleweed. The maintainer selected Plasma 6.8.1 as the starting baseline and the project is auditing and forward-porting the removed X11 session support. It does not replace Wayland or claim to be an official KDE product.

## Current state

The repository contains a Plasma Workspace 6.8.1 port and a separately packaged KWin X11 community fork. The matched RPM set built in an isolated Tumbleweed environment and passed an install-and-login check in a disposable KDE VM: SDDM launched `Evrisselle Ionis Undecima` as an X11 session, and Plasma (Wayland) also started afterward. The six checksum-verified RPMs are now installed on the target Mac Pro. SDDM has separate `Evrisselle Ionis Undecima` and `Plasma (Wayland)` entries; the active Wayland session remained running after installation.

The existing package spec under `packaging/opensuse/plasma6-workspace/` is a 6.7.5 prototype retained as a fallback reference. Do not install its X11 packages against the target machine's 6.8.1 base. The target's stale 6.7.5 X11 runtime library was replaced by the matched set.

See the [selected deployment plan](docs/deployment-plan.md), [forward-port audit](docs/forward-port-audit.md), and [target technical audit](docs/technical-audit.md) before changing the machine.

## Project notes

- [Architecture](docs/architecture.md)
- [Decisions and scope](docs/decisions.md)
- [Forward-port audit](docs/forward-port-audit.md)
- [Target technical audit](docs/technical-audit.md)
- [Milestones](docs/roadmap.md)
- [Deployment plan](docs/deployment-plan.md)
- [Licensing and branding rules](docs/licensing.md)
- [6.7.5 fallback packaging prototype](packaging/opensuse/plasma6-workspace/README.md)
- [Plasma 6.8.1 Workspace port source](packaging/opensuse/plasma68-forwardport/workspace/README.md)
- [KWin X11 candidate package](packaging/opensuse/plasma68-forwardport/kwin6-x11/README.md)
