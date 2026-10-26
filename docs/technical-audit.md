# Technical audit

## Target Tumbleweed system (checked 2026-10-26)

SSH access to the target works. The target reports openSUSE Tumbleweed snapshot 20261017. After the 2026-10-26 installation it has:

- `plasma6-desktop` and Wayland `kwin6` at 6.8.1-1.1 from openSUSE;
- the Evrisselle `plasma6-workspace`, workspace libraries, Plasma session, `kwin6-x11`, and branded session packages at 6.8.1-2.1.evrisselle1 / 6.8.0-2.1.evrisselle1;
- no `plasma6-session-x11`; the branded `Evrisselle Ionis Undecima` session replaces its SDDM role;
- Qt 6.12.0-1.1, KF 6.31.0-1.2, and KDecoration3 6.8.0-1.1.

The earlier X11 SDDM attempt failed while using the incompatible 6.7.5 X11 packages with Plasma 6.8.1. Before the matched install, a read-only SSH check found no `kwin6-x11` or `plasma6-session-x11` package and found an old 6.7.5 `libkwin-x11-6`; the matched transaction replaced that library. The new candidate is now installed, and a real X11 login on the Mac Pro remains to be tried.

The enabled OBS repository contains a wider 6.7.5 Plasma set, but aligning to that set is not the selected plan. The six candidate RPMs were staged and checksum-verified, then installed after a successful package-manager dry run. The transaction also installed four solver-selected dependencies. A Snapper `root` snapshot was created before the package change. Post-install SSH checks confirm all six Evrisselle RPM versions and both SDDM session names; the active Wayland session remains running.

The target root filesystem is Btrfs and `snapper list-configs` reports the `root` configuration. No Plasma package locks are configured. A pre-change `root` snapshot was created before the target transaction.

## Upstream transition

KDE states that Plasma 6.8 retires starting X11 sessions while continuing to support individual X11 applications through XWayland. The 6.7.5-to-6.8.0 changelog records removal of the X11 `startplasma` path, X11 login-session and `startkde` paths, the standalone X11 KWin backend, and multiple Workspace shell and settings paths.

The 6.8.1 `plasma-workspace` CMake file still declares `WITH_X11_SESSION`, but the option no longer controls a target. Its `startkde` build installs `startplasma-wayland` only. The X11 launcher, X11 login template, and `plasma-workspace-x11.target` from 6.7.5 are absent.

KWin 6.8.1 builds `kwin_wayland`; its `KWIN_BUILD_X11` option enables X11/XWayland code used with Wayland, not the standalone X11 window manager. The separate `kwin-x11` release source and the target's installed `kwin_x11` binary are 6.7.5.

See the [forward-port audit](forward-port-audit.md) for source-level findings and remaining components to inspect.

## Current build environment

An isolated openSUSE Tumbleweed 20261024 container produced the matched runtime RPM set: Plasma Workspace and session packages at 6.8.1-2.1.evrisselle1 and KWin X11 at 6.8.0-2.1.evrisselle1. The KWin package explicitly provides the WindowView QML import registered by its own effect code. Qt 6.12 and KF 6.31 match the target; KDecoration3 is 6.8.1 in the build environment and 6.8.0 on the target, with candidate ABI symbols checked. A disposable KDE VM installed the package set and successfully logged into both X11 and Wayland. The target dry run and installation also completed; the SDDM entries are present and the original Wayland session remains active. The target's first X11 login and broader VM acceptance checks remain open.

## References

- [Plasma 6.8 release announcement](https://kde.org/announcements/plasma/6/6.8.0/)
- [Plasma 6.7.5–6.8.0 complete changelog](https://kde.org/announcements/changelogs/plasma/6/6.7.5-6.8.0/)
- [KDE `kwin-x11` 6.7.5 source package in OBS](https://api.opensuse.org/public/source/home:cfeck:Plasma-X11/kwin6-x11)
- [openSUSE Plasma X11 RPM repository](https://download.opensuse.org/repositories/home:/cfeck:/Plasma-X11/openSUSE_Tumbleweed/)
