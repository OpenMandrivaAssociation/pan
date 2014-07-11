%define with_spell 1

%{?_with_spell: %{expand: %%define with_spell 1}}
%{?_without_spell: %{expand: %%define with_spell 0}}

Summary:	A USENET newsreader for GNOME
Name:		pan
Version:	0.137
Release:	8
Epoch:		1
License:	GPLv2+
Group:		Networking/News
Url:		http://pan.rebelbase.com/
Source0:	http://pan.rebelbase.com/download/releases/%{version}/source/%{name}-%{version}.tar.bz2
Patch02:	02_windowsmacosx.dpatch
Patch03:	pan-0.133-fix-str-fmt.patch
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Source4:	%{name}-48.png
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
%if %{with_spell}
BuildRequires:	pkgconfig(gtkspell-2.0)
%endif
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
This is PAN, a powerful and user-friendly USENET newsreader for GNOME.  
The latest info and versions of Pan can always
be found at http://pan.rebelbase.com/.

%prep
%setup -q
%patch02 -p1
%patch03 -p0

%build
%configure2_5x \
%if %{with_spell}
	--with-gtkspell
%else
	--without-gtkspell
%endif

%make

%install
%makeinstall_std Productivitydir=%{_datadir}/applications/

%find_lang %{name}

# Menu
sed -i -e 's/^\(Icon=.*\).png$/\1/g' %{buildroot}%{_datadir}/applications/pan.desktop 

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="GTK" \
	--add-category="News" \
	--add-category="Network" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

#icon
install -d %{buildroot}/%{_iconsdir}
install -d %{buildroot}/%{_liconsdir}
install -d %{buildroot}/%{_miconsdir}
cp -f %{SOURCE2} %{buildroot}/%{_iconsdir}/%{name}.png
cp -f %{SOURCE3} %{buildroot}/%{_miconsdir}/%{name}.png
# png is anti-aliased when put on the gnome panel
cp -f %{SOURCE4} %{buildroot}/%{_liconsdir}/%{name}.png

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

