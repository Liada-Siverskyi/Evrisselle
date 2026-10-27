# KWin X11 candidate for Ionis Undecima

This recipe packages the SonicDE `sonic-win` community fork at commit `02cfdd70b575d0732a92e0311a30c93e5fa823df` (recorded upstream date: 2026-10-25). The fork installs `libkwin-x11.so.6` and plugins separately from the distribution's Wayland KWin files. The package retains the `sonic-win` executable and adds `kwin_x11` and `plasma-kwin_x11.service` compatibility links for the restored Plasma X11 startup path.

`_service` verifies SHA-256 `67bdd3641dd9b61f9e6b5a33c080a0006743e01813072b3278fcd394ce667412` for the archive fetched from the pinned commit. The spec declares the `WindowView` QML capability registered by the effect's C++ code. This is a candidate downstream implementation, not an official KDE KWin release.

## Status and evidence limits

Earlier project notes report a successful isolated build and an initial disposable-VM X11 login followed by a Wayland login. They also record a staged file-overlap check and a KDecoration3 symbol check. The repository does not include the exact environment, dependency snapshot, commands, full logs, or output RPM checksums needed to reproduce these reports. No build or runtime test was performed for this revision.

The maintainer reports that an earlier X11 experiment showed a black screen and empty panel on the target Mac Pro 5,1. This candidate is not accepted as usable; the failure is unresolved and Wayland must remain the stable fallback. Do not infer that separate package paths guarantee ABI compatibility or a working desktop.

The Workspace package declares `kwin6-x11 >= 6.8.0`. Wayland remains supplied by the distribution packages and must not be removed or replaced. A release requires reproducible build records and repeatable X11 and Wayland VM acceptance evidence.
