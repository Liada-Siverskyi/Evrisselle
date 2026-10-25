# Technical audit

## Tumbleweed checkout

The target machine currently has `kwin6`, `plasma6-workspace`, and `plasma6-session` at 6.7.5. Its installed files include the Wayland session descriptor and `startplasma-wayland`, but not `kwin_x11`, `startplasma-x11`, or a Plasma entry under `/usr/share/xsessions`. The existing system therefore cannot be repaired by adding only a login-menu shortcut.

The missing pieces are available as separate source/package pieces at the 6.7.5 baseline:

- `plasma-workspace` 6.7.5 has `WITH_X11_SESSION`, the `startplasma-x11` target, and the X11 session desktop template. The session option also enables the X11 workspace build path.
- `kwin-x11` 6.7.5 is a separate KDE source archive and builds `kwin_x11` independently of the Wayland KWin package.
- openSUSE packaging splits the X11 session payload from the Wayland session payload.

The prototype consequently rebuilds Workspace with X11 enabled and uses openSUSE's separately packaged `kwin6-x11`.

## Upstream transition

Plasma 6.8 removed the X11 login-session templates, `startplasma-x11`, and the X11 systemd target; it also removed several X11-specific Workspace and settings paths. The X11 code cannot be recovered on 6.8 by changing one CMake flag. Forward-porting it is a later engineering milestone.

KDE announced Plasma 6.7 as the final release line with an X11 session, with bug-fix support expected into early 2027. This makes 6.7.5 a practical prototype base, while also making version tracking and security backports part of the product's core maintenance work.

## References

- [Plasma 6.8 announcement](https://kde.org/announcements/plasma/6/6.8.0/)
- [KDE's Plasma 6.7 X11 support notice](https://planet.kde.org/david-edmundson-2026-06-02-ex-11-prepping-for-plasmas-last-x11-supported-release/)
- [KDE's X11 support FAQ](https://blogs.kde.org/2025/11/26/going-all-in-on-a-wayland-future/)
- [Plasma 6.7.5 source directory](https://download.kde.org/stable/plasma/6.7.5/)
- [openSUSE OBS Plasma X11 package sources used as packaging reference](https://api.opensuse.org/public/source/home:cfeck:Plasma-X11/plasma6-workspace/)

