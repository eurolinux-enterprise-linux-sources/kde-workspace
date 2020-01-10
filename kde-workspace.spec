%if 0%{?fedora}
%define gpsd 1
%endif
%if 0%{?fedora} || 0%{?epel}
%define webkit 1
%define libqalculate 1
%endif

%if 0%{?fedora} < 20 || 0%{?rhel} <= 7
%define nepomuk 1
%endif

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
# Require kscreen, omit kcontrol/randr bits
%define kscreen 1
%endif

%if 0%{?fedora} > 17 || 0%{?rhel} > 6
%define systemd_login1 1
%endif

Summary: KDE Workspace
Name:    kde-workspace
Version: 4.11.19
Release: 13%{?dist}
License: GPLv2
URL:     https://projects.kde.org/projects/kde/kde-workspace
Source0: http://download.kde.org/stable/applications/src/14.12.1/kde-workspace-%{version}.tar.xz

# create missing manpage
Source1: ksysguarddrc.5

# modified version of startkde.cmake, the template for startkde
# not shipped as a patch because we have been burned too often by new upstream
# additions that just break things for us
Source2: startkde.cmake

# hack/workaround to invalidate (delete) plasma pixmap cache on upgrade
Source10: fedora-plasma-cache.sh

# add konsole menuitem
# FIXME?  only show menu when/if konsole is installed? then we can drop the hard-dep
Patch2: kde-workspace-4.9.90-plasma_konsole.patch

# RH/Fedora-specific: VT numbers on fast user switching
# could be handled dynamically eventually
Patch3: kde-workspace-4.10.4-new-session-vt-numbers.patch

# RH/Fedora-specific: Force kdm and kdm_greet to be hardened
Patch4: kde-workspace-4.10.4-kdm-harden.patch

# 441062: packagekit tools do not show icons correctly on KDE
Patch7: kdebase-workspace-4.6.80-krdb.patch

# correct quoting
Patch8: kdebase-workspace-4.2.85-klipper-url.patch

# 434824: KDE4 System Settings - No Method To Enter Administrative Mode
Patch9: kdebase-workspace-4.4.90-rootprivs.patch

# kio_sysinfo based on OpenSUSE's patch
Patch15: kdebase-workspace-4.3.75-kio_sysinfo.patch

# TODO: verify this still works (does not seem to for me) -- rex
Patch16: kde-workspace-4.10.90-battery-plasmoid-showremainingtime.patch

# allow adding a "Leave..." button which brings up the complete shutdown dialog
# to the classic menu (as in KDE <= 4.2.x); the default is still the upstream
# default Leave submenu
Patch17: kde-workspace-4.7.80-classicmenu-logout.patch

# SUSE kudos! plymouth fixed by Laercio de Sousa and Stefan Brüns
Patch19: kde-workspace-4.11.1-kdm_plymouth081.patch
Patch20: kdebase-workspace-4.4.92-xsession_errors_O_APPEND.patch

# support the widgetStyle4 hack in the Qt KDE platform plugin
Patch21: kdebase-workspace-4.3.98-platformplugin-widgetstyle4.patch

# revert patch adding broken browser launcher
# https://projects.kde.org/projects/kde/kde-workspace/repository/revisions/2bbbbdd8fe5a38ae27bab44c9515b2ba78f75277
# https://bugzilla.redhat.com/show_bug.cgi?id=747982
# https://bugs.kde.org/show_bug.cgi?id=284628
Patch25: kde-workspace-4.10.3-bz#747982-launchers.patch

# add org.kde.ktp-presence applet to default systray
Patch26: kde-workspace-4.10.2-systray_org.kde.ktp-presence.patch

# add support for automatic multi-seat provided by systemd using existing reserve seats in KDM
# needs having ServerCmd=/usr/lib/systemd/systemd-multi-seat-x set in /etc/kde/kdm/kdmrc
Patch27: kde-workspace-4.11.1-kdm-logind-multiseat.patch

# drop supplemental groups, if we don't call setgroups or initgroups then the
# ksysguardd, kdm_greet process will inherit a random set of supplemental groups from parent process
Patch28: kde-workspace-4.10.5-ksysguardd-setgroups.patch
Patch29: kde-workspace-4.10.5-initgroups.patch

# hide generalWidget, jovie is disable
Patch30: kde-workspace-4.10.5-bz#1060058.patch

# apps fail in KDE with unknown color name BACKGROUND
Patch31: kde-workspace-4.10.5-bz#1043686-cpp.patch

# avoid conflict between kcm_colors 4 and plasma-desktop 5
Patch32: kde-workspace-4.11.16-colorschemes-kde4.patch

## upstreamable patches:
# "keyboard stops working", https://bugs.kde.org/show_bug.cgi?id=171685#c135
Patch50: kde-workspace-4.10.90-kde#171685.patch

# add apper to kickoff favorites
# Apper is hard to find, http://bugzilla.redhat.com/850445
Patch51: kde-workspace-4.9.0-add_apper_to_kickoff_favorites.patch

# use /etc/login.defs to define a 'system' account instead of hard-coding 500
Patch52: kde-workspace-4.8.2-bz#732830-login.patch

# kdm overwrites ~/.Xauthority with wrong SELinux context on logout
# http://bugzilla.redhat.com/567914
# http://bugs.kde.org/242065
Patch53: kde-workspace-4.7.95-kdm_xauth.patch

# don't modify font settings on load (without explicit save)
# http://bugs.kde.org/105797
Patch54: kde-workspace-kcm_fonts_dont_change_on_load.patch

# support BUILD_KCM_RANDR (default ON) option
Patch55: kde-workspace-4.10.2-BUILD_KCM_RANDR.patch

# kdm (local) ipv6
# https://bugzilla.redhat.com/show_bug.cgi?id=1187957
Patch56: kde-workspace-kdm_local_ipv6.patch

# pam/systemd bogosity: kdm restart/shutdown does not work
# http://bugzilla.redhat.com/796969
Patch57: kde-workspace-4.8.0-bug796969.patch

# use backlight actual_brightness interface
Patch58: kde-workspace-4.11.0-backlight_actual_brightness.patch

# https://bugs.kde.org/show_bug.cgi?id=330773#c5
# bbcukmet: update to BBC's new json-based search and modified xml
Patch59: kde-workspace-4.11.7-weather-fix-bbcukmet.patch

# https://bugs.kde.org/show_bug.cgi?id=330773#c6
# bbcukmet: handle cases where min. or max. temperatures are not reported
Patch60: kde-workspace-4.11.7-weather-fix-bbcukmet-temp.patch

# fix some warnings from coverity scan
Patch64: kde-workspace-4.10.5-coverity-scan.patch

# https://bugs.kde.org/show_bug.cgi?id=330773#c16
# bbcukmet: fix typo in the condition->icon matching ("clar sky" -> "clear sky")
Patch65: kde-workspace-4.11.7-weather-fix-bbcukmet-clear-sky.patch

# https://bugs.kde.org/show_bug.cgi?id=332392
# bbcukmet: fix a crash (#1079296/kde#332392) and improve error handling
Patch66: kde-workspace-4.11.7-weather-fix-bbcukmet-crash-kde#332392.patch

# Get rid of dependency on kdepimlibs 4.11
Patch67: kde-workspace-4.11-remove-dependency-on-kdepimlibs-4.11.patch

# Fix coverity scan issues
Patch68: kde-workspace-4.11.19-coverity-scan-fixes.patch

# Fix grouping of tasks in taskmanager applet
# Bug 1348917 - Display problem with applications grouped by type (> 20 programs) in KDE4
Patch69: kde-workspace-taskmanager-grouping.patch

# Fix unlocking of screenlocker
# Bug 1333441 - System not unlocking on extended monitors when using screensaver
Patch70: kde-workspace-kscreenlocker-greeter-unlock-just-once.patch

# Bug 1568853 - CVE-2018-6790 kde-workspace: Missing sanitization of notifications allows to leak client IP address via IMG element
Patch71: kde-workspace-sanitise-notification-html.patch

# Bug 1611762 - ksysguardd: "internal buffer too small to read /proc/cpuinfo" when running with many CPUs
Patch72: kde-workspace-ksysguard-increase-cpu-buffer.patch

## upstream patches
Patch101: kde-workspace-4.10-bz#921742.patch
Patch104: kde-workspace-4.10.x-bz#1001708.patch
Patch105: kde-workspace-4.10.x-bz#1001727.patch
Patch106: kde-workspace-4.10.5-rhbz990146.patch
Patch109: kde-workspace-4.11-bz#1090492.patch

## plasma active patches

## Fedora specific patches
## HAL-ectomy
Patch200: kde-workspace-4.7.80-no_HAL.patch
Patch210: kdebase-workspace-4.5.90-no_HAL2.patch

# rhel patches
Patch300: kde-workspace-4.8.3-webkit.patch
Patch301: kde-workspace-4.10.5-bz#1063302-branding.patch
Patch302: kde-workspace-exclude_kdm.patch
Patch303: powerdevil-upower-0.99.patch
Patch304: kde-workspace-revert-improve-systemtray-on-hdpi-displays.patch
Patch305: kde-workspace-close-menu-on-closed-task.patch
Patch306: kde-workspace-4.11-fix-loading-get-hot-new-stuff.patch
Patch307: kde-workspace-disable-plasma-screensaver.patch

## trunk (Plasma 5) patches

# pkg rename
Obsoletes: kdebase-workspace < 4.7.97-10
Provides:  kdebase-workspace = %{version}-%{release}

Requires: polkit-kde
%if 0%{?systemd_login1}
Requires: systemd
%endif

%if ! 0%{?akonadi_subpkg}
Obsoletes: %{name}-akonadi < %{version}-%{release}
Provides:  %{name}-akonadi = %{version}-%{release}
Provides: plasma-dataengine-akonadi = %{version}-%{release}
Provides: plasma-dataengine-calendar = %{version}-%{release}
%endif

# kwin apparently provides this internally, kwin/scripting/scripting.cpp
# our scripts can't grok it automatically
Provides: plasma4(scriptengine-declarativescript)
Provides: plasma-scriptengine-declarativescript = %{version}-%{release}

# http://bugzilla.redhat.com/605675
Provides: firstboot(windowmanager) = kwin

# kdmtheme's functionality is provided here
Obsoletes: kdmtheme < 1.3

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= 4.14.4
%if 0%{?webkit}
BuildRequires: kdelibs4-webkit-devel
%endif
BuildRequires: kdepimlibs-devel >= 4.10.5
BuildRequires: kactivities-devel
%if 0%{?nepomuk}
BuildRequires: nepomuk-core-devel >= 4.10.5
BuildRequires: pkgconfig(soprano)
%else
BuildConflicts: nepomuk-core-devel
%endif
BuildRequires: libjpeg-devel
BuildRequires: libutempter-devel
%ifnarch s390 s390x
BuildRequires: lm_sensors-devel
BuildRequires: pkgconfig(libraw1394)
%endif
BuildRequires: pam-devel
%if 0%{?fedora}
BuildRequires: prison-devel
BuildRequires: pkgconfig(libdmtx)
%endif
BuildRequires: pkgconfig(akonadi)
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(dbusmenu-qt)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
%if 0%{?gpsd}
BuildRequires: pkgconfig(libgps)
%endif
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(libpng)
%if 0%{?libqalculate}
BuildRequires: pkgconfig(libqalculate)
%endif
BuildRequires: pkgconfig(libstreamanalyzer)
# used for the Logitech mouse KCM, disabled until #399931 is fixed
# BuildRequires: pkgconfig(libusb)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libxklavier)
# added libnm-glib to workaround https://bugzilla.redhat.com/show_bug.cgi?id=685442
BuildRequires: pkgconfig(NetworkManager) pkgconfig(libnm-glib)
BuildRequires: pkgconfig(polkit-qt-1)
BuildRequires: pkgconfig(qimageblitz)
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(xau)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xres)
# kwin
BuildRequires: pkgconfig(xcomposite) pkgconfig(xdamage) pkgconfig(xrender)
BuildRequires: pkgconfig(gl) pkgconfig(glu)
# kwin-gles
%if 0%{?fedora} || 0%{?rhel} > 6
%define gles 1
BuildRequires: pkgconfig(glesv2) pkgconfig(egl)
%if 0%{?fedora}
BuildRequires: pkgconfig(wayland-client) pkgconfig(wayland-egl) pkgconfig(wayland-server)
%endif
%endif
BuildRequires: python2-devel

Obsoletes: kdebase-workspace-googlegadgets < 4.5.80-7
Obsoletes: plasma-scriptengine-googlegadgets < %{version}-%{release}

Requires: konsole
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kcm_colors = %{version}-%{release}
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
Requires: kde-runtime >= 4.10.5

Obsoletes: kded_randrmonitor < 4.9.98-5
%if 0%{?kscreen}
Requires: kscreen
%endif

Requires: cpp
# for kcm_keyboard
Requires: iso-codes
# activity manager
Requires: kactivities
# for kscreenlocker
Requires: kgreeter-plugins = %{version}-%{release}
# startkde references: dbus-launch df mkdir test xmessage xprop xrandr xrdb xset xsetroot
Requires: coreutils
Requires: dbus-x11
# See http://bugzilla.redhat.com/537609
#Requires: xorg-x11-apps
Requires: xorg-x11-utils
Requires: xorg-x11-server-utils

# Make sure we have kwin, but don't care whether it's our kwin, or kwin5
Requires: kwin

Requires: khotkeys
Requires: kmenuedit
Requires: kinfocenter

%define default_face_icon default1.png
%if 0%{?fedora} || 0%{?rhel} > 6
Requires: kde-settings-ksplash
Requires: kde-settings-plasma
%endif

%description
The KDE Workspace consists of what is the desktop of the
KDE Desktop Environment.

This package contains:
* khotkeys (a hotkey daemon)
* klipper (a cut & paste history utility)
* kmenuedit (the menu editor)
* krunner (a command run interface)
* kwin (the window manager of KDE)
* plasma (the KDE desktop, panels and widgets workspace application)
* systemsettings (the configuration editor)
%{!?kscreen:* krandrtray (resize and rotate X screens)}

%package devel
Summary:  Development files for %{name}
Obsoletes: kdebase-workspace-devel < 4.7.97-10
Provides:  kdebase-workspace-devel = %{version}-%{release}
Provides: solid-bluetooth-devel = %{version}-%{release}
Requires: ksysguard-libs%{?_isa} = %{version}-%{release}
Requires: kwin-libs%{?_isa} = %{version}-%{release}
%if 0%{?gles}
Requires: kwin-gles-libs%{?_isa} = %{version}-%{release}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if 0%{?akonadi_subpkg}
Requires: %{name}-akonadi%{?_isa} = %{version}-%{release}
%endif
Requires: kdelibs4-devel
%description devel
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Obsoletes: kdebase-workspace-libs < 4.7.97-10
Provides:  kdebase-workspace-libs = %{version}-%{release}
Provides:  kdebase-workspace-libs%{?_isa} = %{version}-%{release}
Provides: solid-bluetooth = %{version}-%{release}
Requires: libkworkspace%{?_isa} = %{version}-%{release}
%{?kdelibs4_requires}
# at least while oyxgen style is default
# make dep unversioned to allow plasma5's oxygen to replace it
Requires: kde-style-oxygen%{?_isa}
%description libs
%{summary}.

