%define with_spell 1

%{?_with_spell: %{expand: %%define with_spell 1}}
%{?_without_spell: %{expand: %%define with_spell 0}}

Summary:	A USENET newsreader for GNOME
Name:		pan
Version:	0.132
Release:	%mkrel 5
Epoch:		1
License:	GPLv2+
Group:		Networking/News
URL:		http://pan.rebelbase.com/
Source0:	http://pan.rebelbase.com/download/releases/%{version}/source/%{name}-%{version}.tar.bz2
Patch01:	01_make_group_searches_regexps.dpatch
Patch02:	02_windowsmacosx.dpatch
Patch04:	04_g_assert.dpatch
# (fc) 0.132-4mdv fix decoding large JPEG (Fedora) (GNOME bug #467446)
Patch5:		pan-0.132-decodejpeg.patch
# (fc) 0.132-4mdv fix build with gcc4.3 (GNOME bug #524625)
Patch6:		pan-0.132-gcc43.patch
# (fhimpe) fix for CVE-2008-2363 (Fedora)
# http://www.securityfocus.com/bid/29421/info
Patch7:		pan-0.132-CVE-2008-2363.patch
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Source4:	%{name}-48.png

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{with_spell}
BuildRequires:  gtkspell-devel
%endif
BuildRequires:	gtk+2-devel >= 2.0.5
BuildRequires:	libgmime-devel
BuildRequires:	pcre-devel
BuildRequires:	desktop-file-utils

%description
This is PAN, a powerful and user-friendly USENET newsreader for GNOME.  
The latest info and versions of Pan can always
be found at http://pan.rebelbase.com/.

%prep
%setup -q
%patch01 -p1
%patch02 -p1
%patch04 -p1
%patch5 -p1 -b .decodejpeg
%patch6 -p1 -b .gcc43
%patch7 -p1 -b .CVE-2008-2363

%build

%configure2_5x \
%if %{with_spell}
 --with-gtkspell
%else
 --without-gtkspell
%endif

%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std Productivitydir=%{_datadir}/applications/

%{find_lang} %{name}

# Menu
sed -i -e 's/^\(Icon=.*\).png$/\1/g' $RPM_BUILD_ROOT%{_datadir}/applications/pan.desktop 

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="News" \
  --add-category="Network" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icon
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
install -d $RPM_BUILD_ROOT/%{_miconsdir}
cp -f %{SOURCE2} $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
cp -f %{SOURCE3} $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
# png is anti-aliased when put on the gnome panel
cp -f %{SOURCE4} $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

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
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT


