%define	module	Gnome2-GConf
%define	upstream_version 1.044

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Perl module for the gnome2-2.x GConf libraries
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://www.cpan.org/modules/by-module/Gnome2/%{module}-%{upstream_version}.tar.bz2
Patch0:		Gnome2-GConf-1.044-cfg_src.patch

BuildRequires:	libGConf2-devel => 2.4.0
BuildRequires:	perl(Glib) => 1.070
BuildRequires:	perl(Gtk2)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl-devel

Conflicts:	drakxtools < 9.1-15mdk
Requires:	perl-Glib >= 1.070

%description
This module provides perl access to GNOME-2.x GConf2 libraries.

GConf is a configuration data storage mechanism scheduled to
ship with GNOME 2.0. GConf does work without GNOME however; it
can be used with plain GTK+, Xlib, KDE, or even text mode
applications as well.

%prep
%setup -q -n %{module}-%{upstream_version}
%patch0 -p0 -b .cfg_src

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# this fails, we need to start some gnome thingy, but i don't know which
# one. skipping test for now.
#make test

%install
%makeinstall_std

%files
%doc AUTHOR README examples
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2*
%{perl_vendorarch}/auto/Gnome2
