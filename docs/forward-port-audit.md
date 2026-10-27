# Plasma 6.8.1 X11 forward-port audit

Audit notes initially recorded on 2026-10-26. Source baseline: KDE Plasma 6.8.1 and KWin 6.8.1. The source-level observations below are not a runtime acceptance result. The maintainer reports a black screen and empty panel during an earlier X11 experiment; the cause remains open.

## Findings

| Component | Source observation | Port work / status |
| --- | --- | --- |
| `plasma-workspace` startup | `WITH_X11_SESSION` is declared in 6.8.1 but the audit found no target using it. The X11 launcher, xsessions entry, and X11 systemd target present in 6.7.5 are absent. | Patch series attempts to restore startup and selected X11 runtime code, with branding `Evrisselle Ionis Undecima`. Patch applicability and previous build success are maintainer-reported; reproducible logs are not checked in. |
| Plasma Shell and Workspace | The 6.8 source removed X11 branches from shell, panel, task manager, keyboard, mouse, and other Workspace features. | Additional patches restore selected branches and dependencies. Completeness and runtime behavior are not established. |
| KWin | KWin 6.8.1 builds `kwin_wayland`; `KWIN_BUILD_X11` covers X11/XWayland support for that compositor, not the standalone X11 WM. Upstream commit [0b6decb103b0](https://invent.kde.org/plasma/kwin/-/commit/0b6decb103b01187d7665cc9942687df1f1ff22f) removed standalone mode and backend. | Separate `kwin6-x11` recipe pins the SonicDE `sonic-win` community fork. It is not an official KDE 6.8.1 release. A previous VM login was reported, but the current X11 failure is unresolved. |
| Other Plasma packages | The full 6.8.1 component set has not been inventoried for X11 dependencies. | Extend the audit only when source review or reproducible builds identify a concrete requirement. |

## Source review notes

- The original audit compared official `plasma-workspace` 6.7.5 and 6.8.1 release tarballs and recorded that the launcher and session templates were absent in 6.8.1.
- The Workspace patch series was reported to apply to the official 6.8.1 source archive. The archive hash is recorded in the package `_service` file.
- The original audit inspected KWin 6.8.1 CMake files and found no standalone `kwin_x11` target or `main_x11.cpp`.
- The `sonic-win` fork source is pinned by commit and archive SHA-256 in the package recipe and `_service` file.
- The original audit reported that a mechanical revert of the upstream KWin backend removal conflicted with intervening changes. A real API port would require source review.
- Prior notes about a disposable VM build/login and target package installation are historical reports; logs and package artifacts are not present here. They are not proof that the X11 desktop works on the target.

## Reproducibility gap

The repository pins input archives but lacks the exact build image, openSUSE repository snapshot, dependency manifest, build commands, full build logs, and output RPM checksums. These must be published before claiming that another maintainer can reproduce the RPM set. A checksum establishes archive identity only; it does not establish runtime correctness.

## References

- [Plasma 6.8 release announcement](https://kde.org/announcements/plasma/6/6.8.0/)
- [Plasma 6.7.5–6.8.0 complete changelog](https://kde.org/announcements/changelogs/plasma/6/6.7.5-6.8.0/)
- [KWin X11 removal commit](https://invent.kde.org/plasma/kwin/-/commit/0b6decb103b01187d7665cc9942687df1f1ff22f)
- [KDE `kwin-x11` source package in OBS](https://api.opensuse.org/public/source/home:cfeck:Plasma-X11/kwin6-x11)
- [openSUSE Plasma X11 RPM repository](https://download.opensuse.org/repositories/home:/cfeck:/Plasma-X11/openSUSE_Tumbleweed/)
