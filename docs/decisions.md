# Project decisions

| Topic | Decision |
| --- | --- |
| Umbrella project | Evrisselle |
| First product | Evrisselle Ionis Undecima |
| Purpose | Keep a usable Plasma X11 desktop available to people who need X11 |
| First distribution | openSUSE Tumbleweed |
| Target baseline | Plasma 6.8.1 on the user's Tumbleweed system |
| Session model | X11 and Wayland are separate choices in the same login manager |
| Initial implementation | Downstream forward-port of the removed X11 session and runtime paths to Plasma 6.8.1 |
| KWin | Package the pinned Sonic-DE `sonic-win` community fork as a separate `kwin6-x11`; do not reuse the 6.7.5 binary |
| Maintenance | Solo maintainer, best-effort updates and compatibility fixes, no SLA |
| Public release | After a clean build and isolated-session acceptance checks |

## Selected engineering scope

Plasma 6.8.1 is the chosen baseline. The work restores the X11 session startup path and the runtime code needed by a usable Plasma desktop, while preserving the distribution's Wayland session. The matched `sonic-win` KWin and Workspace RPMs built and passed an initial disposable-VM login check for both X11 and Wayland. They are now installed on the Mac Pro after a successful solver dry run and pre-install Snapper snapshot. Both SDDM choices are present, and the active Wayland session remains available; the first target X11 login and broader acceptance checks remain open.

KDE removed more than a CMake switch in 6.8. The workspace no longer builds `startplasma-x11` or installs the X11 session and systemd target; KWin's 6.8.1 source no longer builds `kwin_x11`; and Workspace components lost several X11 code paths. The 6.7.5 packaging prototype is not compatible with the selected baseline.

## Release and safety boundary

- Do not publish or describe the source as a working 6.8.1 X11 session until it builds and passes the isolated VM acceptance checks.
- Do not install the existing 6.7.5 X11 RPMs against the target's 6.8.1 stack.
- Keep source archives, signatures, checksums, patches, and build instructions reproducible.
- Keep SSH and sudo credentials out of scripts and Git.
- Preserve a working Wayland login and a tested Btrfs/Snapper rollback path.
- Do not use KDE logos or claim official KDE support or endorsement.

## Fallback

The earlier 6.7.5 prototype remains a separate fallback if the 6.8.1 forward-port proves impractical. Switching to it would require a new explicit decision and a complete package-set dry run; it is not the active implementation.
