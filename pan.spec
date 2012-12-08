%define with_spell 1

%{?_with_spell: %{expand: %%define with_spell 1}}
%{?_without_spell: %{expand: %%define with_spell 0}}

Summary:	A USENET newsreader for GNOME
Name:		pan
Version:	0.137
Release:	2
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
%if %{with_spell}
BuildRequires:	pkgconfig(gtkspell-2.0)
%endif
BuildRequires:	pkgconfig(gtk+-2.0)
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
%makeinstall_std Productivitydir=%{_datadir}/applications/

%find_lang %{name}

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

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Thu May 03 2012 Götz Waschk <waschk@mandriva.org> 1:0.137-1mdv2012.0
+ Revision: 795315
- update to new version 0.137

* Tue Apr 10 2012 Götz Waschk <waschk@mandriva.org> 1:0.136-1
+ Revision: 790147
- update file list
- spec cleanup
- update to new version 0.136

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 1:0.135-1
+ Revision: 685621
- update to new version 0.135

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.134-2
+ Revision: 666985
- mass rebuild

* Sun Feb 20 2011 Götz Waschk <waschk@mandriva.org> 1:0.134-1
+ Revision: 639065
- update build deps
- new version
- drop patches 1,4
- build against gmime 2.4

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.133-6mdv2011.0
+ Revision: 607068
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.133-5mdv2010.1
+ Revision: 523590
- rebuilt for 2010.1

* Mon Oct 05 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.133-4mdv2010.0
+ Revision: 453948
- rebuild

* Wed Aug 19 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.133-3mdv2010.0
+ Revision: 418067
- add P04 to fix gcc44 build

  + Götz Waschk <waschk@mandriva.org>
    - fix build deps

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1:0.133-2mdv2009.1
+ Revision: 366031
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 1:0.133-1mdv2009.0
+ Revision: 275719
- New version 1.133
- drop patches merge upstream

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1:0.132-6mdv2009.0
+ Revision: 265324
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 04 2008 Frederik Himpe <fhimpe@mandriva.org> 1:0.132-5mdv2009.0
+ Revision: 215080
- Add patch from Fedora fixing CVE-2008-2363

* Mon May 26 2008 Frederic Crozat <fcrozat@mandriva.com> 1:0.132-4mdv2009.0
+ Revision: 211417
- Patch5 (Fedora): fix decoding large JPEG (GNOME bug #467446)
- Patch6 (Duncan): fix build with GCC 4.3 (GNOME bug #524625)

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 1:0.132-3mdv2008.1
+ Revision: 163556
- add ubuntu patches:
  	* search are now using regexp
  	* hide windows/macos from preferences
  	* fix build against latest glib
- drop old menu

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 24 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.132-2mdv2008.0
+ Revision: 92581
- Fix build (icon extension)

* Thu Aug 02 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.132-1mdv2008.0
+ Revision: 58026
- Release 0.132

* Thu May 31 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.131-1mdv2008.0
+ Revision: 33250
- Release 0.131
- Remove patch0, merged upstream

* Mon May 21 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.130-1mdv2008.0
+ Revision: 29247
- Release 0.130
- Patch0 (SVN): fix huge memleak

* Sat May 19 2007 Stefan van der Eijk <stefan@mandriva.org> 1:0.129-1mdv2008.0
+ Revision: 28501
- 0.129

* Mon Apr 23 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.128-1mdv2008.0
+ Revision: 17378
- Release 0.128


* Thu Feb 22 2007 Frederic Crozat <fcrozat@mandriva.com> 0.125-1mdv2007.0
+ Revision: 124371
- Release 0.125

* Tue Feb 13 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.124-1mdv2007.1
+ Revision: 120301
- Release 0.124

* Tue Feb 06 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.123-1mdv2007.1
+ Revision: 116868
- Release 0.123

* Mon Feb 05 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.122-1mdv2007.1
+ Revision: 116292
- Release 0.122

* Mon Jan 22 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.121-1mdv2007.1
+ Revision: 111989
- Release 0.121

* Wed Jan 03 2007 Frederic Crozat <fcrozat@mandriva.com> 1:0.120-1mdv2007.1
+ Revision: 103524
- Release 0.120

* Fri Nov 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.119-1mdv2007.1
+ Revision: 80847
- Release 0.119

* Sat Nov 04 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.118-2mdv2007.1
+ Revision: 76541
- Ensure spellchecking is enabled (and correctly disabled when requested in specfile)

* Fri Nov 03 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.118-1mdv2007.1
+ Revision: 76121
- Release 0.118

* Fri Oct 27 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.117-1mdv2007.1
+ Revision: 73027
- Import pan

* Thu Oct 26 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.117-1mdv2007.1
- Release 0.117

* Mon Oct 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.115-1mdv2007.0
- Release 0.115

* Wed Sep 27 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.114-1mdv2007.0
- Release 0.114

* Sat Sep 23 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.113-1mdv2007.0
- Release 0.113

* Tue Sep 12 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.112-1mdv2007.0
- Release 0.112

* Tue Sep 05 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.111-1mdv2007.0
- Release 0.111

* Tue Aug 22 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.109-1mdv2007.0
- Release 0.109

* Wed Aug 16 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.108-1mdv2007.0
- Release 0.108
- Update Source URL

* Mon Aug 14 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.107-1mdv2007.0
- Release 0.107

* Sat Aug 05 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.106-1mdv2007.0
- Release 0.106
- Fix xdg tag

* Mon Jul 17 2006 Stefan van der Eijk <stefan@mandriva.org> 1:0.103-1mdv2007.0
- New release 0.103

* Sat Jul 01 2006 Stefan van der Eijk <stefan@eijk.nu> 1:0.101-1
- New release 0.101

* Tue May 30 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.99-2mdv2007.0
- really use new menu

* Mon May 29 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.99-1mdv2007.0
- New release 0.99
- Use new menu system

* Mon May 15 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.97-1mdk
- New release 0.97

* Fri May 12 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.96-1mdk
- Release 0.96

* Wed May 03 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.95-1mdk
- New release 0.95

* Mon Apr 24 2006 Pascal Terjan <pterjan@mandriva.org> 1:0.94-1mdk
- 0.94
- Fix sources URL

* Mon Apr 17 2006 Stefan van der Eijk <stefan@eijk.nu> 1:0.93-1mdk
- 0.93
- BuildRequires

* Sat Apr 15 2006 Frederic Crozat <fcrozat@mandriva.com> 1:0.92-1mdk
- Release 0.92 (and no Albert, it wasn't dead ;)
- Remove patches 0, 1 (merged upstream), 2 (no longer relevant)

* Thu Sep 08 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.14.2.91-4mdk
- gcc4 fixes

* Wed Feb 23 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.14.2.91-3mdk 
- Patch0 (CVS): fix header corruption
- Patch1 (CVS): fix group always empty

* Thu Dec 02 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.14.2.91-2mdk
- startupnotify should be true, not yes

