Summary: Network traffic tracker
Name: jnettop
Version: 0.13.0
Release: 15%{?dist}
Group: Applications/Internet
License: GPLv2+
Source: http://jnettop.kubs.info/dist/jnettop-%{version}.tar.gz
Source1: README.Fedora
URL: http://jnettop.kubs.info/wiki/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%if 0%{?rhel} == 4
BuildRequires: libpcap
%else
BuildRequires: libpcap-devel 
%endif
BuildRequires: ncurses-devel glib2-devel db4-devel


%description
Nettop is visualising active network traffic as top does with processes.
It displays active network streams sorted by bandwidth used. This is
often usable when you want to get a fast grip of what is going on on your
outbound router.

%prep
%setup -q
find . -type d -name CVS |xargs rm -rf

%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure 
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -p -m 644 %{SOURCE1} README.Fedora

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/jnettop
%{_mandir}/man8/jnettop.8.gz
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/jnettop-lookup-nmb
%doc AUTHORS ChangeLog COPYING NEWS README README.UIA .jnettop PORTING README.Fedora

%changelog
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 18 2010 Manuel <lonely wolf> Wolfshant <wolfy@fedoraproject.org> 0.13.0-8
- Rebuild against db4-4.8

* Mon Jan 11 2010 Manuel <lonely wolf> Wolfshant <wolfy@fedoraproject.org> 0.13.0-7
- URL for source file has changed

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Manuel <lonely wolf> Wolfshant <wolfy@fedoraproject.org> 0.13.0-5
- Use disttag in release field

* Mon Apr 27 2009 Manuel <lonely wolf> Wolfshant <wolfy@fedoraproject.org> 0.13.0-4
- Add conditional BR for EL-4 (libpcap instead of libpcap-devel)

* Mon Apr 27 2009 Manuel <lonely wolf> Wolfshant <wolfy@fedoraproject.org> 0.13.0-3
- Add README.Fedora, referencing the bundled config file

* Wed Mar 18 2009 Manuel <lonely wolf> Wolfshant <wolfy@fedoraproject.org> 0.13.0-2
- add missing BRs, fix license tag

* Fri Apr 29 2006 Jakub Skopal <j@kubs.cz> 0.13.0-1
- transition to release 0.13.0, see ChangeLog

* Fri Mar 31 2006 Jakub Skopal <j@kubs.cz> 0.12.0-1
- transition to release 0.12.0, see ChangeLog
- added README.UIA

* Thu Jul 1 2005 Jakub Skopal <j@kubs.cz> 0.11.0-2
- added jnettop-lookup-nmb

* Thu Jun 30 2005 Jakub Skopal <j@kubs.cz> 0.11.0-1
- transition to release 0.11.0, see ChangeLog

* Sat Oct 2 2004 Jakub Skopal <j@kubs.cz> 0.10.1-1
- transition to release 0.10.1, see ChangeLog

* Wed Sep 29 2004 Jakub Skopal <j@kubs.cz> 0.10-1
- manual page is now part of RPM package
- transition to release 0.10, see ChangeLog

* Wed Jul 30 2003 Jakub Skopal <j@kubs.cz> 0.9-1
- transition to release 0.9, see ChangeLog

* Wed Apr 23 2003 Jakub Skopal <j@kubs.cz> 0.8.1-1
- transition to release 0.8.1, see ChangeLog

* Wed Apr 23 2003 Jakub Skopal <j@kubs.cz> 0.8-1
- transition to release 0.8, see ChangeLog

* Tue Oct 16 2002 Jakub Skopal <j@kubs.cz> 0.7-1
- transition to release 0.7, see ChangeLog

* Tue Oct 13 2002 Jakub Skopal <j@kubs.cz> 0.6-1
- transition to release 0.6, see ChangeLog

* Tue Sep 03 2002 Jakub Skopal <j@kubs.cz> 0.5-1
- transition to release 0.5, see ChangeLog

* Mon Sep 02 2002 Jakub Skopal <j@kubs.cz> 0.4-1
- transition to release 0.4, see ChangeLog

* Thu Aug 27 2002 Jakub Skopal <j@kubs.cz> 0.3-1
- transition to release 0.3, see ChangeLog

* Thu Aug 27 2002 Jakub Skopal <j@kubs.cz> 0.2-1
- transition to release 0.2, see ChangeLog

* Thu Aug 22 2002 Jakub Skopal <j@kubs.cz> 0.1-1
- initial release

