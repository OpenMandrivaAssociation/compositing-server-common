%define rname compositing-server
%define name %{rname}-common
%define version 2010.1
%define release %mkrel 2

%define xinit_level 01
%define xinit_name %{xinit_level}%{rname}

Name: %name
Version: %version
Release: %release
Summary: Common tools for compositing servers
Group: System/X11
URL: http://www.mandriva.com
Source0: %{rname}.xinit
Source1: %{rname}.sysconfig
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-root
Requires: glxinfo xauth xdpyinfo
BuildArch: noarch

%description
This package contains tools for compositing servers, such as Xgl and
Xmetisse. This includes X session scripts and configuration files.

%prep
%setup -q -c -T

%install
rm -rf %{buildroot}
install -D -m 0755 %SOURCE0 %{buildroot}%{_sysconfdir}/X11/xinit.d/%{xinit_name}
install -D -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/%{rname}
install -d %{buildroot}%{_datadir}/%{rname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/X11/xinit.d/%{xinit_name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{rname}
%dir %{_datadir}/%{rname}




%changelog
* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.1-2mdv2011.0
+ Revision: 603848
- rebuild

* Wed Apr 07 2010 Frederic Crozat <fcrozat@mandriva.com> 2010.1-1mdv2010.1
+ Revision: 532605
- Disable compositing-server if GNOME-Shell is requested (GNOME3Preview) (Mdv bug #57573)

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 2007-11mdv2010.1
+ Revision: 499978
- requires glxinfo instead of mesa-demos

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2007-10mdv2010.0
+ Revision: 413265
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2007-9mdv2009.1
+ Revision: 350734
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2007-8mdv2009.0
+ Revision: 220509
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2007-7mdv2008.1
+ Revision: 123338
- kill re-definition of %%buildroot on Pixel's request

* Fri Sep 14 2007 Adam Williamson <awilliamson@mandriva.org> 2007-7mdv2008.0
+ Revision: 85770
- rebuild for 2008
- Fedora license policy


* Fri Mar 23 2007 Olivier Blin <oblin@mandriva.com> 2007-6mdv2007.1
+ Revision: 148466
- allow per-user compositing configuration (#29001)

* Fri Dec 15 2006 Olivier Blin <oblin@mandriva.com> 2007-5mdv2007.1
+ Revision: 97386
- bump release
- use SESSION environment variable instead of DESKTOP

* Thu Dec 14 2006 Olivier Blin <oblin@mandriva.com> 2007-4mdv2007.1
+ Revision: 96981
- add more comments in sysconfig file

* Thu Dec 14 2006 Olivier Blin <oblin@mandriva.com> 2007-3mdv2007.1
+ Revision: 96842
- rename COMPOSITING_SERVER_OPTIONS as COMPOSITING_SERVER_ARGS

* Thu Dec 14 2006 Olivier Blin <oblin@mandriva.com> 2007-2mdv2007.1
+ Revision: 96757
- require xdpyinfo
- allow to force compositing server geometry with COMPOSITING_SERVER_FORCE_GEOMETRY
- rename COMPOSITING_SERVER_LATE_INIT as COMPOSITING_SERVER_SPAWNS_WINDOW (and add some doc)
- requires xauth

* Wed Dec 13 2006 Olivier Blin <oblin@mandriva.com> 2007-1mdv2007.1
+ Revision: 96577
- update sysconfig comments
- export COMPOSITING_SERVER_LATE_INIT
- export original X display as COMPOSITING_SERVER_DISPLAY_SRC
- move Xgl xinit.d and sysconfig files in compositing-server-common
- Create compositing-server-common