%package ksplash-themes
Summary: KDE ksplash themes
Obsoletes: kdebase-workspace-ksplash-themes < 4.7.97-10
Provides:  kdebase-workspace-ksplash-themes = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description ksplash-themes
%{summary}, including Horos and Minimalistic.

%package -n kcm_colors
Summary: Colors KDE Control Module
Conflicts: kde-workspace < 4.8.0-2
Requires:  kde-runtime >= 4.10.5
%description -n kcm_colors
The Color Selection module is comprised of several sections:
* The Scheme tab, used to manage schemes
* The Options tab, used to change the options of the current scheme
* The Colors tab, used to change the colors of the current scheme
* The state effects tabs (Inactive, Disabled)

%package -n kdm
Summary: The KDE login manager
Provides: kdebase-kdm = %{version}-%{release}
Provides: service(graphical-login) = kdm
Requires: kgreeter-plugins = %{version}-%{release}
Requires: libkworkspace%{?_isa} =  %{version}-%{release}
Requires: kde-settings-kdm
%description -n kdm
KDM provides the graphical login screen, shown shortly after boot up,
log out, and when user switching.

%package -n kdm-themes
Summary: KDM Themes
group: User Interface/X
Obsoletes: kdm < 4.7.3-9
Requires: kdm = %{version}-%{release}
# http://bugzilla.redhat.com/753409
# http://bugzilla.redhat.com/784389
Requires: kde-wallpapers
BuildArch: noarch
%description -n kdm-themes
A collection of kdm themes, including: circles, horos, oxygen, oxygen-air,
as well as stripes wallpaper.

%package -n kgreeter-plugins
Summary: KDE Greeter Plugin Components
# kgreet_* plugins moved
Conflicts: kdm < 4.6.90-4
Conflicts: kde-workspace < 4.7.80-3
%description -n kgreeter-plugins
%{summary} that are needed by KDM and Screensaver unlocking.

%package -n ksysguard
Summary: KDE System Monitor
Requires: ksysguardd = %{version}-%{release}
Requires: ksysguard-libs%{?_isa} = %{version}-%{release}
%description -n ksysguard
%{summary}.

%package -n ksysguard-libs
Summary: Runtime libraries for ksysguard
# when spilt occurred
Conflicts: kdebase-workspace-libs < 4.7.2-2
%{?kdelibs4_requires}
%description -n ksysguard-libs
%{summary}.

%package -n ksysguardd
Summary: Performance monitor daemon
%description -n ksysguardd
%{summary}.

%package -n kwin
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# When the kwin subpackage was split
Conflicts: kde-workspace <= 4.11.14-1
Summary: KDE Window Manager

%description -n kwin
%{summary}.

%package -n kwin-libs
Summary: Runtime kwin libraries
# When kwin-libs subpackage was split
Conflicts: %{name}-libs%{?_isa} <= 4.11.14-1
%description -n kwin-libs
%{summary}.

%package -n kwin-gles
Summary: KWin built to support GLES
# for libkwin* and friends
Requires: kwin-libs%{?_isa} = %{version}-%{release}
Requires: kwin = %{version}-%{release}
%description -n kwin-gles
%{summary}.

%package -n kwin-gles-libs
Summary: Runtime libraries for kwin-gles
%description -n kwin-gles-libs
%{summary}.

%package -n libkworkspace
Summary: Runtime libkworkspace library
# when spilt occurred
Conflicts: kdebase-workspace-libs < 4.7.2-2
Obsoletes: kdebase-workspace-libs-kworkspace < 4.7.2-3
%{?kdelibs4_requires}
%description -n libkworkspace
%{summary}.

%package -n kde-style-oxygen
Summary: Oxygen widget style for KDE
# when split from kde-workspace(-libs)
Conflicts: kde-workspace-libs < 4.11.2-2
%description -n kde-style-oxygen
%{summary}.

%package -n kdeclassic-cursor-theme
Summary: KDE Classic cursor theme
BuildArch: noarch
%description -n kdeclassic-cursor-theme
%{summary}.

%package -n oxygen-cursor-themes
Summary: Oxygen cursor themes
BuildArch: noarch
%description -n oxygen-cursor-themes
%{summary}.

%package -n plasma-scriptengine-python
Summary: Plasma scriptengine for python
Obsoletes: %{name}-python-applet < 4.5.80-7
Provides:  %{name}-python-applet = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: pykde4%{?_isa}
%description -n plasma-scriptengine-python
%{summary}.

%package -n plasma-scriptengine-ruby
Summary: Plasma scriptengine for ruby
Requires: %{name} = %{version}-%{release}
Requires: ruby
%description -n plasma-scriptengine-ruby
%{summary}.

%package akonadi
Summary: Akonadi integration for KDE Workspace
Obsoletes: kdebase-workspace-akonadi < 4.7.97-10
Provides:  kdebase-workspace-akonadi = %{version}-%{release}
Provides: plasma-dataengine-akonadi = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: akonadi
%description akonadi
%{summary}.

%package -n khotkeys
Summary: Application to configure hotkeys in KDE
Conflicts: kde-workspace < 4.11.15-3
Requires: khotkeys-libs%{?_isa} = %{version}-%{release}
%description -n khotkeys
%{summary}.

%package -n khotkeys-libs
Summary: Runtime libraries for %{name}
Conflicts: kde-workspace < 4.11.15-3
%description -n khotkeys-libs
%{summary}.

%package -n kmenuedit
Summary: KDE Menu Editor
Conflicts: kde-workspace < 4.11.15-3
%description -n kmenuedit
%{summary}.

%package -n kinfocenter
Summary: KDE Info Center
Conflicts: kde-workspace < 4.11.15-3
%description -n kinfocenter
%{summary}.

%prep
%setup -q -n kde-workspace-%{version}

# Well, I looked at doing this using the context menu plugin system and it
# looked like a lot more work than this simple patch to me. -- Kevin
# FIXME/REBASE -- rex
%patch2 -p1 -b .plasma-konsole
%patch3 -p1 -b .vtnumbers
%patch4 -p1 -b .harden
%patch7 -p1 -b .krdb
%patch8 -p1 -b .klipper-url
%patch9 -p1 -b .rootprivs
%patch15 -p1 -b .kio_sysinfo
%patch16 -p1 -b .showremainingtime
%patch17 -p1 -b .classicmenu-logout
%patch19 -p1 -b .kdm_plymouth
%patch20 -p1 -b .xsession_errors_O_APPEND
%patch21 -p1 -b .platformplugin-widgetstyle4
%patch25 -p1 -b .bz#747982-launchers
%patch26 -p1 -b .systray_org.kde.ktp-presence
%patch27 -p1 -b .kdm_logind
%patch28 -p1 -b .ksysguardd-setgroups
%patch29 -p1 -b .kdm_greet-initgroups
%patch30 -p1 -b .bz#1060058
%patch31 -p1 -b .bz#1043686
%patch32 -p1 -b .colorschemes-kde4

# upstreamable patches
%patch50 -p1 -b .kde#171685
%patch51 -p1 -b .add_apper_to_kickoff_favorites
%patch52 -p1 -b .bz#732830-login
%patch53 -p1 -b .kdm_xauth
%patch54 -p1 -b .kcm_fonts_dont_change_on_load
%patch55 -p1 -b .BUILD_KCM_RANDR
%patch56 -p0 -b .kdm_local_ipv6
%patch57 -p1 -b .bug796969
%patch58 -p1 -b .backlight_actual_brightness
%patch59 -p1 -b .weather-fix-bbcukmet
%patch60 -p1 -b .weather-fix-bbcukmet-temp
%patch64 -p1 -b .coverity-scan
%patch65 -p1 -b .weather-fix-bbcukmet-clear-sky
%patch66 -p1 -b .weather-fix-bbcukmet-crash
%patch67 -p1 -b .remove-dependency-on-kdepimlibs-4.11
%patch68 -p1 -b .coverity-scan-fixes
%patch69 -p1 -b .taskmanager-grouping
%patch70 -p1 -b .kscreenlocker-greeter-unlock-just-once
%patch71 -p1 -b .sanitise-notification-html
%patch72 -p1 -b .ksysguard-increase-cpu-buffer

# upstream patches
%patch101 -p1 -b .bug921742
%patch104 -p1 -b .bz#1001708
%patch105 -p1 -b .bz#1001727
%patch106 -p1 -b .bz#990146
%patch109 -p1 -b .bz#1090492

# Fedora patches
%if 0%{?fedora} && 0%{?rhel} > 6
%patch200 -p1 -b .no_HAL
%patch210 -p1 -b .no_HAL2
%endif

# rhel patches
%if ! 0%{?webkit}
%patch300 -p1 -b .webkit
%endif
%patch301 -p1 -b .branding
%if ! 0%{?kdm}
%patch302 -p1 -b .bz#1070140
%endif
%patch303 -p1 -b .powerdevil-upower099
%patch304 -p1 -b .improve-systemtray-on-hdpi-displays
%patch305 -p1 -b .close-menu-on-closed-task.patch
%patch306 -p1 -b .fix-loading-get-hot-new-stuff
%patch307 -p1 -b .disable-plasma-screensaver

# trunk patches

%if 0%{?systemd_login1}
# allow/support f18+ patched version of systemd-197 too
sed -i -e 's|198|197|g' powerdevil/daemon/backends/upower/powerdevilupowerbackend.cpp
%endif

# ensure the file we are about to replace exists
[ -f startkde.cmake ]
# replace it with our known good, patched copy
cp -pf %{SOURCE2} startkde.cmake

## some plasma-dataengine-extractor love
if [ -x %{_bindir}/plasma-dataengine-depextractor ] ; then
plasma-dataengine-depextractor plasma/desktop/applets/showActivityManager/package/
plasma-dataengine-depextractor plasma/generic/applets/activitybar/ plasma-applet-activitybar.desktop
plasma-dataengine-depextractor plasma/generic/applets/analog-clock/ plasma-applet-analogclock.desktop
plasma-dataengine-depextractor plasma/generic/applets/batterymonitor/
plasma-dataengine-depextractor plasma/generic/applets/devicenotifier/package/
plasma-dataengine-depextractor plasma/generic/applets/digital-clock/ plasma-applet-digitalclock.desktop
plasma-dataengine-depextractor plasma/generic/applets/lock_logout
plasma-dataengine-depextractor plasma/generic/applets/notifications/
plasma-dataengine-depextractor plasma/generic/applets/system-monitor/ plasma-applet-system-monitor.desktop
plasma-dataengine-depextractor plasma/generic/applets/webbrowser/ plasma-applet-webbrowser.desktop
plasma-dataengine-depextractor plasma/generic/runners/solid/ plasma-runner-solid.desktop
plasma-dataengine-depextractor plasma/netbook/applets/searchbox/ plasma-applet-searchbox.desktop
fi

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} \
  -DKDE4_ENABLE_FPIE:BOOL=ON \
  -DKDE4_KDM_PAM_SERVICE=kdm \
  -DKDE4_KCHECKPASS_PAM_SERVICE=kcheckpass \
  -DKDE4_KSCREENSAVER_PAM_SERVICE=kscreensaver \
  %{?kscreen:-DBUILD_KCM_RANDR:BOOL=OFF} \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# xsession support
mkdir -p %{buildroot}%{_datadir}/xsessions/

%if 0%{?kdm}
mv %{buildroot}%{_kde4_appsdir}/kdm/sessions/kde-plasma.desktop \
   %{buildroot}%{_kde4_appsdir}/kdm/sessions/kde-plasma-safe.desktop \
   %{buildroot}%{_datadir}/xsessions/

# rename kde-plasma-safe.desktop to ensure it's sorted *after* kde-plasma.desktop
# https://bugzilla.redhat.com/show_bug.cgi?id=1164783
mv %{buildroot}%{_datadir}/xsessions/kde-plasma-safe.desktop \
   %{buildroot}%{_datadir}/xsessions/kde-plasma99-safe.desktop

# remove extraneous xsession files
rm -rfv %{buildroot}%{_kde4_appsdir}/kdm/sessions

# nuke, use external kde-settings-kdm
rm -rfv  %{buildroot}%{_kde4_configdir}/kdm

# own %{_kde4_appsdir}/kdm/faces and set default user image
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/faces
pushd %{buildroot}%{_kde4_appsdir}/kdm/faces
ln -sf ../pics/users/%{default_face_icon} .default.face.icon
popd

bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/kdm/index.cache.bz2
sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/kdm/index.cache
sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/kdm/index.cache
bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/kdm/index.cache
%else
install -p -m644 kdm/kfrontend/sessions/kde-plasma.desktop.cmake %{buildroot}%{_datadir}/xsessions/1-kde-plasma-standard.desktop
install -p -m644 kdm/kfrontend/sessions/kde-plasma-safe.desktop.cmake %{buildroot}%{_datadir}/xsessions/2-kde-plasma-safe.desktop
%endif

# fedora-plasma-cache hack
mkdir -p %{buildroot}%{_sysconfdir}/kde/env/
install -m644 -p %{SOURCE10} %{buildroot}%{_sysconfdir}/kde/env/

# unpackaged files
rm -rfv %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Default/
rm -fv  %{buildroot}%{_kde4_libdir}/liboxygenstyle{,config}.so

# fix documentation multilib conflict in index.cache
for f in kcontrol/colors kmenuedit kcontrol/windowbehaviour kcontrol/kwindecoration \
   kcontrol/khotkeys ksysguard plasma-desktop ; do
   bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache.bz2
   sed -i -e 's!name="id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   sed -i -e 's!#id[a-z]*[0-9]*"!!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   sed -i -e 's!a href="#ftn.id[a-z]*[0-9]*"!a href="ftn"!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   sed -i -e 's!id="ftn.id[a-z]*[0-9]*"!id="ftn"!g' %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
   bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/$f/index.cache
done

# fix multilib conflict cause by a different order of dataengines
sed -i 's!\(^X-Plasma-RequiredDataEngines=\).*!\1applicationjobs,notifications,powermanagement!' %{buildroot}%{_kde4_datadir}/kde4/services/plasma-applet-org.kde.notifications.desktop
sed -i 's!\(^X-Plasma-RequiredDataEngines=\).*!\1applicationjobs,notifications,powermanagement!' %{buildroot}%{_kde4_datadir}/kde4/apps/plasma/plasmoids/org.kde.notifications/metadata.desktop
sed -i 's!\(^X-Plasma-RequiredDataEngines=\).*!\1executable,soliddevice,systemmonitor!' %{buildroot}%{_kde4_datadir}/kde4/services/plasma-applet-system-monitor.desktop

# install manpage
mkdir -p %{buildroot}%{_mandir}/man5
install -m 644 -p %{SOURCE1} %{buildroot}%{_mandir}/man5/

