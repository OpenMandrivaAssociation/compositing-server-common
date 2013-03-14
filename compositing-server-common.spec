%define rname compositing-server
%define xinit_level 01
%define xinit_name %{xinit_level}%{rname}

Name:		%{rname}-common
Version:	2010.1
Release:	2
Summary:	Common tools for compositing servers
Group:		System/X11
License:	GPLv2+
Url:		http://www.mandriva.com
Source0:	%{rname}.xinit
Source1:	%{rname}.sysconfig
BuildArch:	noarch
Requires:	glxinfo
Requires:	xauth
Requires:	xdpyinfo

%description
This package contains tools for compositing servers, such as Xgl and
Xmetisse. This includes X session scripts and configuration files.

%prep
%setup -q -c -T

%install
install -D -m 0755 %SOURCE0 %{buildroot}%{_sysconfdir}/X11/xinit.d/%{xinit_name}
install -D -m 0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/%{rname}
install -d %{buildroot}%{_datadir}/%{rname}

%files
%{_sysconfdir}/X11/xinit.d/%{xinit_name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{rname}
%dir %{_datadir}/%{rname}

