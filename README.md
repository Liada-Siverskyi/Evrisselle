# Evrisselle Ionis Undecima

Evrisselle is the project umbrella. **Ionis Undecima** is its first product: a separately selectable KDE Plasma session running on X11, alongside the system's Plasma Wayland session.

The first target is openSUSE Tumbleweed. The initial implementation targets the Plasma 6.7.5 X11 session path from upstream source and prepares RPM packaging for Tumbleweed. It does not replace the Wayland session or present this work as an official KDE product.

## Current state

The repository now contains the first downstream RPM spec and a small branding patch. The spec is configured to build the existing Plasma X11 startup path and emit an `evrisselle-ionis-undecima-session` package. It also rebuilds the matching `plasma6-workspace` package with X11 session support enabled. The X11 window manager is supplied by openSUSE's separate `kwin6-x11` package.

This is a packaging prototype, not an installable release. It has not yet been built in OBS or tested in a clean virtual machine. The current checkout is on Plasma 6.7.5; future Tumbleweed upgrades need explicit compatibility work because Plasma 6.8 removed the X11 session upstream.

## Project notes

- [Technical architecture and packaging](docs/architecture.md)
- [Decisions and scope](docs/decisions.md)
- [Technical audit](docs/technical-audit.md)
- [Milestones](docs/roadmap.md)
- [Licensing and branding rules](docs/licensing.md)
- [openSUSE packaging source](packaging/opensuse/plasma6-workspace/README.md)
