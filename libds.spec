Summary:	Shared Library for Data Structures
Summary(pl):	Wspó³dzielona biblioteka struktur danych
Name:		libds
Version:	1.5.3
Release:	1
License:	GPL
Group:		Libraries
#Source0Download: http://yallara.cs.rmit.edu.au/~malsmith/products/libds/
Source0:	http://yallara.cs.rmit.edu.au/~malsmith/C0A00201/libds/%{name}-%{version}.tar.bz2
# Source0-md5:	1f231fa20cfc9cec03b0329a6968c7f2
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
Summary:	Development files for libds
Summary(pl):	Pliki dla programistów do biblioteki libds
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains development files for the libds library.

%description devel -l pl
Ten pakiet zawiera pliki dla programistów korzystaj±cych z biblioteki
libds.

%package static
Summary:	Static libds library
Summary(pl):	Statyczna biblioteka libds
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libds library.
 
%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki libds.

%prep
%setup -q
%patch0 -p1

# kill old AC_PROG_LIBTOOL
head -n 42 acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4

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
