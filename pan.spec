%define with_spell 1

%{?_with_spell: %{expand: %%define with_spell 1}}
%{?_without_spell: %{expand: %%define with_spell 0}}

Summary:	A USENET newsreader for GNOME
Name:		pan
Version:	0.134
Release:	%mkrel 1
Epoch:		1
License:	GPLv2+
Group:		Networking/News
URL:		http://pan.rebelbase.com/
Source0:	http://pan.rebelbase.com/download/releases/%{version}/source/%{name}-%{version}.tar.bz2
Patch02:	02_windowsmacosx.dpatch
Patch03:	pan-0.133-fix-str-fmt.patch
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Source4:	%{name}-48.png

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{with_spell}
BuildRequires:  gtkspell-devel
%endif
BuildRequires:	gtk+2-devel >= 2.0.5
BuildRequires:	gmime-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool

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
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std Productivitydir=%{_datadir}/applications/

%{find_lang} %{name}

# Menu
sed -i -e 's/^\(Icon=.*\).png$/\1/g' %{buildroot}%{_datadir}/applications/pan.desktop 

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="News" \
  --add-category="Network" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icon
install -d %{buildroot}/%{_iconsdir}
install -d %{buildroot}/%{_liconsdir}
install -d %{buildroot}/%{_miconsdir}
cp -f %{SOURCE2} %{buildroot}/%{_iconsdir}/%{name}.png
cp -f %{SOURCE3} %{buildroot}/%{_miconsdir}/%{name}.png
# png is anti-aliased when put on the gnome panel
cp -f %{SOURCE4} %{buildroot}/%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog AUTHORS TODO COPYING 
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}


