%define	module	Gnome2-GConf
%define	upstream_version 1.044

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	9

Summary:	Perl module for the gnome2-2.x GConf libraries
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://www.cpan.org/modules/by-module/Gnome2/%{module}-%{upstream_version}.tar.bz2
Patch0:		Gnome2-GConf-1.044-cfg_src.patch

BuildRequires:	pkgconfig(gconf-2.0)
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


%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.44.0-8
+ Revision: 770597
- use pkgconfig() deps
- clean spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.44.0-7mdv2011.0
+ Revision: 555876
- rebuild for perl 5.12

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1.44.0-6mdv2010.1
+ Revision: 515514
- skip test, failing because of some missing gnome server
- rebuild using %%perl_convert_version
- redo patch to make it work again with 0 fuzzyness

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.044-2mdv2008.1
+ Revision: 152090
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 08 2007 Thierry Vignaud <tv@mandriva.org> 1.044-1mdv2008.1
+ Revision: 95742
- new release

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 2mdv2008.0-current
+ Revision: 44608
- rebuild


* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.040-1mdv2007.0
- new release

* Wed Jul 26 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.032-1mdv2007.0
- new release

* Sat Jun 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.031-1mdv2007.0
- New version 1.031

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.030-1mdv2007.0
- new release
- spec cleanup
- rpmbuildupdate aware

* Tue Jan 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.021-1mdk
- new release

* Tue Oct 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.020-1mdk
- new release

* Tue Feb 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.012-1mdk
- new release

* Fri Feb 04 2005 Olivier Blin <oblin@mandrakesoft.com> 1.000-4mdk
- Patch0: allow to specify config source in GConfClient

* Thu Feb 03 2005 Olivier Blin <oblin@mandrakesoft.com> 1.000-3mdk
- rebuild for perl-5.8.6

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.000-2mdk
- rebuild for perl-5.8.5

* Wed Mar 31 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.000-1mdk
- new release

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.42-2mdk
- add examples

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.42-1mdk
- initial release

