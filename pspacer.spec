%define kver %(uname -r)
Summary: PSPacer: Precise Software Pacer
Name: pspacer
Version: 2.2.1
Release: 1
Group: Applications/System
Source: %{name}-%{version}.tar.gz
License: GNU GPL
Packager: Takano Ryousei <takano-ryousei@aist.go.jp>
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: iproute kernel-devel
Requires(post): /sbin/depmod

%{!?configure_options: %define configure_options %{nil}}

%description
PSPacer (Precise Software Pacer) is a qdisc module which realizes
precise transmission bandwidth control. It makes bursty traffic which is
often generated by TCP smooth without any special hardware.
This package consists of a Qdisc kernel module and a user-level library
for the tc (8) command.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
./configure %{configure_options}
make

%install
mkdir -p $RPM_BUILD_ROOT/lib/modules/%{kver}/kernel/net/sched
install -m 0644 kernel/sch_psp.ko $RPM_BUILD_ROOT/lib/modules/%{kver}/kernel/net/sched
mkdir -p $RPM_BUILD_ROOT/usr/lib/tc
install -m 0644 tc/q_psp.so $RPM_BUILD_ROOT/usr/lib/tc
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 0755 pspd/pspd $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0644 man/man8/tc-psp.8 $RPM_BUILD_ROOT/usr/share/man/man8
mkdir -p $RPM_BUILD_ROOT/etc/init.d
install -m 0755 scripts/init.d/pspd $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/pspd
install -m 0755 scripts/sysconfig/add $RPM_BUILD_ROOT/etc/sysconfig/pspd
install -m 0755 scripts/sysconfig/del $RPM_BUILD_ROOT/etc/sysconfig/pspd

%post
/sbin/depmod -ae

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.ja ChangeLog LICENSE
%{_mandir}/man8/*
/usr/lib/tc/q_psp.so
/usr/sbin/pspd
/lib/modules/%{kver}/kernel/net/sched/sch_psp.ko
/etc/init.d/pspd
/etc/sysconfig/pspd/*

%changelog
* Mon Feb 19 2007 Takano Ryousei <takano-ryousei@aist.go.jp>
- add a configure script.
* Mon Nov 14 2005 Takano Ryousei <takano-ryousei@aist.go.jp>
- add pspd stuff.
* Mon Nov 7 2005 Takano Ryousei <takano-ryousei@aist.go.jp>
- relax dependencies on the build process: Requires, BuildPrereq.
* Sat Jul 22 2005 Takano Ryousei <takano-ryousei@aist.go.jp>
- rename the package name from sch_psp to pspacer.
* Sat Jun 11 2005 Takano Ryousei <takano-ryousei@aist.go.jp>
- first build
