# Plasma Workspace 6.8.1 X11 session port

This OBS package source is an experimental forward-port for Plasma Workspace 6.8.1. It attempts to restore the X11 launcher, login entry, systemd target, and selected X11 Workspace code while retaining the Wayland session and 6.8 XWayland setup utility.

## Source identity

- `plasma6-workspace.spec` is based on the openSUSE Factory 6.8.1 package recipe.
- `_service` fetches `plasma-workspace-6.8.1.tar.xz` and checks SHA-256 `e2abb7e5b5fc8d59fe369d3ab4ea776e10684af0fb1a8a3275e9df64eff97d20`.
- `0001-Restore-X11-session-on-plasma-6.8.1.patch` restores selected removed paths against that release archive.
- `0002-Evrisselle-session-branding.patch` supplies the branded SDDM session entry.
- `0003` through `0010` restore or adapt additional X11 APIs, KRDB linkage, XWayland helper lookup, and tray pointer handling.
- The openSUSE patches, keyring, and configuration files are included from the matching package source.

The generated session package depends on the separately packaged `kwin6-x11`. The active package recipe enables `WITH_X11_SESSION`. Source identity is pinned, but a pin alone does not prove patch correctness, license compliance, or runtime behavior.

## Status and evidence limits

Earlier project notes report a successful RPM build and an initial disposable-VM X11 login followed by a Wayland login. The repository does not include the exact build environment, dependency snapshot, commands, complete logs, VM transcript, or resulting RPM checksums needed to reproduce those reports.

The maintainer reports that an earlier X11 experiment produced a black screen and empty panel on the target Mac Pro 5,1. The cause is unresolved and this port is not accepted as usable. Plasma Wayland must remain the stable fallback. No build or target test was performed for this revision. Do not install the 6.7.5 `kwin6-x11` binary against Plasma 6.8.1.

Before release, publish the complete build environment and commands, full logs, output checksums, and repeatable VM acceptance results, including a usable X11 panel and preserved Wayland login.
