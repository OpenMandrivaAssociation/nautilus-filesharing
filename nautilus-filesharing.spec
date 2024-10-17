Summary:	Filesharing extension for Nautilus
Name:		nautilus-filesharing
Version:	0.6
Release:	7
Group:		File tools
License:	GPLv2
Url:		https://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libnautilus-extension)
Requires:	drakxtools-newt
Requires:	mdk-menu-messages

%description
This package contains Nautilus extension for filesharing.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

#remove unpackaged files
rm -f %{buildroot}%{_iconsdir}/gnome/scalable/emblems/emblem-shared.svg

%files 
%doc AUTHORS COPYING 
%{_libdir}/nautilus/extensions-2.0/*.so

