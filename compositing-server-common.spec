%define rname compositing-server
%define name %{rname}-common
%define version 2007
%define release %mkrel 9

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
Requires: mesa-demos xauth xdpyinfo
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


