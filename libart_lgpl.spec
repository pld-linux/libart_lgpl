Summary:	Library of graphics routines used by libgnomecanvas
Summary(pl):	Biblioteka funkcji graficznych u¿ywanych przez libgnomecanvas
Name:		libart_lgpl
Version:	2.3.11
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libart_lgpl2

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.

%description -l pl
Funkcje graficzne u¿ywane przez widget GnomeCanvas i trochê innych
aplikacji. libart renderuje ¶cie¿ki wektorów i tym podobne.

%package devel
Summary:	Headers for libart_lgpl
Summary(pl):	Pliki nag³owkowe libart_lgpl
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Conflicts:	gnome-libs-devel < 1.4.1.2
Obsoletes:	libart_lgpl2-devel

%description devel
Header files for libart_lgpl.

%description devel -l pl
Pliki nag³ówkowe do biblioteki libart_lgpl.

%package static
Summary:	Static libart_lgpl library
Summary(pl):	Statyczna biblioteka libart_lgpl
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of libart_lgpl library.

%description static -l pl
Statyczna wersja biblioteki libart_lgpl.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libart2-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
