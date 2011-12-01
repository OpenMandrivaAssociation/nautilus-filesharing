Name: 		nautilus-filesharing
Version:	0.6
Release: 	%mkrel 4
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
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged files
rm -f %{buildroot}%{_libdir}/nautilus/extensions-2.0/*.{la,a} \
      %buildroot%{_datadir}/icons/gnome/scalable/emblems/emblem-shared.svg

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc AUTHORS COPYING 
%{_libdir}/nautilus/extensions-2.0/*.so


