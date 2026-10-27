# Technical audit

## Scope and freshness

This document summarizes source-level observations recorded on 2026-10-26 and reported environment details. The repository does not contain the raw command output, build logs, VM transcript, or package checksums needed to reproduce the environment reports. No current connection to the Mac Pro was made for this audit. The maintainer reports that an earlier X11 experiment produced a black screen and empty panel; this remains unresolved. Plasma Wayland is the required stable fallback.

## Target profile

The selected hardware is a Mac Pro 5,1 running openSUSE Tumbleweed x86_64. Older project notes recorded Tumbleweed snapshot 20261017 and Plasma 6.8.1-era packages on the target. These notes are historical and must not be taken as a current package inventory or authorization to change the machine. No package or session changes were made in this source task.

## Upstream transition

KDE's Plasma 6.8 release notes and changelog describe retirement of starting Plasma X11 sessions while continuing to support X11 applications through XWayland. The 6.8.1 `plasma-workspace` CMake source still declares `WITH_X11_SESSION`, but the project's audit found no target wired to that option. The X11 launcher, login-session template, and `plasma-workspace-x11.target` are absent from the 6.8.1 source archive compared with 6.7.5.

KWin 6.8.1 builds `kwin_wayland`; its `KWIN_BUILD_X11` option covers X11/XWayland support used by the Wayland compositor, not a standalone `kwin_x11` binary. The package source therefore uses a separate SonicDE `sonic-win` tree pinned by commit in the recipe.

See [the forward-port audit](forward-port-audit.md) for the file-level audit notes and linked upstream sources.

## Build and runtime status

During this source review, both archives were fetched from their pinned public URLs and their SHA-256 values matched the checked-in OBS `_service` definitions: Plasma Workspace 6.8.1 `e2abb7e5b5fc8d59fe369d3ab4ea776e10684af0fb1a8a3275e9df64eff97d20`; SonicDE `sonic-win` commit `02cfdd70b575d0732a92e0311a30c93e5fa823df`, `67bdd3641dd9b61f9e6b5a33c080a0006743e01813072b3278fcd394ce667412`. This confirms the downloaded archive bytes matched the pins on 2026-10-27; it does not validate the source's contents, patch application, build, license status, or runtime behavior.

The package READMEs record an earlier isolated Tumbleweed build and initial disposable-VM X11 and Wayland login checks. They lack the exact container image or repository snapshot, dependency manifest, commands, build logs, and RPM checksums needed for independent reproduction. These are historical maintainer reports, not verified results of this audit.

The later black-screen / empty-panel report shows the X11 port is not accepted on the target. No claim is made here that the X11 session currently works, that the target is in any particular installed state, or that Wayland was tested during this turn. Diagnose and validate in a disposable environment before proposing target changes.

## References

- [Plasma 6.8 release announcement](https://kde.org/announcements/plasma/6/6.8.0/)
- [Plasma 6.7.5–6.8.0 complete changelog](https://kde.org/announcements/changelogs/plasma/6/6.7.5-6.8.0/)
- [KWin X11 removal commit](https://invent.kde.org/plasma/kwin/-/commit/0b6decb103b01187d7665cc9942687df1f1ff22f)
- [KDE `kwin-x11` source package in OBS](https://api.opensuse.org/public/source/home:cfeck:Plasma-X11/kwin6-x11)
- [openSUSE Plasma X11 RPM repository](https://download.opensuse.org/repositories/home:/cfeck:/Plasma-X11/openSUSE_Tumbleweed/)
