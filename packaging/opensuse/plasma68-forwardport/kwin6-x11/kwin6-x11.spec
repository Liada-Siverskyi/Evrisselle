%define kf6_version 6.26.0
%define qt6_version 6.10.0
%define sonic_commit 02cfdd70b575d0732a92e0311a30c93e5fa823df

Name:           kwin6-x11
Version:        6.8.0
Release:        2.1.evrisselle1
Summary:        KDE KWin X11 window manager for Evrisselle Ionis Undecima
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/Sonic-DE/sonic-win
Source0:        https://github.com/Sonic-DE/sonic-win/archive/%{sonic_commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(Breeze) >= 6.8.0
BuildRequires:  cmake(KDecoration3) >= 6.8.0
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KGlobalAccelD) >= 6.8.0
BuildRequires:  cmake(KNightTime) >= 6.8.0
BuildRequires:  cmake(KScreenLocker) >= 6.8.0
BuildRequires:  cmake(KWayland) >= 6.8.0
BuildRequires:  cmake(Plasma) >= 6.8.0
BuildRequires:  cmake(PlasmaActivities) >= 6.8.0
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.14.0
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdisplay-info) >= 0.2.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.116
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client) >= 1.22
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.38
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) >= 1.10
BuildRequires:  pkgconfig(xcb-dri3) >= 1.10
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-glx) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-present) >= 1.10
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xcb-xinerama) >= 1.10
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon-x11)

Requires:      libkwin-x11-6 = %{version}-%{release}
Requires:      breeze6-decoration >= 6.8.0
Requires:      kdialog
Requires:      kf6-kirigami-imports >= %{kf6_version}
Requires:      kglobalacceld6 >= 6.8.0
Requires:      plasma6-framework-components >= 6.8.0
Requires:      qt6-declarative-imports >= %{qt6_version}
Requires:      qt6-multimedia-imports >= %{qt6_version}
Recommends:    hwdata
Provides:      windowmanager
Provides:      qt6qmlimport(org.kde.kwin_x11)
Provides:      qt6qmlimport(org.kde.kwin_x11.3) = 0
# WindowView registers this module from the effect's C++ constructor at runtime.
Provides:      qt6qmlimport(org.kde.KWin.Effect.WindowView)

%description
KWin X11 is provided from the pinned SonicDE source tree. This package
adds a standalone X11 window manager alongside the distribution's KWin
Wayland package. The upstream binary is retained as sonic-win; kwin_x11
is provided as a compatibility link for Plasma's X11 session launcher.

%package -n libkwin-x11-6
Summary:       KWin X11 runtime library

%description -n libkwin-x11-6
Runtime library used by the standalone KWin X11 window manager.

%package devel
Summary:       KWin X11 development files
Requires:      libkwin-x11-6 = %{version}-%{release}

%description devel
Development files for the standalone KWin X11 library.

%prep
%autosetup -n sonic-win-%{sonic_commit}

%build
%cmake \
  -DBUILD_TESTING=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DKDE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_bindir}
ln -s sonic-win %{buildroot}%{_bindir}/kwin_x11
mkdir -p %{buildroot}/usr/lib/systemd/user
ln -s sonic-win.service %{buildroot}/usr/lib/systemd/user/plasma-kwin_x11.service

%fdupes %{buildroot}%{_datadir}

find %{buildroot} \( -type f -o -type l \) -printf '%p\n' \
  | sed 's#^%{buildroot}##' | sort > %{_builddir}/%{name}-all.files
grep -E '^%{_libdir}/libkwin-x11\.so\.6(\..*)?$' \
  %{_builddir}/%{name}-all.files > %{_builddir}/%{name}-lib.files
grep -E '^%{_libdir}/libkwin-x11\.so$|^%{_libdir}/cmake/KWinX11(/|$)|^%{_libdir}/cmake/KWinX11DBusInterface(/|$)|^%{_includedir}/kwin-x11(/|$)|^/usr/share/dbus-1/interfaces/kwin_x11_' \
  %{_builddir}/%{name}-all.files > %{_builddir}/%{name}-devel.files
grep -Ev '^%{_libdir}/libkwin-x11\.so(\.6(\..*)?)?$|^%{_libdir}/cmake/KWinX11(/|$)|^%{_libdir}/cmake/KWinX11DBusInterface(/|$)|^%{_includedir}/kwin-x11(/|$)|^/usr/share/dbus-1/interfaces/kwin_x11_' \
  %{_builddir}/%{name}-all.files > %{_builddir}/%{name}.files

%preun
%systemd_user_preun sonic-win.service plasma-kwin_x11.service

%post
%systemd_user_post sonic-win.service plasma-kwin_x11.service

%files -f %{_builddir}/%{name}.files
%license LICENSES/*
%doc README.md

%files -n libkwin-x11-6 -f %{_builddir}/%{name}-lib.files
%ldconfig_scriptlets -n libkwin-x11-6

%files devel -f %{_builddir}/%{name}-devel.files
