# Plasma Workspace 6.8.1 X11 session port

This OBS package source is an experimental forward-port for the selected Plasma 6.8.1 baseline. It restores the X11 session launcher, login entry, systemd target, and the X11-specific Workspace code removed by KDE during the 6.8 transition, while retaining the Wayland session and the 6.8 XWayland setup utility.

## Source and patches

- `plasma6-workspace.spec` is based on the openSUSE Factory 6.8.1 package recipe.
- The downstream package release uses the `2.1.evrisselle1` suffix so it sorts above the current openSUSE `2.1` build without sharing its package identity.
- `0001-Restore-X11-session-on-plasma-6.8.1.patch` reverses selected KDE source removals against the signed 6.8.1 release source. It also retains current Wayland code where the upstream changes are shared.
- `0002-Evrisselle-session-branding.patch` names the separate login entry `Evrisselle Ionis Undecima` without a redundant protocol suffix.
- `0003` through `0007` restore the X11 task-shading API, its proxy forwarding, Workspace look-and-feel integration, and the `krdb` build target removed during the 6.8 transition.
- `0008` through `0010` fix the restored KRDB linkage, supply the XWayland helper path to the fonts KCM, and capture the tray pointer position used by the 6.8.1 source.
- `_service` fetches the official KDE source archive and verifies SHA-256 `e2abb7e5b5fc8d59fe369d3ab4ea776e10684af0fb1a8a3275e9df64eff97d20`.
- The upstream openSUSE patches, keyring, and configuration files are included from the matching OBS source package.

The RPM recipe explicitly enables `WITH_X11_SESSION`. The generated `evrisselle-ionis-undecima-session` package requires the separate `kwin6-x11` package at version 6.8.0 or newer. The KWin candidate is a pinned community fork, not an official KDE release.

## Status

The ten-patch series applies cleanly during RPM `%prep` against the official `plasma-workspace-6.8.1` source archive. The full CMake build and RPM packaging succeeded in an isolated Tumbleweed container. In a disposable openSUSE KDE VM, SDDM started `Evrisselle Ionis Undecima` with session type `x11`; a subsequent Plasma (Wayland) login also succeeded. Lock/unlock, display changes, suspend/resume, repeated cycles, and uninstall rollback remain untested.

The matched packages were checksum-verified, passed the target's privileged solver dry run, and were installed on the target after a Snapper root snapshot was created. SDDM exposes `Evrisselle Ionis Undecima` and `Plasma (Wayland)`; the active Wayland session remained running. The target's first X11 login and broader session checks remain open. Do not install the 6.7.5 `kwin6-x11` binary against Plasma 6.8.1.
