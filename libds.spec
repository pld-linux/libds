#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Shared Library for Data Structures
Summary(pl.UTF-8):	Współdzielona biblioteka struktur danych
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

%description -l pl.UTF-8
libDS to współdzielona biblioteka dostarczająca funkcje do obsługi
wątków i struktur danych.

%package devel
Summary:	Development files for libds
Summary(pl.UTF-8):	Pliki dla programistów do biblioteki libds
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains development files for the libds library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki dla programistów korzystających z biblioteki
libds.

%package static
Summary:	Static libds library
Summary(pl.UTF-8):	Statyczna biblioteka libds
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static libds library.
 
%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki libds.

%prep
%setup -q
%patch -P0 -p1

# kill old AC_PROG_LIBTOOL
head -n 42 acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static}
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
