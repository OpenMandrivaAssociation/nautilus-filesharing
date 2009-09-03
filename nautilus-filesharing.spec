Name: 		nautilus-filesharing
Version:	0.5
Release: 	%mkrel 4
Summary: 	Filesharing extension for Nautilus
Group: 		File tools
License: 	GPL
URL:		http://www.mandrivalinux.com/
Source0: 	%{name}-%{version}.tar.gz
Patch0:		nautilus-filesharing-0.5-use-gnomeui.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	mdk-menu-messages
BuildRequires:	eel-devel >= 2.14.0
BuildRequires:	glib2-devel >= 2.15.6
BuildRequires:	nautilus-devel
BuildRequires:	libgnome2-devel

%description
This package contains Nautilus extension for filesharing.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
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


