Summary: Library of graphics routines used by libgnomecanvas
Name: libart_lgpl
Version: 2.3.8
Release: 1
URL: http://www.gnome.org/
Source0: %{name}-%{version}.tar.gz
License: LGPL
Group: System Environment/Libraries 
BuildRoot: %{_tmppath}/%{name}-root

%description

Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%package devel
Summary: Libraries and headers for libart_lgpl.
Group: Development/Libraries
Requires:	%name = %{version}
Conflicts:      gnome-libs-devel < 1.4.1.2

%description devel

Graphics routines used by the GnomeCanvas widget and some other 
applications. libart renders vector paths and the like.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_bindir}/libart2-config
%{_includedir}/*

%changelog
* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- actually increase version to 2.3.8

* Thu Jan 24 2002 Havoc Pennington <hp@redhat.com>
- upgrade to 2.3.8 so header files don't break eel2

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 2.3.7.91 snap

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- cvs snap, rebuild with new glib

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- 2.3.6

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- new CVS snap with upstream changes merged

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- Initial build.
