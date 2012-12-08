Name: 		nautilus-filesharing
Version:	0.6
Release: 	%mkrel 6
Summary: 	Filesharing extension for Nautilus
Group: 		File tools
License: 	GPL
URL:		http://www.mandrivalinux.com/
Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	mdk-menu-messages
Requires:	drakxtools-newt
BuildRequires:	gtk+2-devel
BuildRequires:	nautilus-devel

%description
This package contains Nautilus extension for filesharing.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.{la,a} \
      %buildroot%{_datadir}/icons/gnome/scalable/emblems/emblem-shared.svg

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%doc AUTHORS COPYING 
%{_libdir}/nautilus/extensions-2.0/*.so




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-4mdv2011.0
+ Revision: 666588
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdv2011.0
+ Revision: 606811
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdv2010.1
+ Revision: 523406
- rebuilt for 2010.1

* Thu Sep 10 2009 Frederic Crozat <fcrozat@mandriva.com> 0.6-1mdv2010.0
+ Revision: 436505
- Release 0.6 :
 - no longer depend on eel / libgnomeui
- requires drakxtools-newt

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5-4mdv2010.0
+ Revision: 428437
- use appropriate BuildRequires:
- add missing BuildRequires:
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 0.5-3mdv2009.1
+ Revision: 365867
- fix building using gnomeui

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2009.0
+ Revision: 223333
- rebuild

* Fri Mar 28 2008 Frederic Crozat <fcrozat@mandriva.com> 0.5-1mdv2008.1
+ Revision: 190956
- Release 0.5
 - fix running fileshareset (Mdv bug #39499)
 - fix invalid unref

* Fri Feb 29 2008 Frederic Crozat <fcrozat@mandriva.com> 0.4-1mdv2008.1
+ Revision: 176697
- Release 0.4 : use new api from glib 2.15.6

* Mon Jan 28 2008 Frederic Crozat <fcrozat@mandriva.com> 0.3-1mdv2008.1
+ Revision: 159383
- Release 0.3 : port to gio and clean UI

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Frederic Crozat <fcrozat@mandriva.com> 0.2-3mdv2008.0
+ Revision: 81809
- Bump release

* Wed Aug 15 2007 Götz Waschk <waschk@mandriva.org> 0.2-2mdv2008.0
+ Revision: 63636
- remove icon that is now in nautilus


* Thu Jul 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.2-2mdv2007.0
- Rebuild with latest libgail

* Wed Apr 26 2006 Frederic Crozat <fcrozat@mandriva.com> 0.2-1mdk
- Release 0.2 : fix build with eel >= 2.14.x

* Mon Jan 10 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.1-1mdk 
- Initial package

