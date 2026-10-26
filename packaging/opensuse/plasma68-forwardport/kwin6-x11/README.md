# KWin X11 candidate for Ionis Undecima

This package uses the pinned SonicDE `sonic-win` source commit `02cfdd70b575d0732a92e0311a30c93e5fa823df` (2026-10-25). It is an X11-focused community fork whose build installs `libkwin-x11.so.6` and plugins under `kwin-x11`, separate from the distribution's Wayland KWin files. The package keeps the upstream `sonic-win` executable and adds the `kwin_x11` and `plasma-kwin_x11.service` compatibility links used by the restored Plasma X11 startup.

The GitHub source archive is SHA-256 pinned in `_service` and its license notices remain in the built package. This is a candidate KWin implementation for the 6.8.1 Workspace session, not an official KDE 6.8.1 KWin release. The effect registers the `org.kde.KWin.Effect.WindowView` QML type from C++; the RPM spec declares that runtime module capability explicitly so the package solver can match its import in the effect QML.

## Build status

- CMake configuration and the full `sonic-win` build succeeded in an isolated openSUSE Tumbleweed 20261024 container with Qt 6.12, KF 6.31, and KDecoration3 6.8.1.
- The target machine has Qt 6.12 and KF 6.31, but KDecoration3 6.8.0. The candidate uses the 6.8.0 API baseline; a symbol check found no unresolved KDecoration3 symbols against the target's 6.8.0 libraries.
- The staged installation contained 1452 files and had no path overlap with the target's installed `kwin6` 6.8.1 package.
- The matched runtime RPMs are `kwin6-x11` and `libkwin-x11-6` 6.8.0-2.1.evrisselle1. In a disposable KDE VM, SDDM launched the X11 session successfully and Wayland also started afterward.

The Workspace session package depends on `kwin6-x11 >= 6.8.0`; it must not require the old 6.7.5 package. Wayland remains supplied by the existing distribution packages and is not removed or replaced. The matched runtime packages are installed on the target. SDDM exposes the branded X11 session and stock Wayland choice; the first X11 login on the target remains to be tried.
