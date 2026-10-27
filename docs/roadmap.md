# Roadmap

## Current state

The Plasma 6.8.1 Workspace and SonicDE KWin X11 package recipes are experimental source work. Previous project notes reported a successful build and initial disposable-VM login checks, but no logs or reproducible test artifacts are included. The maintainer later reported that the X11 attempt on the target Mac Pro 5,1 showed a black screen and empty panel. That failure is unresolved. The distribution's Wayland session is the required stable fallback.

No package operation, SDDM restart, session switch, or permission change is part of this source task. Do not treat the target as validated or the port as ready to install.

## Milestones

| Milestone | State | Evidence needed |
| --- | --- | --- |
| Select openSUSE Tumbleweed x86_64 and Plasma 6.8.1 baseline | Recorded | `docs/decisions.md`, `docs/technical-audit.md` |
| Audit upstream X11 removals and pin source inputs | Initial notes and source pins exist; audit is incomplete | Reproducible source comparison with revisions and checksums |
| Build matched Workspace and KWin candidate packages | Prior notes report a successful isolated build; not independently reproducible from checked-in artifacts | Build environment definition, complete logs, RPM output checksums |
| Reproduce and diagnose the black-screen / empty-panel failure | Open | Logs and screenshots from an isolated environment; root cause and fix |
| Validate the complete X11 desktop in a disposable VM | Not established by repository evidence | Repeatable login, panel, input, logout, and Wayland-preservation results |
| Validate broader hardware and session behavior | Not started / not evidenced | Display, lock, suspend/resume, applications, rollback, and repeated cycles |
| Establish licensing for original Evrisselle materials | Open | Maintainer-selected license and file-level notices |
| Publish a tested release | Blocked on diagnosis, licensing, and reproducible acceptance evidence | Source, licenses, checksums, build records, and test report together |

## Acceptance criteria

1. Stock Plasma Wayland remains available and starts successfully before and after testing.
2. The branded X11 entry starts a complete desktop with a populated, interactive panel.
3. Repeated login/logout, input, display changes, lock/unlock, suspend/resume, and X11 applications work in a disposable environment.
4. Removing the candidate packages leaves the stock Wayland session usable.
5. Source inputs, license notices, package outputs, and test evidence can be independently checked.

A successful package build does not satisfy these criteria. Do not label the port ready or recommend installation before the acceptance evidence is recorded.
