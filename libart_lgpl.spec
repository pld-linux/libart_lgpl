Summary:	Library of graphics routines used by libgnomecanvas
Summary(pl):	Biblioteka funkcji graficznych u�ywanych przez libgnomecanvas
Name:		libart_lgpl
Version:	2.3.8
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/����������
Group(uk):	X11/��̦�����
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/libart_lgpl/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Graphics routines used by the GnomeCanvas widget and some other
applications. libart renders vector paths and the like.

%description -l pl
Funkcje graficzne u�ywane przez widget GnomeCanvas i troch� innych
aplikacji. libart renderuje �cie�ki wektor�w i tym podobne.

%package devel
Summary:	Headers for libart_lgpl
Summary(pl):	Pliki nag�owkowe libart_lgpl
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}
Conflicts:	gnome-libs-devel < 1.4.1.2

%description devel
Header files for libart_lgpl.

%description devel -l pl
Pliki nag��wkowe do biblioteki libart_lgpl.

%package static
Summary:	Static libart_lgpl library
Summary(pl):	Statyczna biblioteka libart_lgpl
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name}-devel = %{version}
Conflicts:	gnome-libs-static < 1.4.1.2

%description static
Static version of libart_lgpl library.

%description static -l pl
Statyczna wersja biblioteki libart_lgpl.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libart2-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