%check
for f in %{buildroot}%{_kde4_datadir}/applications/kde4/*.desktop ; do
  desktop-file-validate $f
done


%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
update-desktop-database -q &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
update-desktop-database -q &> /dev/null || :
fi

%files
%doc COPYING README
%{_sysconfdir}/kde/env/fedora-plasma-cache.sh
%{_kde4_bindir}/kaccess
%{_kde4_bindir}/kapplymousetheme
%{_kde4_bindir}/kblankscrn.kss
%{_kde4_bindir}/kcheckrunning
%{_kde4_bindir}/kcminit
%{_kde4_bindir}/kcminit_startup
%{_kde4_bindir}/kdostartupconfig4
%{_kde4_bindir}/klipper
%{_kde4_bindir}/krandom.kss
%if ! 0%{?kscreen}
%{_kde4_bindir}/krandrstartup
%{_kde4_bindir}/krandrtray
%endif
%{_kde4_bindir}/krdb
%{_kde4_bindir}/krunner
%{_kde4_bindir}/ksmserver
%{_kde4_bindir}/ksplashsimple
%{_kde4_bindir}/ksplashx
%{_kde4_bindir}/ksplashx_scale
%{_kde4_bindir}/ksplashqml
%{_kde4_bindir}/kstartupconfig4
%{_kde4_bindir}/ksystraycmd
%{_kde4_bindir}/oxygen-shadow-demo
%{_kde4_bindir}/plasma-desktop
%{_kde4_bindir}/plasma-netbook
%{_kde4_bindir}/plasma-overlay
%{_kde4_bindir}/plasma-windowed
%{_kde4_bindir}/solid-action-desktop-gen
%{_kde4_bindir}/startkde
%{_kde4_bindir}/systemsettings
%{_kde4_appsdir}/desktoptheme/
%{_kde4_appsdir}/freespacenotifier/
%{_kde4_appsdir}/kaccess/
%{_kde4_appsdir}/katepart/syntax/plasma-desktop-js.xml
%{_kde4_appsdir}/kcminput/
%{_kde4_appsdir}/kcmkeyboard/
%{_kde4_appsdir}/kcmkeys/
%{_kde4_appsdir}/kcmsolidactions/
%{_kde4_appsdir}/kcmstyle/
%{_kde4_appsdir}/kconf_update/
%exclude %{_kde4_appsdir}/kconf_update/kwin_*
%{_kde4_appsdir}/kcontrol/
%{_kde4_appsdir}/kdisplay/
%dir %{_kde4_appsdir}/ksmserver/
%{_kde4_appsdir}/ksmserver/ksmserver.notifyrc
%{_kde4_appsdir}/ksmserver/screenlocker/
%dir %{_kde4_appsdir}/ksmserver/themes/
%{_kde4_appsdir}/ksmserver/themes/contour/
%{_kde4_appsdir}/ksmserver/themes/default/
%dir %{_kde4_appsdir}/ksplash/
%dir %{_kde4_appsdir}/ksplash/Themes/
%{_kde4_appsdir}/ksplash/Themes/None/
%{_kde4_appsdir}/ksplash/Themes/Simple/
%{_kde4_appsdir}/ksplash/Themes/SimpleSmall/
%dir %{_kde4_appsdir}/kstyle
%dir %{_kde4_appsdir}/kstyle/themes/
%{_kde4_appsdir}/kstyle/themes/qt*.themerc
%{_kde4_appsdir}/kthememanager/
%{_kde4_appsdir}/kwrited/
%{_kde4_appsdir}/plasma/
%{_kde4_appsdir}/plasma-desktop/
%{_kde4_appsdir}/plasma-netbook/
%{_kde4_appsdir}/powerdevil/
%{_kde4_appsdir}/solid/
%{_kde4_appsdir}/systemsettings/

%{_kde4_configdir}/activities.knsrc
%{_kde4_configdir}/aurorae.knsrc
%if 0%{?kdm}
%{_kde4_configdir}/background.knsrc
%endif
%{_kde4_configdir}/ksplash.knsrc
%{_kde4_configdir}/plasma-overlayrc
%{_kde4_configdir}/plasma-themes.knsrc
%{_kde4_configdir}/wallpaper.knsrc
%{_kde4_configdir}/xcursor.knsrc

%{_kde4_datadir}/kde4/services/ScreenSavers
%{_kde4_datadir}/kde4/services/ServiceMenus
%{_kde4_datadir}/kde4/services/kded/*.desktop
%exclude %{_kde4_datadir}/kde4/services/kded/khotkeys.desktop
%{_kde4_datadir}/kde4/services/fonts.protocol
%{_kde4_datadir}/kde4/services/*.desktop
%if 0%{?kdm}
%exclude %{_kde4_datadir}/kde4/services/kdm.desktop
%endif
%exclude %{_kde4_datadir}/kde4/services/kwin*.desktop
%exclude %{_kde4_datadir}/kde4/services/khotkeys.desktop
# KInfoCenter
%exclude %{_kde4_datadir}/kde4/services/kcmusb.desktop
%exclude %{_kde4_datadir}/kde4/services/kcm_infosummary.desktop
%exclude %{_kde4_datadir}/kde4/services/kcm_memory.desktop
%exclude %{_kde4_datadir}/kde4/services/devinfo.desktop
%exclude %{_kde4_datadir}/kde4/services/interrupts.desktop
%exclude %{_kde4_datadir}/kde4/services/nic.desktop
%exclude %{_kde4_datadir}/kde4/services/opengl.desktop
%exclude %{_kde4_datadir}/kde4/services/smbstatus.desktop
%exclude %{_kde4_datadir}/kde4/services/kcm_pci.desktop
%ifnarch s390 s390x
%exclude %{_kde4_datadir}/kde4/services/kcmview1394.desktop
%endif
%{_kde4_datadir}/kde4/servicetypes/*
%exclude %{_kde4_datadir}/kde4/servicetypes/kwin*.desktop
%{_kde4_datadir}/sounds/pop.wav
%{_kde4_datadir}/autostart/klipper.desktop
%{_kde4_datadir}/autostart/krunner.desktop
%{_kde4_datadir}/autostart/plasma.desktop
%{_kde4_datadir}/autostart/plasma-desktop.desktop
%{_kde4_datadir}/applications/kde4/*
%exclude %{_kde4_datadir}/applications/kde4/kmenuedit.desktop
%exclude %{_kde4_datadir}/applications/kde4/kinfocenter.desktop
%{_sysconfdir}/dbus-1/system.d/org.kde.fontinst.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%if 0%{?kdm}
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%endif
%{_sysconfdir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_datadir}/dbus-1/interfaces/com.canonical.AppMenu.Registrar.xml
%{_datadir}/dbus-1/interfaces/org.kde.kded.appmenu.xml
%{_datadir}/dbus-1/interfaces/org.kde.KSMServerInterface.xml
%{_datadir}/dbus-1/interfaces/org.kde.krunner.App.xml
%{_datadir}/dbus-1/services/org.kde.fontinst.service
%{_datadir}/dbus-1/services/org.kde.krunner.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%if 0%{?kdm}
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkdm.service
%endif
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kde4_datadir}/config.kcfg/freespacenotifier.kcfg
%{_kde4_datadir}/config.kcfg/klaunch.kcfg
%{_kde4_datadir}/config.kcfg/plasma-shell-desktop.kcfg
%{_datadir}/xsessions/*.desktop
%{_kde4_docdir}/HTML/en/kfontview/
%{_kde4_docdir}/HTML/en/kcontrol/
%exclude %{_kde4_docdir}/HTML/en/kcontrol/colors/
%{_kde4_docdir}/HTML/en/klipper/
%{_kde4_docdir}/HTML/en/plasma-desktop/
%{_kde4_docdir}/HTML/en/systemsettings/
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_iconsdir}/oxygen/*/*/*
%exclude %{_kde4_iconsdir}/oxygen/*/*/kwin.*
%{_kde4_libdir}/kde4/classic_mode.so
%{_kde4_libdir}/kde4/devinfo.so
%{_kde4_libdir}/kde4/icon_mode.so
%{_kde4_libdir}/kde4/ion_*.so
%{_kde4_libdir}/kde4/kcm_*.so
%exclude %{_kde4_libdir}/kde4/kcm_colors.so
%if 0%{?kdm}
%exclude %{_kde4_libdir}/kde4/kcm_kdm.so
%endif
%exclude %{_kde4_libdir}/kde4/kcm_kwin*
%exclude %{_kde4_libdir}/kde4/kcm_hotkeys.so
# KInfoCenter
%exclude %{_kde4_libdir}/kde4/kcm_usb.so
%exclude %{_kde4_libdir}/kde4/kcm_infosummary.so
%exclude %{_kde4_libdir}/kde4/kcm_memory.so
%exclude %{_kde4_libdir}/kde4/devinfo.so
%exclude %{_kde4_libdir}/kde4/kcm_info.so
%exclude %{_kde4_libdir}/kde4/kcm_samba.so
%exclude %{_kde4_libdir}/kde4/kcm_nic.so
%exclude %{_kde4_libdir}/kde4/kcm_opengl.so
%exclude %{_kde4_libdir}/kde4/kcm_pci.so
%ifnarch s390 s390x
%exclude %{_kde4_libdir}/kde4/kcm_view1394.so
%endif
%{_kde4_libdir}/kde4/kded_*.so
%exclude %{_kde4_libdir}/kde4/kded_khotkeys.so
%{_kde4_libdir}/kde4/keyboard_layout_widget.so
%{_kde4_libdir}/kde4/krunner_*.so
%{_kde4_libdir}/kde4/plasma_animator_default.so
%{_kde4_libdir}/kde4/plasma_applet_*.so
%{_kde4_libdir}/kde4/plasma_containmentactions_*.so
%if 0%{?webkit}
%{_kde4_libdir}/kde4/plasma_appletscriptengine_dashboard.so
%{_kde4_libdir}/kde4/plasma_appletscriptengine_webapplet.so
%endif
%{_kde4_libdir}/kde4/plasma_containment_*.so
%{_kde4_libdir}/kde4/plasma_engine_*.so
%if 0%{?gpsd}
%{_kde4_libdir}/kde4/plasma-geolocation-gps.so
# covered by a glob above, dont list here to avoid "File listed twice" bogosity -- rex
#{_kde4_datadir}/kde4/services/plasma-geolocation-gps.desktop
%endif
%{_kde4_libdir}/kde4/plasma-geolocation-ip.so
%{_kde4_libdir}/kde4/plasma_package*_*.so
%{_kde4_libdir}/kde4/plasma_toolbox_*.so
%{_kde4_libdir}/kde4/plasma_wallpaper_*.so
%{_kde4_libdir}/kde4/powerdevil*.so
%{_kde4_libexecdir}/kcheckpass
%{_kde4_libexecdir}/kcmdatetimehelper
%if 0%{?kdm}
%{_kde4_libexecdir}/kcmkdmhelper
%{_kde4_libexecdir}/krootimage
%endif
%{_kde4_libexecdir}/kscreenlocker_greet
%{_kde4_libdir}/libkdeinit4_kaccess.so
%{_kde4_libdir}/libkdeinit4_kcminit.so
%{_kde4_libdir}/libkdeinit4_kcminit_startup.so
%{_kde4_libdir}/libkdeinit4_klipper.so
%{_kde4_libdir}/libkdeinit4_krunner.so
%{_kde4_libdir}/libkdeinit4_ksmserver.so
%{_kde4_libdir}/libkdeinit4_plasma-desktop.so
%{_kde4_libdir}/libkdeinit4_plasma-netbook.so
%{_kde4_libdir}/libkdeinit4_plasma-windowed.so
%{_kde4_libdir}/libkickoff.so
%{_kde4_libdir}/libpowerdevilcore.so
%{_kde4_libdir}/libpowerdevilconfigcommonprivate.so
%{_kde4_libdir}/libsystemsettingsview.so
%{_kde4_libdir}/kconf_update_bin/*
%exclude %{_kde4_libdir}/kconf_update_bin/kwin_*
# python
%exclude %{_kde4_datadir}/kde4/services/plasma-scriptengine*python.desktop
# ruby
%exclude %{_kde4_datadir}/kde4/services/plasma-scriptengine-*ruby*.desktop
%if 0%{?akonadi_subpkg}
%exclude %{_kde4_libdir}/kde4/plasma_applet_calendar.so
%exclude %{_kde4_libdir}/kde4/plasma_applet_clock.so
%exclude %{_kde4_libdir}/kde4/plasma_applet_dig_clock.so
%exclude %{_kde4_libdir}/kde4/plasma_engine_akonadi.so
%exclude %{_kde4_libdir}/kde4/plasma_engine_calendar.so
%exclude %{_kde4_datadir}/kde4/services/plasma-applet-analogclock.desktop
%exclude %{_kde4_datadir}/kde4/services/plasma-applet-calendar.desktop
%exclude %{_kde4_datadir}/kde4/services/plasma-applet-digitalclock.desktop
%exclude %{_kde4_datadir}/kde4/services/plasma-engine-akonadi.desktop
%exclude %{_kde4_datadir}/kde4/services/plasma-dataengine-calendar.desktop
%endif
%{_kde4_bindir}/kfontinst
%{_kde4_bindir}/kfontview
%{_kde4_libdir}/kde4/fontthumbnail.so
%{_kde4_libdir}/kde4/kfontviewpart.so
%{_kde4_libdir}/kde4/kio_fonts.so
%{_kde4_libdir}/strigi/strigita_font.so
%{_kde4_libexecdir}/backlighthelper
%{_kde4_libexecdir}/fontinst
%{_kde4_libexecdir}/fontinst_helper
%{_kde4_libexecdir}/fontinst_x11
%{_kde4_libexecdir}/kfontprint
%{_kde4_configdir}/kfontinst.knsrc
%{_polkit_qt_policydir}/org.kde.fontinst.policy
%{_polkit_qt_policydir}/org.kde.kcontrol.kcmclock.policy
%if 0%{?kdm}
%{_polkit_qt_policydir}/org.kde.kcontrol.kcmkdm.policy
%endif
%{_polkit_qt_policydir}/org.kde.powerdevil.backlighthelper.policy
%{_kde4_appsdir}/kfontinst/
%{_kde4_appsdir}/kfontview/
%{_kde4_appsdir}/konqsidebartng/virtual_folders/services/fonts.desktop
# exclude ksysguard bits
%exclude /usr/share/applications/kde4/ksysguard.desktop
# exclude ksysguard icons
%exclude %{_kde4_iconsdir}/oxygen/*/apps/computer.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/daemon.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/kdeapp.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/kernel.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/ksysguardd.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/running.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/shell.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/unknownapp.*
%exclude %{_kde4_iconsdir}/oxygen/*/apps/waiting.*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%{_kde4_libdir}/libkephal.so.4*
%{_kde4_libdir}/libkfontinst.so.4*
%{_kde4_libdir}/libkfontinstui.so.4*
%{_kde4_libdir}/libkscreensaver.so.5*
%{_kde4_libdir}/libplasma-geolocation-interface.so.4*
%{_kde4_libdir}/libplasma_applet-system-monitor.so.4*
%if ! 0%{?akonadi_subpkg}
# libplasmaclock has an implicit dependency on plasma-dataengine-calendar
 %{_kde4_libdir}/libplasmaclock.so.4*
%endif
%{_kde4_libdir}/libplasmagenericshell.so.4*
%{_kde4_libdir}/libpowerdevilui.so.4*
%{_kde4_libdir}/libsystemsettingsview.so.2*
%{_kde4_libdir}/libtaskmanager.so.4*
%{_kde4_libdir}/libweather_ion.so.6*
%{_kde4_libdir}/libpowerdevilcore.so.0*
%{_kde4_libdir}/libpowerdevilconfigcommonprivate.so.4*
%{_kde4_libdir}/kde4/plugins/gui_platform/libkde.so

%files devel
%{_kde4_includedir}/*
%{_kde4_appsdir}/cmake/modules/*.cmake
%{_kde4_libdir}/cmake/KDE4Workspace/
%{_kde4_libdir}/libkdecorations.so
%{_kde4_libdir}/libkephal.so
%{_kde4_libdir}/libkfontinst.so
%{_kde4_libdir}/libkfontinstui.so
%{_kde4_libdir}/libkscreensaver.so
%{_kde4_libdir}/libksgrd.so
%{_kde4_libdir}/libksignalplotter.so
%{_kde4_libdir}/libkwineffects.so
%{_kde4_libdir}/libkworkspace.so
%{_kde4_libdir}/liblsofui.so
%{_kde4_libdir}/libplasma-geolocation-interface.so
%{_kde4_libdir}/libplasma_applet-system-monitor.so
%{_kde4_libdir}/libplasmaclock.so
%{_kde4_libdir}/libplasmagenericshell.so
%{_kde4_libdir}/libpowerdevilui.so
%{_kde4_libdir}/libprocesscore.so
%{_kde4_libdir}/libprocessui.so
%{_kde4_libdir}/libtaskmanager.so
%{_kde4_libdir}/libweather_ion.so
%{_kde4_libdir}/libkwinglutils.so
%if 0%{?gles}
%{_kde4_libdir}/libkwinglesutils.so
%endif

%files ksplash-themes
%{_kde4_appsdir}/ksplash/Themes/Minimalistic/

%files -n kcm_colors
%{_kde4_datadir}/kde4/services/colors.desktop
%{_kde4_libdir}/kde4/kcm_colors.so
%{_kde4_configdir}/colorschemes-kde4.knsrc
%{_kde4_docdir}/HTML/en/kcontrol/colors/
%{_kde4_appsdir}/color-schemes/Honeycomb.colors
%{_kde4_appsdir}/color-schemes/Norway.colors
%{_kde4_appsdir}/color-schemes/ObsidianCoast.colors
%{_kde4_appsdir}/color-schemes/Oxygen.colors
%{_kde4_appsdir}/color-schemes/OxygenCold.colors
%{_kde4_appsdir}/color-schemes/Steel.colors
%{_kde4_appsdir}/color-schemes/WontonSoup.colors
%{_kde4_appsdir}/color-schemes/Zion.colors
%{_kde4_appsdir}/color-schemes/ZionReversed.colors

%if 0%{?kdm}
%files -n kdm
%{_kde4_bindir}/genkdmconf
%{_kde4_bindir}/kdm
%{_kde4_bindir}/kdmctl
%{_kde4_libdir}/kde4/kcm_kdm.so
%{_kde4_libexecdir}/kdm_config
%{_kde4_libexecdir}/kdm_greet
%{_kde4_configdir}/kdm.knsrc
%{_kde4_docdir}/HTML/en/kdm/
%dir %{_kde4_appsdir}/doc
%{_kde4_appsdir}/doc/kdm/
%dir %{_kde4_appsdir}/kdm/
%{_kde4_appsdir}/kdm/faces/
%{_kde4_appsdir}/kdm/patterns/
%{_kde4_appsdir}/kdm/pics/
%{_kde4_appsdir}/kdm/programs/
%dir %{_kde4_appsdir}/kdm/themes/
%{_kde4_datadir}/kde4/services/kdm.desktop


%files -n kdm-themes
%{_kde4_appsdir}/kdm/themes/ariya/
%{_kde4_appsdir}/kdm/themes/circles/
%{_kde4_appsdir}/kdm/themes/elarun/
%{_kde4_appsdir}/kdm/themes/horos/
%{_kde4_appsdir}/kdm/themes/oxygen/
%{_kde4_appsdir}/kdm/themes/oxygen-air/
# not sure why this is included in kdm sources... ? -- rex
%{_kde4_datadir}/wallpapers/stripes.png*
%endif

%files -n kgreeter-plugins
%{_kde4_libdir}/kde4/kgreet_classic.so
%{_kde4_libdir}/kde4/kgreet_generic.so
%{_kde4_libdir}/kde4/kgreet_winbind.so

%post -n ksysguard
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans -n ksysguard
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :

%postun -n ksysguard
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
fi

%files -n ksysguard
#doc %{name}-%{version}/ksysguard/README
%{_kde4_bindir}/ksysguard
%{_kde4_libdir}/libkdeinit4_ksysguard.so
%{_kde4_appsdir}/ksysguard/
%{_kde4_configdir}/ksysguard.knsrc
%{_kde4_datadir}/applications/kde4/ksysguard.desktop
%{_kde4_docdir}/HTML/en/ksysguard/
%{_kde4_iconsdir}/oxygen/*/apps/computer.*
%{_kde4_iconsdir}/oxygen/*/apps/daemon.*
%{_kde4_iconsdir}/oxygen/*/apps/kdeapp.*
%{_kde4_iconsdir}/oxygen/*/apps/kernel.*
%{_kde4_iconsdir}/oxygen/*/apps/ksysguardd.*
%{_kde4_iconsdir}/oxygen/*/apps/running.*
%{_kde4_iconsdir}/oxygen/*/apps/shell.*
%{_kde4_iconsdir}/oxygen/*/apps/unknownapp.*
%{_kde4_iconsdir}/oxygen/*/apps/waiting.*
%{_kde4_libexecdir}/ksysguardprocesslist_helper
%{_polkit_qt_policydir}/org.kde.ksysguard.processlisthelper.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service

