Summary:	A USENET newsreader for GNOME
Name:		pan
Version:	0.164
Release:	1
License:	GPLv2+
Group:		Networking/News
Url:		https://pan.rebelbase.com/
Source0:	https://gitlab.gnome.org/GNOME/pan/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gnutls) >= 3.0.0
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0) >= 2.0.16
BuildRequires:  pkgconfig(libnotify) >= 0.4.1
BuildRequires:  pkgconfig(libsecret-1)

%description
This is PAN, a powerful and user-friendly USENET newsreader for GNOME.  
The latest info and versions of Pan can always
be found at http://pan.rebelbase.com/.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%cmake \
		-DBUILD_STATIC_LIBS=OFF \
		-DBUILD_SHARED_LIBS=ON \
  		-DENABLE_MANUAL=ON \
  		-DWANT_GNUTLS=ON \
  		-DWANT_DBUS=ON \
  		-DWANT_GKR=ON \
  		-DWANT_NOTIFY=ON
%make_build

%install
%make_install -C build

%find_lang %{name}


%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%files
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README.org
%{_bindir}/%{name}
%{_datadir}/applications/*.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.%{name}.png
%{_datadir}/metainfo/*.%{name}.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.pan.service
%{_datadir}/pan/

