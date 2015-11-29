%define plugin_name libsteam
%define dir_name steam-mobile
%define gitrevision 5aef56a958654041c49c74693920f1f9d87ad94b

Name: purple-%{plugin_name}
Version: 1.6.1
Release: 2
Summary: Steam plugin for Pidgin/Adium/libpurple
License: GPLv3
URL: https://github.com/EionRobb/pidgin-opensteamworks
Source0: https://github.com/EionRobb/pidgin-opensteamworks/archive/%{gitrevision}.tar.gz
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: gcc

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Steam protocol.
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: pidgin

%description
Adds support for Steam to Pidgin, Adium, Finch and other libpurple 
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Steam protocol inplemented by steam-mobile.

%prep
%setup -qn pidgin-opensteamworks-%{gitrevision}

# fix W: wrong-file-end-of-line-encoding
perl -i -pe 's/\r\n/\n/gs' README.md

# generating empty configure script
cd %{dir_name}
echo '#!/bin/bash' > configure
chmod +x configure

%build
cd %{dir_name}
%configure
%make_build

%install
cd %{dir_name}
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/%{plugin_name}.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/purple-2/%{plugin_name}.so
%doc README.md

%files -n pidgin-%{plugin_name}
%dir %{_datadir}/pixmaps/pidgin
%dir %{_datadir}/pixmaps/pidgin/protocols
%dir %{_datadir}/pixmaps/pidgin/protocols/16
%{_datadir}/pixmaps/pidgin/protocols/16/steam.png
%dir %{_datadir}/pixmaps/pidgin/protocols/22
%{_datadir}/pixmaps/pidgin/protocols/22/steam.png
%dir %{_datadir}/pixmaps/pidgin/protocols/48
%{_datadir}/pixmaps/pidgin/protocols/48/steam.png

%changelog
* Sun Nov 29 2015 V1TSK <vitaly@easycoding.org> - 1.6.1-2
- Applyed Maxim Orlov's fixes.

* Wed Oct 14 2015 V1TSK <vitaly@easycoding.org> - 1.6.1-1
- Created first RPM spec for Fedora/openSUSE.