%post -n ksysguard-libs -p /sbin/ldconfig
%postun -n ksysguard-libs -p /sbin/ldconfig

%files -n ksysguard-libs
%{_kde4_libdir}/kde4/plugins/designer/ksignalplotterwidgets.so
%{_kde4_libdir}/libksignalplotter.so.4*
%{_kde4_libdir}/kde4/plugins/designer/ksysguardwidgets.so
%{_kde4_libdir}/kde4/plugins/designer/ksysguardlsofwidgets.so
%{_kde4_libdir}/libksgrd.so.4*
%{_kde4_libdir}/liblsofui.so.4*
%{_kde4_libdir}/libprocesscore.so.4*
%{_kde4_libdir}/libprocessui.so.4*

%files -n ksysguardd
%config(noreplace) %{_kde4_sysconfdir}/ksysguarddrc
%{_mandir}/man5/*
%{_kde4_bindir}/ksysguardd

%if 0%{?gles}
%files -n kwin-gles
%{_kde4_bindir}/kwin_gles
%{_kde4_libdir}/libkdeinit4_kwin_gles.so
%{_kde4_libdir}/kde4/kwin4_effect_gles_builtins.so

%post -n kwin-gles-libs -p /sbin/ldconfig
%postun -n kwin-gles-libs -p /sbin/ldconfig

%files -n kwin-gles-libs
%{_kde4_libdir}/libkwinglesutils.so.1*
%endif

%post -n libkworkspace -p /sbin/ldconfig
%postun -n libkworkspace -p /sbin/ldconfig

%files -n libkworkspace
%{_kde4_libdir}/libkworkspace.so.4*

%post -n kde-style-oxygen -p /sbin/ldconfig
%postun -n kde-style-oxygen -p /sbin/ldconfig

%files -n kde-style-oxygen
%{_kde4_bindir}/oxygen-demo
%{_kde4_bindir}/oxygen-settings
%{_kde4_appsdir}/kstyle/themes/oxygen.themerc
%{_kde4_libdir}/liboxygenstyle.so.4*
%{_kde4_libdir}/liboxygenstyleconfig.so.4*
%{_kde4_libdir}/kde4/kstyle_oxygen_config.so
%{_kde4_libdir}/kde4/plugins/styles/oxygen.so


%post -n kwin
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans -n kwin
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
update-desktop-database -q &> /dev/null || :

%postun -n kwin
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
update-desktop-database -q &> /dev/null || :
fi

%files -n kwin
%{_kde4_bindir}/kwin
%{_kde4_appsdir}/kwin/
%{_kde4_configdir}/kwineffect.knsrc
%{_kde4_configdir}/kwinscripts.knsrc
%{_kde4_configdir}/kwinswitcher.knsrc
%{_kde4_datadir}/config.kcfg/kwin.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%{_kde4_libdir}/kde4/kwin3_aurorae.so
%{_kde4_libdir}/kde4/kwin3_b2.so
%{_kde4_libdir}/kde4/kwin3_laptop.so
%{_kde4_libdir}/kde4/kwin3_oxygen.so
%{_kde4_libdir}/kde4/kwin4_effect_builtins.so
%{_kde4_libdir}/kde4/kwin_b2_config.so
%{_kde4_libdir}/kde4/kwin_oxygen_config.so
%{_kde4_libdir}/kde4/kcm_kwin*
%{_kde4_libexecdir}/kwin_killer_helper
%{_kde4_libexecdir}/kwin_opengl_test
%{_kde4_libexecdir}/kwin_rules_dialog
%{_kde4_libdir}/libkdeinit4_kwin.so
%{_kde4_libdir}/libkdeinit4_kwin_rules_dialog.so
%{_kde4_libdir}/kconf_update_bin/kwin_*
%{_kde4_libdir}/kde4/imports/org/kde/kwin/
%{_kde4_iconsdir}/oxygen/*/*/kwin.*
%{_kde4_appsdir}/kconf_update/kwin_*
%{_kde4_datadir}/kde4/services/kwin
%{_kde4_datadir}/kde4/services/kwin*.desktop
%{_kde4_datadir}/kde4/servicetypes/kwin*.desktop

%post -n kwin-libs -p /sbin/ldconfig
%postun -n kwin-libs -p /sbin/ldconfig

%files -n kwin-libs
%{_kde4_libdir}/libkdecorations.so.4*
%{_kde4_libdir}/libkwineffects.so.1*
%{_kde4_libdir}/libkwinglutils.so.1*


%post -n kdeclassic-cursor-theme
touch --no-create %{_kde4_iconsdir}/KDE_Classic &> /dev/null || :

%posttrans -n kdeclassic-cursor-theme
gtk-update-icon-cache %{_kde4_iconsdir}/KDE_Classic &> /dev/null || :

%postun -n  kdeclassic-cursor-theme
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/KDE_Classic &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/KDE_Classic &> /dev/null || :
fi

%files -n kdeclassic-cursor-theme
%{_kde4_iconsdir}/KDE_Classic/

%files -n oxygen-cursor-themes
%{_kde4_iconsdir}/Oxygen_Black/
%{_kde4_iconsdir}/Oxygen_Blue/
%{_kde4_iconsdir}/Oxygen_White/
%{_kde4_iconsdir}/Oxygen_Yellow/
%{_kde4_iconsdir}/Oxygen_Zion/

%files -n plasma-scriptengine-python
%{python_sitearch}/PyKDE4/plasmascript.py*
%{_kde4_appsdir}/plasma_scriptengine_python
%{_kde4_datadir}/kde4/services/plasma-scriptengine*python.desktop

%files -n plasma-scriptengine-ruby
%{_kde4_appsdir}/plasma_scriptengine_ruby/
%{_kde4_datadir}/kde4/services/plasma-scriptengine-*ruby*.desktop

%if 0%{?akonadi_subpkg}
%post akonadi -p /sbin/ldconfig
%postun akonadi -p /sbin/ldconfig

%files akonadi
%{_kde4_libdir}/libplasmaclock.so.4*
%{_kde4_libdir}/kde4/plasma_applet_calendar.so
%{_kde4_libdir}/kde4/plasma_applet_clock.so
%{_kde4_libdir}/kde4/plasma_applet_dig_clock.so
%{_kde4_libdir}/kde4/plasma_engine_akonadi.so
%{_kde4_libdir}/kde4/plasma_engine_calendar.so
%{_kde4_datadir}/kde4/services/plasma-applet-analogclock.desktop
%{_kde4_datadir}/kde4/services/plasma-applet-calendar.desktop
%{_kde4_datadir}/kde4/services/plasma-applet-digitalclock.desktop
%{_kde4_datadir}/kde4/services/plasma-engine-akonadi.desktop
%{_kde4_datadir}/kde4/services/plasma-dataengine-calendar.desktop
%endif

%files -n khotkeys
%{_kde4_libdir}/kde4/kded_khotkeys.so
%{_kde4_libdir}/kde4/kcm_hotkeys.so
%{_kde4_appsdir}/khotkeys/
%{_kde4_datadir}/kde4/services/khotkeys.desktop
%{_kde4_datadir}/kde4/services/kded/khotkeys.desktop
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml

%post -n khotkeys-libs -p /sbin/ldconfig
%postun -n khotkeys-libs -p /sbin/ldconfig

%files -n khotkeys-libs
%{_kde4_libdir}/libkhotkeysprivate.so.4*

%files -n kmenuedit
%{_kde4_bindir}/kmenuedit
%{_kde4_libdir}/libkdeinit4_kmenuedit.so
%{_kde4_appsdir}/kmenuedit
%{_kde4_datadir}/applications/kde4/kmenuedit.desktop
%{_kde4_docdir}/HTML/en/kmenuedit/

%files -n kinfocenter
%{_kde4_bindir}/kinfocenter
%{_kde4_libdir}/kde4/kcm_usb.so
%{_kde4_libdir}/kde4/kcm_infosummary.so
%{_kde4_libdir}/kde4/kcm_memory.so
%{_kde4_libdir}/kde4/devinfo.so
%{_kde4_libdir}/kde4/kcm_info.so
%{_kde4_libdir}/kde4/kcm_samba.so
%{_kde4_libdir}/kde4/kcm_nic.so
%{_kde4_libdir}/kde4/kcm_opengl.so
%{_kde4_libdir}/kde4/kcm_pci.so
%{_kde4_datadir}/applications/kde4/kinfocenter.desktop
%{_kde4_datadir}/kde4/services/kcmusb.desktop
%{_kde4_datadir}/kde4/services/kcm_infosummary.desktop
%{_kde4_datadir}/kde4/services/kcm_memory.desktop
%{_kde4_datadir}/kde4/services/devinfo.desktop
%{_kde4_datadir}/kde4/services/interrupts.desktop
%{_kde4_datadir}/kde4/services/nic.desktop
%{_kde4_datadir}/kde4/services/opengl.desktop
%{_kde4_datadir}/kde4/services/smbstatus.desktop
%{_kde4_datadir}/kde4/services/kcm_pci.desktop
%{_kde4_appsdir}/kinfocenter/
%{_kde4_appsdir}/kcmusb/
%{_kde4_docdir}/HTML/en/kinfocenter/
%ifnarch s390 s390x
%{_kde4_libdir}/kde4/kcm_view1394.so
%{_kde4_datadir}/kde4/services/kcmview1394.desktop
%{_kde4_appsdir}/kcmview1394/
%endif

