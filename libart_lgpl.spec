#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library of graphics routines used by libgnomecanvas
Summary(pl.UTF-8):	Biblioteka funkcji graficznych używanych przez libgnomecanvas
Name:		libart_lgpl
Version:	2.3.21
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libart_lgpl/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	08559ff3c67fd95d57b0c5e91a6b4302
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool
Obsoletes:	libart_lgpl2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.

%description -l pl.UTF-8
Funkcje graficzne używane przez widget GnomeCanvas i trochę innych
aplikacji. libart renderuje ścieżki wektorów i tym podobne.

%package devel
Summary:	Headers for libart_lgpl
Summary(pl.UTF-8):	Pliki nagłowkowe libart_lgpl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libart_lgpl2-devel
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
Header files for libart_lgpl.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki libart_lgpl.

%package static
Summary:	Static libart_lgpl library
Summary(pl.UTF-8):	Statyczna biblioteka libart_lgpl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of libart_lgpl library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libart_lgpl.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libart_lgpl_2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libart_lgpl_2.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libart2-config
%attr(755,root,root) %{_libdir}/libart_lgpl_2.so
%{_libdir}/libart_lgpl_2.la
%{_includedir}/libart-2.0
%{_pkgconfigdir}/libart-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libart_lgpl_2.a
%endif
