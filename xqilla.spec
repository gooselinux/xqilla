Name:           xqilla
Version:        2.2.3
Release:        8%{?dist}
Summary:        XQilla is an XQuery and XPath 2.0 library, built on top of Xerces-C

Group:          System Environment/Libraries
License:        ASL 2.0
URL:            http://xqilla.sourceforge.net/HomePage
Source0:        http://downloads.sourceforge.net/xqilla/XQilla-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  xerces-c-devel >= 3.0.1 
BuildRequires:  doxygen graphviz

%description
XQilla is an XQuery and XPath 2.0 implementation written in C++ and based
on Xerces-C. It implements the DOM 3 XPath API, as well as having it's own
more powerful API. It conforms to the W3C proposed recomendation of XQuery
and XPath 2.0.

%package        devel
Summary:        XQilla is an XQuery and XPath 2.0 library, built on top of Xerces-C
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       xerces-c-devel >= 3.0.1

%description    devel
XQilla is an XQuery and XPath 2.0 implementation written in C++ and based
on Xerces-C. It implements the DOM 3 XPath API, as well as having it's own
more powerful API. It conforms to the W3C proposed recomendation of XQuery
and XPath 2.0.

%package        doc
Summary:        XQilla documentation
Group:          Documentation
BuildArch:      noarch

%description    doc
simple-api and dom3-api documentation for XQilla.

%prep
%setup -qn XQilla-%{version}

%build
%configure \
  --disable-static \
  --with-xerces=%{_prefix}

# Avoid lib64 rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
make docs

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f '{}' ';'

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE
%{_bindir}/xqilla
%{_libdir}/libxqilla.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libxqilla.so
%{_includedir}/xqilla/
%{_includedir}/xqc.h

%files doc
%defattr(-,root,root,-)
%doc docs/dom3-api/ docs/simple-api/


%changelog
* Fri May 14 2010 Kalev Lember <kalev@smartlink.ee> - 2.2.3-8
- Require fully versioned main package for -devel subpackage
- Don't build static library
- Removed library Requires which are automatically picked up by rpm
- Removed spurious BR autoconf automake libtool
- Build -doc subpackage as noarch
- Install documentation with %%doc macro
- Use %%{_prefix} instead of hardcoding /usr
- Use parallel make
- Various other spec file clean ups

* Mon Mar  8 2010 Jonathan Robie <jrobie@localhost.localdomain> - 2.2.3-7
- Removed static library, per Fedora packaging guidelines.

* Mon Feb  8 2010 Jonathan Robie <jrobie@localhost.localdomain> - 2.2.3-6
- Fixed rpath problem detected by rpmlint

* Fri Feb  5 2010 Jonathan Robie <jrobie@localhost.localdomain> - 2.2.3-3
- Move to version 2.2.3, using Xerces 3.0.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Robert Scheck <robert@fedoraproject.org> 2.1.3-0.6
- Added a few #include lines needed to build properly with g++ 4.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan  7 2009 Milan Zazrivec <mzazrivec@redhat.com> 2.1.3-0.4
- fixed requirements for xqilla-devel package

* Tue Dec  2 2008 Milan Zazrivec <mzazrivec@redhat.com 2.1.3-0.3
- fix for bz #473997 - xqilla : Unowned directories

* Fri Aug 29 2008 Milan Zazrivec <mzazrivec@redhat.com> 2.1.3-0.2
- Rebased XQilla to latest upstream version 2.1.3
- Fixed files section in spec (documentation was included twice)

* Fri Feb 29 2008 Milan Zazrivec <mzazrivec@redhat.com> 2.0.0-5
- Create xqilla-doc package for xqilla documentation

* Wed Feb 20 2008 Milan Zazrivec <mzazrivec@redhat.com> - 2.0.0-4
- Fix Requires: value for xqilla-devel

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.0-3
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Milan Zazrivec <mazrivec@redhat.com> 2.0.0-2
- Included Xerces-C 2.8.0 sources
- Add missing #include <cstring> where needed (g++ 4.3 changes)

* Thu Jan 10 2008 Milan Zazrivec <mzazrivec@redhat.com> 2.0.0-1
- Removed src/mapm/mapm_mt.cpp
- Added modified mapm_mt.c, taken from MAPM library ver. 4.9.5
- Added parallel make

* Tue Jan 08 2008 Milan Zazrivec <mzazrivec@redhat.com> 2.0.0-0
- Initial packaging of version 2.0.0
