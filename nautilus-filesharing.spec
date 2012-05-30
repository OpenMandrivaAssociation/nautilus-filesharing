Name: 		nautilus-filesharing
Version:	0.6
Release: 	6
Summary: 	Filesharing extension for Nautilus
Group: 		File tools
License: 	GPL
URL:		http://www.mandrivalinux.com/
Source0: 	%{name}-%{version}.tar.gz
Requires:	mdk-menu-messages
Requires:	drakxtools-curses
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
%makeinstall_std

#remove unpackaged files
rm -f %{buildroot}%{_libdir}/nautilus/extensions-2.0/*.{la,a} \
      %buildroot%{_datadir}/icons/gnome/scalable/emblems/emblem-shared.svg

%files 
%doc AUTHORS COPYING 
%{_libdir}/nautilus/extensions-2.0/*.so
