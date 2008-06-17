Name: 		nautilus-filesharing
Version:	0.5
Release: 	%mkrel 2
Summary: 	Filesharing extension for Nautilus
Group: 		File tools
License: 	GPL
URL:		http://www.mandrivalinux.com/
Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	mdk-menu-messages

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


