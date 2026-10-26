# Evrisselle deployment plan

## Goal

Deliver Evrisselle Ionis Undecima as a separately selectable Plasma X11 session on the target openSUSE Tumbleweed x86_64 machine while keeping its ordinary Plasma Wayland session available. The private deployment target is the maintainer's Mac Pro.

## Selected baseline

The implementation targets Plasma 6.8.1, matching the target's current workspace, desktop, and Wayland KWin packages. This is the maintainer's selected route. KDE removed the X11 login path and several X11 runtime paths in Plasma 6.8, so the work requires downstream source changes in KWin and Plasma Workspace. More package changes may be needed after the audit.

The earlier SDDM attempt used `kwin6-x11` and `plasma6-session-x11` at 6.7.5 against the 6.8.1 base and failed. A read-only SSH check before the new install confirmed the old packages were absent while Plasma and Wayland KWin remained at 6.8.1. The matched candidate has now been installed after isolated testing.

## Work sequence

1. Keep `docs/forward-port-audit.md` current as each affected upstream component is inspected.
2. Pin the exact 6.8.1 source revisions and record archive signatures and SHA-256 checksums.
3. Build the separate `kwin6-x11` package from the pinned Sonic-DE community fork and finish the Plasma Workspace patch in `packaging/opensuse/plasma68-forwardport/workspace/`. Add package changes for other components only when the audit demonstrates they are required.
4. Package the changed components as one matched Tumbleweed set. Keep the ordinary Wayland session in the existing distribution package path.
5. Build in OBS or a disposable openSUSE build environment against the same dependency snapshot as the target. Resolve package dependencies and conflicts before making an installer. **Done for the initial matched RPM set** in an isolated Tumbleweed environment.
6. Install into a disposable VM and validate both sessions, lock/unlock, logout, input, display changes, suspend/resume, and X11 applications. Verify uninstall and rollback. **The first X11 login and a subsequent Wayland login passed; repeated cycles and the remaining acceptance checks are open.**
7. Use an SSH installation command that verifies staged checksums, runs a package-manager dry run, prompts for remote privileges, and creates a Snapper root snapshot before package changes. It must not store SSH or sudo credentials. **The one-off command completed without storing credentials.**
8. Run the target dry run and create a pre-install Snapper root snapshot. **Complete on 2026-10-26:** all six checksummed RPMs installed on the maintainer's Mac Pro. The package-manager dry run resolved a 10-package transaction; installation completed, and SDDM contains both `Evrisselle Ionis Undecima` and `Plasma (Wayland)`. The existing Wayland session remained active after the change.
9. Publish package source and instructions only after the isolated acceptance checks pass.

## Installation safeguards

- Never install the current 6.7.5 `kwin6-x11` or `plasma6-session-x11` packages alone against Plasma 6.8.1.
- Preserve the stock Wayland session files and a tested way to select Wayland from SDDM.
- Review the package-manager solver's complete transaction; a repository-priority change does not establish ABI compatibility.
- Require a verified pre-change Btrfs/Snapper snapshot before changing the target packages.
- Keep credentials outside scripts, command history, and Git.
- Treat every Plasma version update as a new compatibility review.

## Current state

SSH key authentication to the target works. Remote `sudo` requires an interactive password, which was entered at the terminal prompt and was not stored. The target has a Btrfs root filesystem and a configured Snapper `root` profile; a pre-install root snapshot was created. The matched candidate RPM set built in an isolated Tumbleweed 20261024 environment. A disposable VM installed the set, logged into the X11 session with `Type=x11`, then successfully started Wayland with `Type=wayland`. On the target, the transaction completed successfully and installed the six matched RPMs plus four solver-selected dependencies. Both session entries are present, and the active session is still Wayland. The user's first X11 login on the Mac Pro remains to be tried from SDDM; broader acceptance checks remain open. The target has KDecoration3 6.8.0 while the build environment has 6.8.1; symbol compatibility was checked.