%changelog
* Tue Feb 12 2019 Jan Grulich <jgrulich@redhat.com> - 4.11-19-13
- Sanitise notification HTML
  Resolves: bz#1568853

- Increase cpu buffer size in ksysguard
  Resolves: bz#1611762

* Mon Oct 16 2017 Jan Grulich <jgrulich@redhat.com> - 4.11.19-12
- Make sure that plasma screensaver is not used when previously configured
  Resolves: bz#1342560

* Fri Oct 13 2017 Jan Grulich <jgrulich@redhat.com> - 4.11.19-11
- Disable plasma screensaver for security reasons
  Resolves: bz#1342560

* Tue Sep 26 2017 Jan Grulich <jgrulich@redhat.com> - 4.11.19-10
- Fix grouping of tasks in taskmanager applet
  Resolves: bz#1348917
- Fix unlocking of kscreenlocker, unlock it just once
  Resolves: bz#1333441

* Mon Sep 11 2017 Jan Grulich <jgrulich@redhat.com> - 4.11.19-9
- Fix loading of get hot new stuff for KWin decorations and effects
  Resolves: bz#1422002

* Tue Mar 22 2016 Jan Grulich <jgrulich@redhat.com> - 4.11.19-8
- Powerdevil: do not notify about a non existent action
  Resolves: bz#1289149
- Plasma taskmanager: close context menu when task is closed
  Resolves: bz#1262603

* Mon Sep 07 2015 Jan Grulich <jgrulich@redhat.com> - 4.11-19-7
- Requires: cpp
  Resolves: bz#1260129

* Tue Jul 07 2015 Jan Grulich <jgrulich@redhat.com> - 4.11-19-6
- Revert "Improve systemtray on HiDPI displays"
  Resolves: #1238300

* Fri Jun 12 2015 Jan Grulich <jgrulich@redhat.com> - 4.11.19-5
- Fix accidentally removed KDE session

* Mon Jun 08 2015 Jan Grulich <jgrulich@redhat.com> - 4.11-19-4
- Fix multilib issues++

* Mon Jun 08 2015 Jan Grulich <jgrulich@redhat.com> - 4.11-19-3
- Fix multilib issues

* Fri Jun 05 2015 Jan Grulich <jgrulich@redhat.com> - 4.11.19-2
- Fix coverity scan issues
- Re-add kwin-gles subpackages

* Tue Jun 02 2015 Jan Grulich <jgrulich@redhat.com> - 4.11.19-1
- Re-base to 4.11.19 (sync with F21)

* Mon Apr 13 2015 Lukáš Tinkl <ltinkl@redhat.com> - 4.10.5-22
- Resolves: #1202801 - Backport patch to with upower 1.0 API

* Tue Sep 02 2014 Daniel Vrátil <dvratil@redhat.com> - 4.10.5-21
- Resolves: bz#1090492 - changing calendar settings does not appear in plasmoid until month changed (fixed patch)
- Resolves: bz#1109936 - incorrect dispaly corner detection with multiple displays (fixed patch)

* Wed Aug 20 2014 Than Ngo <than@redhat.com> - 4.10.5-20
- Resolves: bz#1040678 - cannot assign custom keyboard shortcut for Show Desktop Grid
- Resolves: bz#1090492 - changing calendar settings does not appear in plasmoid until month changed
- Resolves: bz#1109936 - incorrect dispaly corner detection with multiple displays

* Mon Aug 18 2014 Than Ngo <than@redhat.com> - 4.10.5-19
- Resolves: bz#1109987
- Resolves: bz#1060058
- Resolves: bz#1043686

* Mon Apr 28 2014 Than Ngo <than@redhat.com> - 4.10.5-18
- Resolves: bz#1091087

* Thu Mar 06 2014 Jan Grulich <jgrulich@redhat.com> - 4.10.5-17
- Fix some warnings from coverity scan

* Tue Mar 04 2014 Jan Grulich <jgrulich@redhat.com> - 4.10.5-16
- Last try to fix rhbz#1067111

* Sat Mar 01 2014 Jan Grulich <jgrulich@redhat.com> - 4.10.5-15
- Really resolves: rhbz#1067111

* Fri Feb 28 2014 Than Ngo <than@redhat.com> - 4.10.5-14
- add missing xsessions

* Thu Feb 27 2014 Than Ngo <than@redhat.com> - 4.10.5-13
- Exclude kdm

* Mon Feb 24 2014 Jan Grulich <jgrulich@redhat.com> - 4.10.5-12
- Resolves: rhbz#1067111 - adding second panel on second monitor places panel on top

* Wed Feb 19 2014 Than Ngo <than@redhat.com> - 4.10.5-11
- fix branding issue

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.10.5-10
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.10.5-9
- Mass rebuild 2013-12-27

* Fri Dec 06 2013 Lukáš Tinkl <ltinkl@redhat.com> - 4.10.5-8
- Resolves: rhbz#990146 - Timezone changed to Bratislava instead of Prague

* Wed Oct 30 2013 Than Ngo <than@redhat.com> - 4.10.5-7
- bz#1001708, Out of range date
- bz#1001727, "RTC time" is not changed when using time server

* Wed Aug 07 2013 Than Ngo <than@redhat.com> - 4.10.5-6
- rebuilt

* Tue Aug 06 2013 Than Ngo <than@redhat.com> - 4.10.5-5
- enable libkscreen

* Wed Jul 24 2013 Than Ngo <than@redhat.com> - 4.10.5-4
- cleanup

* Wed Jul 17 2013 Than Ngo <than@redhat.com> - 4.10.5-3
- CVE-2013-4132, backport systray icons memleak fix
- CVE-2013-4133, backport potential kcheckpass security issue

* Tue Jul 02 2013 Than Ngo <than@redhat.com> - 4.10.5-2
- drop the rejected KMix memory leak workaround

* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Wed Jun 26 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.4-6
- kmix: media track change memory leaks with pulseaudio+oxygen widget style (kde#309464, #912457)

* Fri Jun 14 2013 Lukáš Tinkl <ltinkl@redhat.com> - 4.10.4-5
- fix kickoff menu kbd navigation (kdebz#310166)

* Fri Jun 14 2013 Daniel Vrátil <dvratil@redhat.com> - 4.10.4-4
- add upstream patch for #921742

* Thu Jun 13 2013 Martin Briza <mbriza@redhat.com> - 4.10.4-3
- Fix VT numbers on starting a new session (#857366)

* Tue Jun 11 2013 Daniel Vrátil <dvratil@redhat.com> - 4.10.4-2
- backport upstream patch for #921781

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3
- restore patch omitting broken launchers

* Fri May 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-12
- -DKDE4_ENABLE_FPIE:BOOL=ON
- don't write fonts.conf on load (kde#105797)

* Mon Apr 29 2013 Than Ngo <than@redhat.com> - 4.10.2-11
- drop old patch for aurora
- fix multilib issue

* Mon Apr 29 2013 Martin Briza <mbriza@redhat.com> 4.10.2-10
- changed the systemd-displaymanager patch to switch the sessions using systemd-logind, too

* Thu Apr 25 2013 Martin Briza <mbriza@redhat.com> 4.10.2-9
- regenerated the systemd-displaymanager patch against latest upstream master
- worked around #955374 before I fix it clean upstream

* Wed Apr 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-8
- avoid/revert commit to avoid plasma crash on wallpaper change (kde#318806)

* Mon Apr 22 2013 Than Ngo <than@redhat.com> - 4.10.2-7
- fedora/rhel condition

* Sun Apr 21 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-6
- sync to latest 4.10 branch commits

* Thu Apr 18 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-5
- drop LD_BIND_NOW from startkde (#908380)
- fold all startkde-related patches into redhat_startkde.patch

* Thu Apr 11 2013 Daniel Vrátil <dvratil@redhat.com> 4.10.2-4
- clear screenlocker password on ESC (#949452)

* Thu Apr 11 2013 Martin Briza <mbriza@redhat.com> 4.10.2-3
- added basic support for automatic multi-seat in KDM (#884271)

* Tue Apr 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-2
- rebase systray_ktp-presence patch for applet rename

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.2-1
- 4.10.2

* Sun Mar 24 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-3
- don't apply no_HAL on el6

* Wed Mar 13 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-2
- PowerDevil should use upower to suspend on F17 (#920874)
- other small upstream fixes (xrandrbrightness, login1 leak, stop screensaver)

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Wed Feb 20 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-11
- python-scriptengine-python: s/Requires: PyKDE4/Requires: pykde4/

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-10
- respin BUILD_KCM_RANDR.patch, avoid failure in startkde when krandrstartup doesn't exist

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-9
- drop solid_krunner_disable patch (seems better now)

* Thu Feb 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-8
- kscreen support => disable all of kcontrol/randr (f19+ currently)

* Sat Feb 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-7
- fedora-plasma-cache.sh: don't delete Trolltech.conf

* Sat Feb 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-6
- tweak fedora-plasma-cache.sh for plasma-svgelements*, Trolltech.conf too
- enable powerdevil-login1 support on f18

* Fri Feb 08 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-5
- fix fedora-plasma-cache.sh (to not exit)

* Thu Feb 07 2013 Lukáš Tinkl <ltinkl@redhat.com> 4.10.0-4
- fix wrong description and size for 2-stage USB storage devices

* Mon Feb 04 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-3
- refresh Powerdevil login1 patch

* Sat Feb 02 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.10.0-2
- fix kcmdatetimehelper search path so hwclock and zic are found (#906854)

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Wed Jan 30 2013 Lukáš Tinkl <ltinkl@redhat.com> 4.9.98-7
- update Powerdevil login1 patch

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-6
- unconditionally Obsoletes: kded_randrmonitor

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-5
- Requires: kscreen, Obsoletes: kded_randrmonitor (f19+)

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-4
- drop Requires: kde-display-management (for now)
- switch fedora-plasma-cache hack to env script

* Fri Jan 25 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-3
- add fedora-plasma-cache kconf_update script

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.98-2
- respin systemd_login1 patch

* Sun Jan 20 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 4.9.97-6
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-5
- refresh powerdevil_systemd_login1 patch (kde review#108407)

* Mon Jan 14 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-4
- proper powerdevil systemd-login1 support (kde review#108407)

* Thu Jan 10 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-3
- hack to use org.freedesktop.login1 to handle suspend (instead of upower),
  seems to help avoid double-sleep (#859227)

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-2
- kded_xrandrmonitor subpkg, to allow use of it or kscreen

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Thu Dec 06 2012 Martin Briza <mbriza@redhat.com> 4.9.90-2
- Merged and cleaned the systemd shutdown and logout patches.
- It is possible to use systemd and/or CK without defining it at compile time

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Fri Nov 16 2012 Martin Briza <mbriza@redhat.com> - 4.9.3-3
- user switching dialog now doesn't list inactive (closing) sessions and more information is retrieved from logind

* Thu Nov 15 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-2
- pull upstream fix for some regressions (krunner, analog clock)
- drop unused llvm_whitelist patch

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Fri Nov 02 2012 Than Ngo <than@redhat.com> - 4.9.2-10
- rhel/fedora condition

* Thu Nov 1 2012 Lukáš Tinkl<ltinkl@redhat.com> 4.9.2-9
- build against prison only under Fedora

* Tue Oct 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-8
- more systemd_inhibit love (#859227, kde#307412)

* Fri Oct 26 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-7
- rework fontconfig patch to ensure $XDG_CONFIG_HOME/fontconfig exists

* Thu Oct 18 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-6
- monitor sleep settings reset, resulting in monitor turning off (kde#295164)

* Mon Oct 08 2012 Martin Briza <mbriza@redhat.com> 4.9.2-5
- Fixing user switching with SystemD (#859347), for LightDM

* Thu Oct 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-4
- ongoing systemd_inhibit work (#859227)

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.2-3
- tarball respin (includes plasma/python2 patch)

* Mon Oct 01 2012 Lukáš Tinkl <ltinkl@redhat.com> - 4.9.2-2
- fix loading of Python2 plasmoids

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Thu Sep 27 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-7
- disable plasma-runner-solid by default (kde#307445)

* Fri Sep 21 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-6
- update the systemd PowerDevil Policy Agent patch to match the upstream
  version (part of KDE 4.9.2)
- update clock applets on system date/time changes

* Tue Sep 18 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-5
- fix device notifier Free Space meter

* Thu Sep 13 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-4
- hopefully also solve the screen dimming issue when inactive session goes idle

* Thu Sep 13 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.1-3
- Resolves #849334 - screen lock failure (laptop lid)

* Wed Sep 05 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-2
- upstream patch for kwin regression (kde#306260, kde#306275)

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Mon Aug 27 2012 Lukáš Tinkl <ltinkl@redhat.com> 4.9.0-6
- Resolves #851887 - KDE Logout does not Suspend to RAM/Disk

* Tue Aug 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-5
- Add apper to default kickoff favorites (#850445)

* Thu Aug 09 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-4
- upstream patch for aurora/qml-based kwin decorations

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-3
- window keeps status 'asking for attention' after gaining focus (kde#303208)

* Fri Aug 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-2
- kcm_fonts should use $XDG_CONFIG_HOME/fontconfig/fonts.conf for storage settings for fontconfig > 2.10.0 (kde#304317)

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Than Ngo <than@redhat.com> - 4.8.97-2
- remove obsolete stuffs in startkde, kde-4.6.x already uses QLocale
  to try obtain a default country.

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Tue Jul 10 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-4
- fix tooltip for OpticalDisc

* Mon Jul 09 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-3
- Battery Monitor widget stops tracking charging state changes after suspend/resume cycle (#837345, kde#287952)

* Tue Jul 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.95-2
- restore stable kdecoration API to 4.8 (#831958, kde#301728)

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95
- remove battery size patch

* Mon Jun 25 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-3
- Requires: konsole

* Tue Jun 19 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-2
- battery plasmoid icon does not scale below a certain size (kde#301877)

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.90-1
- 4.8.90

* Fri Jun 01 2012 Jaroslav Reznik <jreznik@redhat.com> 4.8.80-4
- respin
- remove kwin check opengl patch

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.80-3
- Provides: plasma4(scriptengine-declarativescript)

* Sat May 26 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.8.80-2
- new showremainingtime patch, now just defaults the option to true
  (It doesn't have ugly side effects anymore with the rewritten plasmoid.)

* Sat May 26 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80
- remove remaining time patch, should be enabled in kde-settings

* Tue May 08 2012 Than Ngo <than@redhat.com> - 4.8.3-4
- add rhel/fedora conditions

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-3
- more work on plasma clock widget/locale crash (kde#299237)

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.3-2
- plasma clock widget/locale crash (kde#299237)

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3
- kdm grub2 integration upstreamed

* Tue Apr 3 2012 Lukas Tinkl <ltinkl@redhat.com> 4.8.2-3
- respin 4.8.2 tarball

* Sun Apr 01 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.2-2
- Kwin does not repaint window shadow regions after closing window (#808791, kde#297272)

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 19 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.1-7
- rebuild for plasma4.prov fix (no more spaces in Plasma runner auto-Provides)

* Thu Mar 15 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-6
- Requires: kactivities >= %%{version}

* Wed Mar 14 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.1-5
- fix another bug in the systemd shutdown/restart patch (missing parameter)

* Tue Mar 13 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.1-4
- fix bugs in the systemd shutdown/restart patch

* Mon Mar 12 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-3
- Port shutdown/restart code from ConsoleKit to systemd (#788171)

* Thu Mar 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.1-2
- 4.8 branch commit for settings_style support

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.1-1
- 4.8.1
- removed powerdevil verb., eDP and gcc47 patches

* Tue Feb 28 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-12
- kdm restart/shutdown does not work (#796969)

* Wed Feb 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-11
- drop ConsoleKit support f17+

* Wed Feb 22 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-10
- kdm: Requires: ConsoleKit-x11 (#787855)

* Tue Feb 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-9
- add ktp_presence applet to default systray

* Tue Feb 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-8
- omit kwin_llvmpipe_whitelist patch, not ready/testable (#794835)

* Mon Feb 13 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-7
- kwin llvmpipe whitelist (#790142)
- powerdevil verbosity++ (kde#289760)

* Sat Feb 11 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-6
- kdm-grub2 integration (#785849)

* Tue Feb 07 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.8.0-5
- kde-workspace: Requires: ConsoleKit (shutdown/restart, works around #788171)
- kdm: Requires: ConsoleKit (works around #787855, nasty error message on login)

* Thu Feb 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-4
- eDP patch (kde#289760)

* Tue Jan 31 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-3
- kgreeter-plugins subpkg (#785817)

* Tue Jan 24 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.0-2
- kcm_colors subpkg (#761184)
- kdm-themes: Requires: kde-wallpapers unconditionally (#784389)
- s/kdebase-runtime/kde-runtime/

* Fri Jan 20 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-10
- rename kdebase-workspace -> kde-workspace

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Tue Jan 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-3
- kdm overwrites ~/.Xauthority with wrong SELinux context on logout (#567914,kde#242065)
- gcc47 fixes

* Thu Dec 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- startkde: omit MALLOC_CHECK_ debug'ery

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> 4.7.95-1
- 4.7.95
- Add Ariya kdm theme

* Wed Dec 14 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-3
-libs: move libkworkspace (versioned) dep here (from -devel)

* Thu Dec 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-2
- kwin-gles: move kwin4_effect_gles_builtins here

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90
- BR: libjpeg-devel (ksplash)

* Thu Dec 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-6
- get some kwin-gles love

* Tue Nov 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-5
- BR: kactivities-devel

* Thu Nov 24 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-4
- Respin with new upstream tarball
- Drop patch: don't use INSTALL to copy file to current binary dir

* Thu Nov 24 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-3
- Fixed file listed twice
- Remove big cursors from files (they are no longer in upstream tarball)
- Add new files: libkwinglutils.so*, liboxygenstyleconfig.so*
  libpowerdevilconfigcommonprivate.so*, kfontinst.knsrc
- New ksplash theme Minimalistic
- patch: don't use INSTALL to copy file to current binary dir

* Thu Nov 24 2011 Radek Novacek <rnovacek@redhat.com> 4.7.80-2
- Drop "only show in kde" patch (applied upstream)

* Fri Nov 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Thu Nov 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-13
- add plasma-active patches

* Thu Nov 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-12
- Crash in TaskManager::TaskItem::task (kde#272495)
- Crashes When Adding Weather Widgets (Geolocation) (kde#277036)

* Thu Nov 17 2011 Lukas Tinkl <ltinkl@redhat.com> 4.7.3-11
- battery plasmoid fixes (#753429)

* Wed Nov 16 2011 Lukas Tinkl <ltinkl@redhat.com> 4.7.3-10
- fix kwin + twinview

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-9
- kdm-themes subpkg (#753409)

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-8
- rebuild (libpng)

* Mon Nov 07 2011 Than Ngo <than@redhat.com> - 4.7.3-7
- Fix possible uninitialized variable use in ksplashx multi-screen code

* Fri Nov 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-6
- build against libkactivities-6.1

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-5
- drop kde-wallpapers (now packaged separately)

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-4
- tarball respin

* Mon Oct 31 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-3
- kde-wallpapers: Obsoletes: kdebase-workspace-wallpapers < 4.7.2-10

* Mon Oct 31 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-2
- Requires: kde-settings-ksplash kde-settings-plasma (f16+)

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3
- -devel: Provides: kde-workspace-devel
- -libs: Provides: kde-workspace-libs

* Sat Oct 29 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.2-12
- kcm_clock helper: Sync the hwclock after setting the date (#749516)

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-11
- Rebuilt for glibc bug#747377

* Tue Oct 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-10
- BR: libkactivities-devel

* Mon Oct 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-9
- kdebase-workspace-wallpapers -> kde-wallpapers

* Fri Oct 21 2011 Alexey Kurov <nucleo@fedoraproject.org> - 4.7.2-8
- revert patch adding broken launchers (#747982)

* Mon Oct 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-7
- Generate texture coordinates for limited NPOT support (kde#269576)

* Sat Oct 15 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.2-6
- drop displayEvents patch, moved to kde-settings (in kde-settings-4.7-12)

* Thu Oct 13 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-5
- ksysguard: include ksysguard.desktop

* Wed Oct 12 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-4
- plasmaclock displayEvents=false default

* Mon Oct 10 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-3
- ksysguard(-libs) subpkg
- libkworkspace subpkg
- kdm: Requires: libkworkspace

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Tue Sep 20 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-3
- switch to pkgconfig-style deps

* Fri Sep 16 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.1-2
- upstream kwin_performance patch
- Use /etc/login.defs to define a 'system' account instead of hard-coding 500 (#732830)

* Wed Sep 14 2011 Radek Novacek <rnovacek@redhat.com> 4.7.1-1
- Remove upstreamed patch kdebase-workspace-4.7.0-kde#278206.patch

* Tue Sep 06 2011 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Tue Aug 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-9
- disable google-gadget support (f16+)

* Sun Aug 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.0-8
- rebuild again for the fixed RPM dependency generators for Plasma (#732271)

* Sun Aug 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.0-7
- rebuild for the RPM dependency generators for Plasma (GSoC 2011)

* Wed Aug 17 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-6
- upstream kwin malloc patch

* Sat Aug 13 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-5
- upstream kwin software rasterizer patch

* Thu Aug 11 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-4
- modularize googlegadget/gpsd support a bit

* Sat Aug 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.0-3
- drop Requires: nepomukcontroller (included in kde-runtime now)

* Thu Jul 28 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.0-2
- fix GDM getting misdetected as LightDM (kde#278206, patch by Alex Fiestas)

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.0-1
- 4.7.0
- kde4workspace_version is not needed anymore
- Provides: kde-workspace kde-wallpapers (to match new upstream tarballs)

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-4
- rebuild (qt48)

* Mon Jul 18 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-3
- Conflicts: kdm < 4.6.90-4 (when kgreet_* plugins moved)

* Tue Jul 12 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.95-2
- fix redhat_startkde.patch

* Fri Jul 08 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.95-1
- 4.6.95 (rc2)

* Wed Jul 06 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-4
- move kgreet_* plugins to main pkg, needed by kscreenlocker (#711234)

* Tue Jul 05 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-3
- startkde: omit MALLOC_CHECK pieces

* Thu Jun 30 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.90-2
- cleanup/remove some old/deprecated pieces

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Fri May 27 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.80-1
- 4.6.80 (beta1)
- add BR prison-devel

* Thu May 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-9
- drop BR: libcaptury-devel

* Wed May 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-8
- virtual desktop names are lost after log out (kde#272666)

* Sat May 21 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-7
- multilib QT_PLUGIN_PATH (#704840)

* Thu May 19 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.6.3-6
- make nm-09-compat patch F15-only, it won't work on Rawhide anyway

* Sun May 15 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-5
- kde4/plugins/styles/oxygen.so is not multilib (#704840)

* Sun May 08 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.6.3-4
- nm-09-compat: reenable Solid NM backend build with NM 0.9 (disabled in 4.6.3)

* Sat Apr 30 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.3-3
- fix spurious "Networking system disabled" message (#700831)

* Fri Apr 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-2
- use updated plymouth patch trying new method first

* Thu Apr 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-1
- 4.6.3

* Thu Apr 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.2-4
- fix kde#270942 (direct rendering disabled on Intel graphics since mesa 7.10.1)

* Fri Apr 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.2-3
- fix the temperature plasmoids and ksysguard temperature sensors regression

* Thu Apr 07 2011 Lukas Tinkl <ltinkl@redhat.com> - 4.6.2-2
- #694222 - Brightness controls no longer work
- kdebug#257948 - Powerdevil can no longer control brightness
- drop obsolete HAL backlight patch

* Wed Apr 06 2011 Than Ngo <than@redhat.com> - 4.6.2-1
- 4.6.2

* Tue Apr 05 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-7.1
- apply no_HAL patches on f14 too

* Sun Apr 03 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.6.1-7
- Restore lost hunks from redhat_startkde patch, fixes regressions with running
  Qt 3 binaries (Qt 3 Assistant etc.) and with the initial background color
- Fix incorrectly rebased hunk from redhat_startkde patch, fixes regression with
  language setting

* Wed Mar 30 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.1-6
- Autohide panel gets visible and does not hide itself (#690450)

* Thu Mar 24 2011 Dan Williams <dcbw@redhat.com> 4.6.1-5
- Rebuild with NM 0.9 compat patches (F15+)

* Thu Mar 24 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-4
- Notification size increases randomly and cant be restored (#688967)

* Mon Mar 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-3
- solid_nm_emit patch

* Mon Mar 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-2
- use system-kde-theme again (ie, lovelock-kde-theme on f15)
- -Requires: system-backgrounds-kde
- +Requires: system-plasma-desktoptheme
- -ksplash-themes: move Default (Air+Horos) ksplash theme here

* Sat Feb 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Fri Feb 11 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-8
- include Horos wallpaper (upstream default) in main pkg, not -wallpapers

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-6
- drop Requires: system-{backgrounds,ksplash}-kde, use
  generic/upstream theming, for now.

* Thu Feb 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-5
- oxygen theme crasher (#674792, kde#265271)

* Wed Jan 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.0-4
- startkde: drop MALLOC_CHECK bits

* Tue Jan 25 2011 Lukas Tinkl <ltinkl@redhat.com> - 4.6.0-3
- respun tarball, omit (now upstreamed) PowerDevil
  fixes from 4.6.0-2

* Mon Jan 24 2011 Lukas Tinkl <ltinkl@redhat.com> - 4.6.0-2
- handle PowerDevil config migration

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0

* Tue Jan 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-3
- require nepomukcontroller (temporary)

* Fri Jan 14 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-2
- add optional BR libdmtx (data matrix bar-codes support)

* Wed Jan 05 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1
- 4.5.90 (4.6rc1)

* Sat Dec 04 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.5.85-2
- adjust the HALsectomy patches
- remove solid-powermanagement

* Sat Dec 04 2010 Thomas Janssen <thomasj@fedoraproject.org> - 4.5.85-1
- 4.5.85 (4.6beta2)

* Wed Dec 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-7
- -googlegadgets => plasma-scriptengine-googlegaddgets
- -python-applet => plasma-scriptengine-python
- (new) plasma-scriptengine-ruby

* Wed Nov 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-6
- drop old polkit conditionals
- don't include libpowerdevil{core,ui}.so in -devel

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-5
- drop Obsoletes: -python-applet

* Tue Nov 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-4
- respun tarball, includes Python script engine fixes

* Mon Nov 22 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.5.80-3
- disable PowerDevil's HAL backend (aka project HALsectomy)

* Mon Nov 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.80-2
- backport upstream fixes to reenable and fix the Python script engine

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Mon Nov 15 2010 Than Ngo <than@redhat.com> - 4.5.3-3
- apply patch to fix crash on automatic re-login after automatic login

* Sat Nov 06 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.3-2
- drop classicmenu-games patch, upstream fixed the same issue differently and
  now the 2 fixes conflict (classic menu confuses Name and Description)

* Fri Oct 29 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Wed Oct 27 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.5.2-5
- use upstream ck-shutdown patch from 4.6 trunk (instead of my old one),
  supports GDM session switching (#560511, kde#186198)
- drop old F11- version of the ck-shutdown patch, F11 is EOL

* Wed Oct 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-4
- kdebase-workspace depends on xorg-x11-apps (#537609)

* Sat Oct 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-3
- backport kwin ui for unredirecting fullscreen windows

* Fri Oct 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-2
- include better, upstream fix for: krandr: Display Settings are Lost
  on Logout (kdebug183143, rh#607180)

* Fri Oct 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- 4.5.2

* Wed Sep 29 2010 jkeating - 4.5.1-5
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-4
- kdm is not localized when changing lang using system-config-language (#631861)

* Wed Sep 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-3
- Provides: firstboot(windowmanager)  (#605675)

* Sun Aug 29 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-2
- "fonts/package" is an invalid MIME type (#581896)

* Fri Aug 27 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.5.1-1
- 4.5.1

* Thu Aug 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.0-4
- Requires: iso-codes (for kcm_keyboard)

* Fri Aug 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.0-3
- krunner "run command" doesn't keep any history (kde#247566)

* Thu Aug 12 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.5.0-2
- disable malloc checking in startkde for releases

* Tue Aug 03 2010 Than Ngo <than@redhat.com> - 4.5.0-1
- 4.5.0
- kde4workspace_version

* Tue Jul 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1.py27
- rebuild for python27

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.4.92-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-2
- omit non-essential xsession .desktop files, runs afoul of selinux (#588130)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri Jun 25 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.90-2
- port and reapply rootprivs (#434824) patch

* Fri Jun 25 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.90-1
- 4.5 RC1 (4.4.90)

* Wed Jun 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.85-5
- krandr: Display Settings are Lost on Logout (kdebug183143, rh#607180)

* Mon Jun 21 2010 Karsten Hopp <karsten@redhat.com> 4.4.85-4
- don't require raw1394 on s390, s390x

* Sun Jun 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.85-3
- Significant CPU penalty for using Kwin effects (kde#239963)

* Tue Jun 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.85-2
- Adding "Enable networking" button to knetworkmanager (rh#598765, kde#238325)
- drop < f12 conditionals
- pciutils, raw1394 & qualculate BRs
- added kcmkdm helper and policy (from kdelibs)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Fri May 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.80-3
- Conflicts: kdebase < 6:4.4.80

* Tue May 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.80-2
- Blur shadow around widgets does not smoothly fade out (kde#235620)

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- 4.5 Beta 1 (4.4.80)
- kxkb and safestartkde has been removed
- add newly installed files

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.3-2
- rebuild (gpsd,kdelibs)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Tue Apr 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-5
- powerdevil only autosuspends once/twice (kde#221648)
- CVE-2010-0436

* Mon Apr 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-4
- another stab at f13 kdm/plymouth love (#577482)
- powerdevil always suspends twice (kde#221637)

* Wed Apr 07 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.2-3
- rip out bulletproof X changes (cf. kubuntu_33_kdm_bulletproof_x.diff) from
  our copy of kubuntu_34_kdm_plymouth_transition.diff
- drop experimental novt patch, should not be needed with the working Plymouth
  integration and may have side effects (can readd it later if really needed)
- fix icon name in plasma-konsole patch: use XDG icon instead of kappfinder one

* Tue Apr 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.2-2
- try to workaround "X server hogs the CPU (#577482)" by letting X
  choose vt itself
- include (but not yet apply) kubuntu_34_kdm_plymouth_transition.diff

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.2-1
- 4.4.2

* Thu Mar 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.1-2
- fix KSysGuard and KRunner System Activity dialog not refreshing (kde#230187)

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Fri Feb 26 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-8
- fix the Games menu in the classic menu mixing up Name and Description

* Fri Feb 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-7
- version solid-bluetooth(-devel) better

* Fri Feb 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-6
- solid-bluetooth and Requires: bluez ... pulls unwanted baggage (#566306)

* Tue Feb 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-5.1
- Requires: kbluetooth (<f13)

* Sat Feb 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-5
- fix incorrectly rebased classicmenu-logout patch (#564536)

* Thu Feb 11 2010 Than Ngo <than@redhat.com> - 4.4.0-4
- move xsession desktop files to main package
  (cannot start kde from gdm if kdm not installed)
- Desktop locking crashes (kde#217882#16)

* Thu Feb 11 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.0-3
- requires bluez for solid-bluetooth

* Tue Feb 09 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.4.0-2.1
- use old ck-shutdown patch without the CanStop check on F11 (#562851)

* Mon Feb 08 2010 Than Ngo <than@redhat.com> - 4.4.0-2
- apply upstream patch to fix Plasma Memory Leak and High CPU usage

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0

* Tue Feb 02 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.98-3
- support the widgetStyle4 hack in the Qt KDE platform plugin

* Mon Feb 01 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.98-2
- rebase battery-plasmoid-showremainingtime patch and remove references to 4.2

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Sat Jan 30 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.95-2
- ck-shutdown: don't offer shutdown/restart when not allowed by CK (#529644)

* Thu Jan 21 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Thu Jan 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.90-10
- fix polkit-1 conditionals

* Wed Jan 20 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.90-9
- fix infinite recursion in the patch for #556643

* Tue Jan 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-8
- SELinux is preventing /sbin/setfiles "read" access on
  /var/spool/gdm/force-display-on-active-vt (deleted) (#556643)

* Sun Jan 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-7
- rebuild (libxklavier)

* Thu Jan 14 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.3.90-6
- fix KDM's missing header build problem
- polkit-qt BR for polkit-1

* Mon Jan 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-5
- do not link calendar dataengine with Akonadi (kde#215150, rh#552473)
- s/plasma-engine/plasma-dataengine/

* Sat Jan 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-4
- krunner crasher (kde#221871)

* Fri Jan 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-3
- rebuild (kdelibs polkit-1 macros)

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-2
- drop -akonadi subpkg

* Wed Jan 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- kde-4.3.90 (4.4rc1)

* Tue Jan 05 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.85-3
- F13+: don't Obsoletes: PolicyKit-kde, let polkit-kde obsolete it
- F13+: explicitly require polkit-kde instead of PolicyKit-authentication-agent

* Sat Jan 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-2
- startkde: disable MALLOC_CHECK_

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- kde-4.3.85 (4.4beta2)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.3.80-5
- Repositioning the KDE Brand (#547361)

* Fri Dec 11 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.80-4
- SELinux is preventing access to a leaked .xsession-errors-:0 file descriptor (#542312)

* Wed Dec 09 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.80-3
- drop polkit-qt* Obsoletes, we have a new polkit-qt now

* Wed Dec 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.80-2
- BR: shared-desktop-ontologies-devel

* Tue Dec 01 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)
- kdm_plymouth patch (#475890)

* Sat Nov 28 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.75-0.4.svn1048496
- backport battery plasmoid from current pre-4.3.80 trunk for showremainingtime
- rebase battery-plasmoid-showremainingtime patch
- rebase brightness-keys patch for the above backport

* Sat Nov 28 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.75-0.3.svn1048496
- rebase plasma-konsole patch

* Wed Nov 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.75-0.2.svn1048496
- Requires: PolicyKit-authentication-agent unconditionally

* Sat Nov 21 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- update to 4.3.75 snapshot

* Wed Nov 18 2009 Lukáš Tinkl <ltinkl@redhat.com> 4.3.3-8
- correctly try to deduce LANG (kubuntu_13_startkde_set_country.diff)

* Fri Nov 13 2009 Rex Dieter <rdieter@fedoraproject.org> 4.3.3-7
- kubuntu_101_brightness_fn_keys_and_osd.diff (#509295)

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-6
- rhel cleanup, fix conditional for RHEL

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-5
- fix logic on Requires: kdm  (ie, make F-12 builds not include it)

* Thu Nov 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-4
- try experimental patch for "keyboard stops working" (kde#171685)

* Wed Nov 11 2009 Than Ngo <than@redhat.com> - 4.3.3-3
- rhel cleanup, drop BR on libcaptury-devel

* Mon Nov 09 2009 Rex Dieter <rdieter@fedoraprojectg.org> - 4.3.3-2
- Obsoletes: polkit-qt-examples (f12+)
- -devel: Obsoletes: polkit-qt-devel (f12+)

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3
- BR: libXau-devel libXdmcp-devel

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.2-2
- drop Requires: oxygen-icon-theme (dep moved to kdebase-runtime)

* Sun Oct 04 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Sun Sep 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-9
- fix classicmenu-logout ("Leave...") patch

* Sun Sep 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-8
- support "Leave..." which brings up complete shutdown dialog in classic menu

* Fri Sep 25 2009 Than Ngo <than@redhat.com> - 4.3.1-7
- don't include googlegadgets on RHEL

* Thu Sep 24 2009 Than Ngo <than@redhat.com> - 4.3.1-6
- rhel cleanup

* Wed Sep 23 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.1-5
- fix spontaneous Plasma crashes due to uninitialized vars

* Mon Sep 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-4
- drop PolicyKit 0.9 support (PolicyKit-kde) on F12+/EL

* Sat Sep 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-3
- -python-applet: Provides: plasma-scriptengine-python
- Requires: system-ksplash-theme (f12+,rhel6+)

* Fri Sep 11 2009 Than Ngo <than@redhat.com> - 4.3.1-2
- drop  BR: lm_sensors-devel on s390(x)

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1
- drop Requires: kde-plasma-folderview, rely on comps instead

* Fri Aug 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.3.0-102
- Fix typo

* Thu Aug 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-101
- inflate Release tag, avoiding possible upgrade/obsoletes pain
- -devel: drop Provides: PolicyKit-kde-devel, bump Obsoletes

* Thu Aug 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-12
- PolicyKit-kde subpkg (#519172, #519654)

* Wed Aug 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-11
- Requires: system-backgrounds-kde (f12+)

* Tue Aug 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-10
- Requires: kde-plasma-folderview

* Sun Aug 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-9
- -akonadi: move plasma_engine_calendar here
- drop Requires: kdm (F-12+)

* Wed Aug 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-8
- adjust default-applets patch to not load plasma-networkmanagement

* Tue Aug 18 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.0-7
- move akonadi stuff to subpackage

* Fri Aug 07 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-6
- Requires: oxygen-icon-theme >= 4.3.0

* Tue Aug 04 2009 Than Ngo <than@redhat.com> - 4.3.0-5
- respin

* Mon Aug 03 2009 Than Ngo <than@redhat.com> - 4.3.0-4
- respin

* Mon Aug 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.0-3
- show the remaining time in the battery plasmoid's popup (as in 4.2) (#515166)

* Sat Aug 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-2
- move designer plugins to -libs, fixes
  Multilib conflicts for index.cache.bz2 (#515088)
- tighten -libs deps, using %%{?_isa}
- %%check: desktop-file-validate

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Mon Jul 27 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.98-3
- backport forgotten method impl in Solid from 4.3 branch, r1000715

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Thu Jul 09 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Mon Jul 06 2009 Than Ngo <than@redhat.com> - 4.2.95-7
- plasma-desktop crashes when closing/opening windows (upstream patch)

* Fri Jul 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-6
- add kde-plasma-networkmanagement to the default panel if installed

* Wed Jul 01 2009 Michel Salim <salimma@fedoraproject.org> - 4.2.95-5
- rebuild (google-gadgets)

* Wed Jul 01 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.95-4
- rebuild (libxklavier)

* Mon Jun 29 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.95-3
- omit a few kdm bits from main pkg (#508647)

* Mon Jun 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-2
- port and reapply rootprivs (#434824) patch (#508593)
- fix internal version number (otherwise it mismatches with our file list)

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Thu Jun 18 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-3
- startkde: make MALLOC_CHECK opt-in (default off)

* Fri Jun 12 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-2
- bump Obsoletes: PolicyKit-kde

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Sun May 31 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.85-5
- make default_leonidas.png the default face icon on F11

* Sat May 30 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-4
- -devel:  exclude libkickoff.so, libsystemsettingsview.so
- drop old cmake crud

* Fri May 29 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-3
- omit/revert session-button patch (kde#194506,rh#502953)
- drop unused knotificationitem-1 patch

* Wed May 27 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.85-2
- upgrade path broken (F-11+), Obsoletes: guidance-power-manager (#502892)
- drop < F-10 crud, have_bluez3

* Mon May 11 2009 Than Ngo <than@redhat.com> 4.2.85-1
- 4.2.85
- Obsoletes/Provides: PolicyKit-kde(-devel)

* Wed May 06 2009 Than Ngo <than@redhat.com> - 4.2.3-2
- Requires: oxygen-icon-theme >= 4.2.2
- fix oxygen-cursor-themes noarch'ness

* Sun May 03 2009 Than Ngo <than@redhat.com> - 4.2.3-1
- 4.2.3

* Tue Apr 28 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-5
- #497657 -  kpackagekit/kopete notification misrendering/missing
  buttons with qt-4.5.1

* Wed Apr 22 2009 Than Ngo <than@redhat.com> - 4.2.2-4
- dropp unused BR on libraw1394, it breaks the build on s390(x)

* Sun Apr 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-3
- Calendar standalone plasmoid on Desktop using 100% of CPU (kde#187699)

* Wed Apr 01 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-2
- optimize scriptlets
- drop upstreamed patches

* Mon Mar 30 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Mon Mar 23 2009 Than Ngo <than@redhat.com> - 4.2.1-12
- upstream patch to fix suspending issue

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-11
- Obsoletes: guidance-power-manager (-> powerdevil upgrade path, F-11+)

* Wed Mar 18 2009 Than Ngo <than@redhat.com> - 4.2.1-10
- upstream patch to fix MenuEntryActions created from khotkeys

* Mon Mar 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-9
- kdm subpkg
- -devel: move cmake modules here
- Requires: kdelibs4%%{?_isa} ..
- BR: libutempter-devel (drops need for kwrited helper)

* Thu Mar 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-8
- oxygen-cursor-themes: make noarch (f10+)

* Thu Mar 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-7
- fix quicklauch (kdebug#185585,rh#489769)
- -wallpapers: make noarch (f10+)

* Tue Mar 10 2009 Than Ngo <than@redhat.com> - 4.2.1-6
- fix konsole patch to use invokeTerminal

* Mon Mar  9 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.1-5
- fix pager not displaying desktop numbers (kdebug#184152)

* Mon Mar 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-4
- kde 4.2 update crashes plasma (kdebug#185736)

* Wed Mar 04 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-3
- move designer plugins to main/runtime (#487622)

* Tue Mar 03 2009 Than Ngo <than@redhat.com> - 4.2.1-2
- respin

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Thu Feb 26 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.0-17
- kio_sysinfo kick-off integration

* Tue Feb 24 2009 Jaroslav Reznik <jreznik@redhat.com> - 4.2.0-16
- no klipper action on selection for Arora browser

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-15
- Provides: service(graphical-login) = kdm

* Fri Feb 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-14
- Requires: oxygen-icon-theme >= %%version

* Thu Feb 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-13
- dpms issues (kdebug#177123)

* Wed Feb 18 2009 Than Ngo <than@redhat.com> - 4.2.0-12
- drop the BR on PyKDE4, it's just needed for runtime
- python-applet subpackage

* Tue Feb 17 2009 Than Ngo <than@redhat.com> - 4.2.0-11
- googlegadgets subpackage

* Mon Feb 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-10
- fix shutdown dialog not centered, sometimes entirely off screen (kde#181199)

* Wed Feb 11 2009 Than Ngo <than@redhat.com> - 4.2.0-9
- fix kdm crash with Qt-4.5

* Mon Feb 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-8
- kickoff logout shuts down system (#484737, kdebug#180576)

* Sun Feb 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-7
- include awol rss dataengine, BR: kdepimlibs-devel (see also kdebug#179050)

* Fri Jan 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4.2
- respin default_applets patch for kpowersave too (#483163)

* Thu Jan 29 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-4.1
- conditionalize bluetooth backport on F10+
- F9: revert solid-bluetooth to the version from KDE 4.1.4

* Thu Jan 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4
- omit ldap hack (#457638), kde42's reduced linkage to the rescue

* Thu Jan 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-3
- Requires: PyKDE4 (for plasmascript bits)
- solid-bluetoothTrunkTo42.diff (bug #481801), and
  +Provides: solid-bluetooth(-devel) = 4.3

* Wed Jan 28 2009 Than Ngo <than@redhat.com> - 4.2.0-2
- readd the patch that omist battery applet when guidance-power-manager is installed

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Fri Jan 16 2009 Than Ngo <than@redhat.com> - 4.1.96-4
- backport fix from trunk to allow symlinks in wallpaper theme

* Wed Jan 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.1.96-3
- BR: google-gadgets-devel > 0.10.5

* Fri Jan 09 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- remove Provides: plasma-devel

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Tue Dec 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-7
- Obsoletes: kpowersave (kpowersave -> powerdevil upgrade path, F-11+)

* Mon Dec 22 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-6
- (re)enable edje, google-gadget support

* Thu Dec 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.85-5
- drop BR edje-devel, we need QEdje instead, which we don't have yet
- comment out BR google-gadgets-* for now, need 0.10.4, have 0.10.3

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-4
- BR: edje-devel
- BR: google-gadgets-devel

* Tue Dec 16 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-3
- respun tarball

* Fri Dec 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-2
- BR: PyKDE4-devel >= %%version

* Thu Dec 11 2008 Than Ngo <than@redhat.com> -  4.1.85-1
- 4.2beta2

* Wed Dec 10 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.82-1
- 4.1.82
- rebase redhat-startkde patch

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-12
- move libplasma_applet-system-monitor.so from -devel to -libs (not a symlink)

* Fri Dec 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-11
- drop devel symlink (parallel -devel) hacks, not needed anymore in this package

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-10
- keep libtaskmanager.so in libdir

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-9
- keep libweather_ion.so in libdir

* Tue Dec 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-8
- keep libplasmaclock.so in libdir

* Mon Dec 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-7
- rebuild for Python 2.6

* Thu Nov 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-6
- disable Logitech mouse KCM again until #399931 is fixed

* Thu Nov 27 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-5
- use python_sitearch for x86_64 systems
- kephal seems to be disabled/removed, re-adapted file lists

* Tue Nov 25 2008 Than Ngo <than@redhat.com> 4.1.80-4
- respin

* Sun Nov 23 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-3
- rebase kdebase-workspace-4.1.1-show-systemsettings.patch
- new library: Kephal -> adapt file lists

* Wed Nov 19 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged
- drop kdebase-workspace-4.1.2-kdm-i18n.patch, it's included in upstream
- drop kdebase-workspace-4.0.85-plasma-default-wallpaper.patch, it's included in upstream
- drop kdebase-workspace-4.1.65-consolekit-kdm.patch
- add kdebase-workspace-4.1.80-session-button.patch
- add kdebase-workspace-4.1.2-ldap.patch

* Wed Nov 19 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 4.1.80-1
- 4.1.80
- BR cmake >= 2.6.2
- make install/fast
- drop _default_patch_fuzz 2
- rebase startkde patch
- rebase plasma-konsole patch
- rebase ck-shutdown patch
- add PyKDE4-devel, python-devel and PyQt4-devel to build plasma's python
  scripting interface
- BR google-gadgets-devel for google gadgets scriptengine
- BR libusb-devel for Logitech USB support in KControl

* Thu Nov 13 2008 Than Ngo <than@redhat.com> 4.1.3-5
- apply upstream patch to fix X crash when disabling compositing

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Fri Nov 07 2008 Than Ngo <than@redhat.com> 4.1.2-14
- only omit battery applet when guidance-power-manager is installed

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-13
- omit battery applet from default panel

* Wed Nov 05 2008 Than Ngo <than@redhat.com> 4.1.2-12
- fix i18n issue in kdm

* Tue Nov 04 2008 Than Ngo <than@redhat.com> 4.1.2-11
- add workaround for ldap issue (#457638)

* Sun Nov 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-10
- never touch PATH in startkde, prepending $QTDIR/bin is unnecessary on Fedora
  and breaks locating Qt 3 Assistant and other Qt 3 stuff (startkde gets run
  with a full path by KDM)

* Sat Nov 01 2008 Than Ngo <than@redhat.com> 4.1.2-9
- previous session button should be enabled

* Fri Oct 31 2008 Than Ngo <than@redhat.com> 4.1.2-8
- apply patch to fix multihead issue
- bz#469235, use non-blocking QProcess:startDetacted

* Sat Oct 25 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-7
- F10: use KDM default face icon from solar-kde-theme, require it

* Sat Oct 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-6
- reenable panel-autohide-fix-flicker patch
- backport revision 866998 to fix the CPU consumption problem (kde#172549)
- backport panelview.cpp coordinate fixes (revisions 869882, 869925, 870041)
- backport revision 871058 (request config sync when panel controller goes away)

* Fri Oct 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-5
- disable panel-autohide-fix-flicker patch for now, eats CPU

* Thu Oct 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-4
- backport panel autohide from 4.2 / plasma-4.1-openSUSE

* Wed Oct  8 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.2-3
- fix crash when invoking a klipper command for a second time

* Sun Sep 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Mon Sep 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-2
- show KCM icon in rootprivs patch (thanks to Harald Sitter "apachelogger")

* Thu Aug 28 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Mon Aug 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-8
- patch another place where systemsettings was hidden from the menu (#457739)

* Mon Aug 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-7
- enable KWin taskbarthumbnail effect (used by backported tooltip manager)

* Fri Aug 01 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-6
- patch to help krandr issues/crashes (kde#152914)

* Fri Aug 01 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.0-5
- fix 457479: "Run as root" dialog of kdm system settings is shown twice
  (due to activated signal being connected to twice)

* Fri Aug 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-4
- fix KDM configuration using the wrong appsdir for themes (#455623)

* Mon Jul 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-3
- respun tarball

* Sun Jul 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-2
- updated tooltip manager from 4.2 (fixes Plasma crash on theme change, #456820)

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Wed Jul 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-5
- F10+: fix circular kdebase<->kdebase-workspace dependency: don't Obsolete or
  Require kdebase, as kdebase now requires kdebase-workspace, obviating the
  upgrade path hack

* Tue Jul 22 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-4
- oxygen-cursor-themes, -wallpapers subpkgs

* Sat Jul 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-3
- BR soprano-devel (optional dependency of the Plasma Engine Explorer)

* Sat Jul 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-2
- backport Plasma tooltip manager from KDE 4.2 (fixes regression from 4.0)
  WARNING: Adds some new APIs from 4.2 (Plasma::popupPosition, Plasma::viewFor,
           Plasma::ToolTip*), use at your own risk, we have no control to
           guarantee that they will not change!

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Wed Jul 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-8
- fix KDM ConsoleKit patch to use x11-display-device instead of display-device

* Wed Jul 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-7
- fix segfault in KDM ConsoleKit patch (#455562)

* Tue Jul 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-6
- move systemsettings back from System to Settings in the menu

* Mon Jul 14 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-5
- new consolekit-kdm patch using libck-connector, BR ConsoleKit-devel (#430388)

* Mon Jul 14 2008 Rex Dieter <rdieter@fedorproject.org> 4.0.98-4
- install circles kdm theme

* Sun Jul 13 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.98-3
- sync kickoff-suspend patch from F9 (loads ksmserver translations)

* Fri Jul 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-2
- respun tarball (with systray patch)

* Thu Jul 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Wed Jul 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.85-3
- rewrite and reapply plasma-default-wallpaper patch
- (no more separate plasma-default-wallpaper-config part)
- rediff kde#154119 patch one last time

* Wed Jul 09 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-2
- systray icon patch (kde#164786)

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Fri Jun 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.83-2
- port and apply kde#154119/kde#158301 patch for moving icons on panel (#439587)

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Tue Jun 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-2
- +Provides: kdm

* Sat Jun 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Wed Jun 04 2008 Than Ngo <than@redhat.com> 4.0.80-4
- fix #449881, ksysguard OnlyShowIn=KDE

* Tue Jun 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.80-3
- enable NetworkManager support, now compatible with NM 0.7

* Thu May 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.80-2
- BR: libcaptury-devel

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Wed May 21 2008 Than Ngo <than@redhat.com> 4.0.72-4
- fix #447030, hyperlinks do not open correctly in firefox

* Thu May 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.72-3
- ksysguardd subpkg (#426543)
- %%config(noreplace) systemsettingsrc

* Thu May 08 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.72-2
- gtkrc patch (rh#443309, kde#146779)

* Wed May 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-1
- update to 4.0.72
- update file list (Lorenzo Villani)
- port plasma-konsole, ck-shutdown, rootprivs, plasma-default-wallpaper patches
- remove NoDisplay=true in systemsettings onlyshowkde patch (still add
  OnlyShowIn=KDE), rename to show-systemsettings
- drop upstreamed suspend patch
- drop backported kde#155362 and menu-switch patches
- drop rh#443610 patch, "Zoom Out" should be working in 4.1
- disable kde#158301 patch for now (fails to apply, looks hard to port)

* Fri May 02 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-20
- Requires: kdebase , so it doesn't go missing on upgrades from kde3 (#444928)

* Mon Apr 28 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-19
- #444141: Initial wallpaper chooser has "EOS" preselected but wallpaper is "Fedora Waves"

* Sun Apr 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-18
- don't show "Zoom Out" toolbox action (#443610, patch from openSUSE branch)

* Sat Apr 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-17
- allow moving plasmoids on panels (#439587, kde#158301) (upstream patch)

* Fri Apr 18 2008 Than Ngo <than@redhat.com> 4.0.3-16
- fix #442559, Suspend/Hibernate issue on logout

* Tue Apr 15 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-15
- workaround #434824: KDE4 System Settings - No Method To Enter Administrative Mode
- fix #441062: packagekit tools do not show icons correctly on KDE

* Tue Apr 15 2008 Sebastian Vahl <fedora@deadbabylon.de> 4.0.3-13
- update redhat-startkde.patch to match waves background color (#442312)

* Fri Apr 11 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-12
- allow to define a default wallpaper (plasmarc:wallpaper)

* Wed Apr 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-11
- read the default KSplash theme from kde-settings in startkde (#441565)

* Mon Apr 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-7
- own %%{_kde4_appsdir}/kdm/faces and set default user image (#441154)

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-6
- rebuild for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-5
- update file list for _kde4_libexecdir

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-4
- backport context menu switch between Kickoff and simple menu from 4.1

* Sat Mar 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- add support for shutdown/reboot through ConsoleKit >= 0.2.4 (#431817)

* Fri Mar 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- most of the kde#155362 patch has been merged, keep only the config part

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.2-9
- add onlyshowin=KDE for systemsetting

* Thu Mar 13 2008 Than Ngo <than@redhat.com> 4.0.2-8
- backport upstream patch to fix crash in kmenuedit when users
  delete entry and save it

* Wed Mar 12 2008 Than Ngo <than@redhat.com> 4.0.2-7
- apply upstream patch to fix changing wallpaper causes desktop to go white
- apply upstream patch to check whether the to-be-embedded window has been destroyed, (bz#437058)

* Mon Mar 10 2008 Than Ngo <than@redhat.com> 4.0.2-6
- add gestures=false in kde-settings, remove kdebase-workspace-4.0.2-Gestures.patch

* Thu Mar 06 2008 Than Ngo <than@redhat.com> 4.0.2-5
- typo fix

* Tue Mar 04 2008 Than Ngo <than@redhat.com> 4.0.2-4
- disable gestures as default
- add konsole in desktop menu

* Mon Mar 03 2008 Than Ngo <than@redhat.com> 4.0.2-3
- apply upstream patch to fix crash in khotkeys

* Fri Feb 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-2
- drop upstreamed kde#155974 patch
- update kde#155362 patch

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-8
- %%files: don't own %%_kde4_libdir/kde4/plugins (thanks wolfy!)

* Sat Feb 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-7
- omit broken disk space checking hunk from redhat-startkde patch (#426871)

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-6
- revert Conflicts, it matches against Provides from kdelibs3.

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-5
- Conflicts: kdelibs < 6:4 (temporary, to ease upgrade pain)
- -devel: Requires: %%name-libs

* Mon Feb 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-4
- backport enhancement to allow multi-line taskbar from 4.1 (kde#155974)

* Mon Feb 04 2008 Than Ngo <than@redhat.com> 4.0.1-3
- respin

* Fri Feb 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- update kde#155362 (simple menu) patch for 4.0.1 (thanks to Jan Mette)

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-1
- 4.0.1

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-8
- respin (qt4)

* Sat Jan 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-7
- backport simple menu enhancement to show .desktop Name from 4.1 (kde#155362)

* Wed Jan 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-6
- Obsoletes: kdebase < 6:4

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-5
- initial login with white background (#428131, kde#155122)

* Wed Jan 09 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-4
- use upstream systemtray patch (#427442, kde#153193)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-3
- respun tarball
- omit gtk_applet patch (for now, doesn't build)

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-2
- omit plasma-pager patch
- pull upstream patch to workaround gtk applet crasher (#427442)

* Mon Jan 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-1
- update to 4.0.0
- drop upstreamed creategtkrc-gtk212 patch
- update redhat-startkde and consolekit-kdm patches

* Mon Dec 31 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.97.0-5
- fix createGtkrc to set tooltip colors also for GTK+ 2.12+

* Sun Dec 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-4
- Obsoletes: kdmtheme

* Mon Dec 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-3
- Requires: coreutils dbus-x11 xorg-x11-apps xorg-x11-utils
            xorg-x11-server-utils (used in startkde)
- drop pam configs that were previously moved to kde-settings

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-2
- rebuild for changed _kde4_includedir

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraprojec.torg. 3.97.0-1
- kde-3.97.0
- move pam configs to kde-settings
- Requires: kde-settings-kdm

* Tue Dec 04 2007 Than Ngo <than@redhat.com> 3.96.2-3
- fix kdm/kcheckpass/kscreensaver to get working

* Sat Dec 01 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.2-2
- BR: dbus-devel
- crystalsvg icons are not part of kdebase-workspace anymore
- make sure libkdeinit_plasma.so is in normal package

* Sat Dec 01 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.2-1
- kde-3.96.2

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.1-4
- Obsoletes and Provides kdebase-kdm for upgrades from old kde-redhat

* Fri Nov 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.1-3
- update and apply redhat-startkde patch
- update and apply KDM ConsoleKit patch (#228111, kde#147790)
- ConsoleKit patch also includes xdmcp fixes from Mandriva (#243560)

* Wed Nov 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.1-2
- %%doc README COPYING
- -libs subpkg
- -libs: Requires: kdelibs4
- don't remove libplasma.so from %%{_kde4_libdir}
- %%files: use %%_datadir for dbus-1/interfaces,xsessions

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.1-1
- kde-3.96.1

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-7
- use kde.desktop from /usr/share/apps/kdm/sessions/kde.desktop
- use %%config(noreplace) for /etc/ksysguarddrc
- Requires: kdebase, kdebase-runtime, oxygen-icon-theme
- fix url

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-6
- add patch to get pager in plasma bar
- re-added BR: libraw1394-devel

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-5
- leave libkworkspace.so for kate
- BR: kde-filesystem >= 4

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-4
- BR: libXtst-devel
- BR: libXScrnSaver-devel

* Fri Nov 16 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-3
- own some more directories
- add %%defattr to package devel
- some spec cleanups
- -R: kdepimlibs-devel
- +BR: libXpm-devel
- +BR: glib2-devel (do we really need this?)

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-2
- BR: libXxf86misc-devel
- BR: libXxf86misc-devel
- BR: libXcomposite-devel
- BR: bluez-libs-devel
- BR: libxklavier-devel
- BR: pam-devel
- BR: lm_sensors-devel
- BR: libXdamage-devel
- BR: libXv-devel
- BR: libXres-devel

* Wed Nov 14 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.96.0-1
- kde-3.96.0

* Wed Nov 14 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.95.2-1
- Initial version of kdebase-workspace
