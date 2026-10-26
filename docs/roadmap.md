# Roadmap

## MVP acceptance

The 6.8.1 MVP is ready for a private test when a clean build succeeds for the target Tumbleweed snapshot and, in a disposable VM:

1. The existing Plasma Wayland choice remains available and starts normally.
2. `Evrisselle Ionis Undecima` appears as a separate login-manager choice.
3. The X11 session starts a complete Plasma desktop and survives repeated logout/login cycles.
4. Window management, task switching, keyboard layouts, display changes, lock/unlock, suspend/resume, and X11 application launch work.
5. Removing the Evrisselle packages leaves the stock Wayland session usable.
6. The package source, source signatures/checksums, patch series, and installation instructions are published together.

## Milestones

| Milestone | State | Output |
| --- | --- | --- |
| Confirm target package and rollback state | Done | `docs/technical-audit.md` |
| Record the selected 6.8.1 baseline and upstream removals | Done | `docs/decisions.md`, `docs/forward-port-audit.md` |
| Restore KWin's standalone X11 window manager for 6.8.1 | RPM built and tested in the VM | Pinned Sonic-DE `sonic-win` source and recipe in `packaging/opensuse/plasma68-forwardport/kwin6-x11/` |
| Restore Plasma Workspace X11 startup and shell paths | Clean RPM build and VM login passed | `packaging/opensuse/plasma68-forwardport/workspace/` |
| Identify and restore other required Plasma X11 components | Initial matched package set identified; broader hardware/session audit remains | Dependency/source matrix |
| Build the matched package set in OBS | Not started | Successful clean build for target Tumbleweed snapshot |
| Validate both sessions in a disposable VM | X11 and Wayland login checks passed; repeated cycles and suspend/resume remain | Acceptance log and rollback evidence |
| Prepare and run the target installer | Installed on the maintainer's Mac Pro; dry run and pre-install Snapper snapshot completed | First real X11 login on the target |
| Publish the tested MVP source and packages | Source and package recipes are ready locally | Publish the tested source set; broader acceptance checks remain open |

## Release rule

Do not label the port installable or supported until the matched packages build and the VM acceptance checks pass. The first end-to-end session test must happen in a disposable VM, not on the maintainer's daily system.
