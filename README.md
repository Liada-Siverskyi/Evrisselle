# Evrisselle Ionis Undecima

Evrisselle is an independent downstream project exploring a separately selectable KDE Plasma X11 session for openSUSE Tumbleweed x86_64. **Ionis Undecima** is the session concept; Plasma (Wayland) remains the distribution-provided session and must remain usable.

This is not an official KDE product. KDE source, the SonicDE KWin fork, and openSUSE packaging retain their own names, licenses, and notices.

## Status

The public source contains experimental packaging for a Plasma Workspace 6.8.1 X11 forward-port and a separately packaged SonicDE KWin X11 fork. The selected target is a Mac Pro 5,1 running openSUSE Tumbleweed x86_64.

The earlier X11 experiment did not produce a usable desktop on the target: the reported result was a black screen with an empty panel. The project is therefore **not ready to install or use**. The stable Wayland session is the required fallback and must be preserved throughout further work. Do not infer a successful target login from package installation or from the historical test notes below.

The repository's previous documentation recorded a clean build and X11/Wayland logins in a disposable VM, as well as a package installation on the target. Those are historical maintainer-reported results; the repository contains no build logs, VM image, test transcript, or hardware capture to independently reproduce them. They do not resolve the black-screen report. No new build or hardware test is claimed by this revision.

## Source layout

- [`packaging/opensuse/plasma68-forwardport/workspace/`](packaging/opensuse/plasma68-forwardport/workspace/) — Plasma Workspace 6.8.1 spec, source service, and downstream patch series.
- [`packaging/opensuse/plasma68-forwardport/kwin6-x11/`](packaging/opensuse/plasma68-forwardport/kwin6-x11/) — candidate KWin X11 package from a pinned SonicDE community-fork commit.
- [`packaging/opensuse/plasma6-workspace/`](packaging/opensuse/plasma6-workspace/) — older 6.7.5 prototype retained for reference; it is not compatible with the selected 6.8.1 stack.
- [`docs/`](docs/) — architecture, decisions, audits, deployment constraints, roadmap, and licensing notes.
- [`docs/change-history.md`](docs/change-history.md) — commit-level summary of the existing public history at the current base revision.

## Safety and release status

Do not install, remove, or replace packages on the Mac Pro as part of this source work. Do not restart SDDM, change login sessions, or alter access permissions. All development and validation should happen in reviewable source branches and disposable build/VM environments. Any future hardware validation must be separately planned after the black-screen failure is understood, with Wayland access and rollback preserved.

The packages and port are experimental. A successful build alone does not establish a working session. See [the technical audit](docs/technical-audit.md), [forward-port audit](docs/forward-port-audit.md), [deployment plan](docs/deployment-plan.md), and [licensing notes](docs/licensing.md) for evidence limits and remaining work.
