%define module	Gnome2-GConf
%define name	perl-%{module}
%define version 1.043
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Perl module for the gnome2-2.x GConf libraries
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
URL:		http://gtk2-perl.sf.net/
Source:		http://www.cpan.org/modules/by-module/Gnome2/%{module}-%{version}.tar.bz2
Patch0:		Gnome2-GConf-1.000-cfg_src.patch
BuildRequires:	perl-devel
BuildRequires:	libGConf2-devel => 2.4.0
BuildRequires:	perl-Glib => 1.070
BuildRequires:	perl-Gtk2
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig 
Requires:	perl-Glib >= 1.070
Conflicts:	drakxtools < 9.1-15mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides perl access to GNOME-2.x GConf2 libraries.

GConf is a configuration data storage mechanism scheduled to
ship with GNOME 2.0. GConf does work without GNOME however; it
can be used with plain GTK+, Xlib, KDE, or even text mode
applications as well.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 
%patch0 -p0 -b .cfg_src

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{cflags}" GTK2_PERL_CFLAGS="%{cflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc AUTHOR README examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2*
%{perl_vendorarch}/auto/Gnome2


