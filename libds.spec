Summary:	Shared Library for Data Structures
Summary(pl):	Wspó³dzielona biblioteka struktur danych
Name:		libds
Version:	1.4.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://yallara.cs.rmit.edu.au/%7Emalsmith/C0A00201/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	27dd7ef790e701adbb1666e2b5b3c8aa
Patch0:		%{name}-makefile.patch
URL:		http://yallara.cs.rmit.edu.au/~malsmith/products/libds/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libDS is a shared library to provide some threading routines and data
structures.

%description -l pl
libDS to wspó³dzielona biblioteka dostarczaj±ca funkcje do obs³ugi
w±tków i struktur danych.

%package devel
Summary:	Development files for %{name}
Summary(pl):	Pliki dla programistów do biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
This package contains development files for the %{name} library.

%description devel -l pl
Ten pakiet zawiera pliki dla programistów korzystaj±cych z biblioteki
%{name}.

%package static
Summary:        Static %{name} library
Summary(pl):    Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the static %{name} library.
 
%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki %{name}.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc htmldocs/*
%attr(755,root,root) %{_bindir}/libds-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
