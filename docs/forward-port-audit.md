# Plasma 6.8.1 X11 forward-port audit

Audit date: 2026-10-26. Source baseline: KDE Plasma 6.8.1 and KWin 6.8.1. Target: the openSUSE Tumbleweed snapshot recorded in `technical-audit.md`.

## Findings

| Component | 6.8.1 source state | Port work |
| --- | --- | --- |
| `plasma-workspace` startup | `WITH_X11_SESSION` is declared but no longer used. The build creates `startplasma-wayland` from the integrated startup program. The X11 launcher, xsessions entry, and X11 systemd target are absent. | Ten downstream patches restore the startup path and X11 runtime code, with the login name `Evrisselle Ionis Undecima`. The clean RPM build completed and the SDDM X11 login passed in a disposable VM. |
| Plasma Shell and Workspace | Plasma 6.8 removed X11 branches from shell, panel, task-manager, keyboard, mouse, and other Workspace features. | The patch series restores the audited X11 branches and session shading/krdb dependencies while retaining Wayland paths. The package set and both login paths passed the initial VM checks; broader acceptance checks remain. |
| KWin | KWin 6.8.1 builds `kwin_wayland`. Its `KWIN_BUILD_X11` option covers X11 common code and Xwayland, not the standalone X11 window manager. Upstream commit [`0b6decb103b0`](https://invent.kde.org/plasma/kwin/-/commit/0b6decb103b01187d7665cc9942687df1f1ff22f) removed standalone mode and backend: 125 files and about 9,200 lines. The separate OBS `kwin6-x11` source still uses 6.7.5. | A pinned Sonic-DE `sonic-win` community fork builds a standalone X11 compositor with separate plugins and libraries. `kwin6-x11` 6.8.0-2.1.evrisselle1 passed the VM login test. Its WindowView QML type is registered by the effect's C++ code; the RPM declares that runtime capability explicitly. This is not an official KDE 6.8.1 release. |
| Other Plasma packages | Not yet fully inventoried. | Extend this table as build/source inspection identifies X11 paths needed by Ionis Undecima. |

The KDE 6.8 changelog records the removal of the X11 startup branch, session/startkde paths, and additional X11-specific shell and Workspace behavior. KDE's release announcement states that starting Plasma X11 sessions is retired while X11 applications continue to run through XWayland. This is a downstream session port, not a supported KDE configuration switch.

## Source checks already performed

- Compared the official `plasma-workspace` 6.7.5 and 6.8.1 release tarballs. In 6.8.1, the `WITH_X11_SESSION` CMake option remains in the top-level file but has no build use; the X11 launcher and session templates from 6.7.5 are absent.
- Prepared `packaging/opensuse/plasma68-forwardport/workspace/0001-Restore-X11-session-on-plasma-6.8.1.patch` from reversions of the relevant upstream removals, preserving the 6.8.1 Wayland XWayland setup utility. `git apply --check` accepts it against the official 6.8.1 source tree. The branded session patch is separate.
- Inspected the official KWin 6.8.1 CMake sources: the installable compositor target is `kwin_wayland`; there is no `kwin_x11` target or `main_x11.cpp`.
- Downloaded the KDE `kwin-x11-6.7.5` release source. It is a separate source tree with an X11 backend and builds `kwin_x11`; it is not present as a 6.8.1 release archive.
- Checked the public OBS sources for `KDE:Frameworks/kwin6-x11` and `home:cfeck:Plasma-X11/kwin6-x11`; both still use `kwin-x11-6.7.5.tar.xz`. There is no matching OBS KWin X11 source for 6.8.1 to reuse.
- Tried reverting the upstream backend-removal commit directly onto the official v6.8.1 tag. The revert conflicts in core files because intervening KWin changes touched those code paths; it needs an actual API port and source review, not a mechanical reversal.
- Before the matched install, inspected the target's package ownership: its `kwin_x11` and `startplasma-x11` files came from 6.7.5 RPMs, while workspace, desktop, and Wayland KWin were 6.8.1. The old X11 runtime was replaced by the matched set on 2026-10-26.
- Checked a Plasma Workspace development branch named `work/asturmlechner/with_x11` (6.8.80 snapshot). Its current `startkde/CMakeLists.txt` still builds only `startplasma-wayland`; it does not provide the missing session startup path.

## Build environment limits

The host has RPM build tools but not the full Plasma development stack. An isolated openSUSE Tumbleweed 20261024 container provided the build environment. Its Qt 6.12 and KF 6.31 match the target, but KDecoration3 is 6.8.1 instead of the target's 6.8.0. The matched runtime packages were installed in a disposable VM; the X11 and subsequent Wayland logins passed. They are also installed on the target after a successful dry run and pre-install Snapper snapshot. The active Wayland session remained running; the first target X11 login is still to be tried.

## References

- [Plasma 6.8 release announcement](https://kde.org/announcements/plasma/6/6.8.0/)
- [Plasma 6.7.5–6.8.0 complete changelog](https://kde.org/announcements/changelogs/plasma/6/6.7.5-6.8.0/)
- [KDE `kwin-x11` 6.7.5 source package in OBS](https://api.opensuse.org/public/source/home:cfeck:Plasma-X11/kwin6-x11)
- [openSUSE Plasma X11 RPM repository](https://download.opensuse.org/repositories/home:/cfeck:/Plasma-X11/openSUSE_Tumbleweed/)
