Summary:	Shared Library for Data Structures
Summary(pl):	Wspó³dzielone biblioteki stróktur danych
Name:		libds
Version:	1.3.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://yallara.cs.rmit.edu.au/%7Emalsmith/C0A00201/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	5bec4654043863fb5b07d89b9df11f5d
Patch0:		%{name}-makefile.patch
URL:		http://yallara.cs.rmit.edu.au/~malsmith/products/libds/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared Library for Data Structures.

%description -l pl
Wspó³dzielone biblioteki stróktur danych.

%package devel
Summary:	Development files for %{name}
Summary(pl):	Pliki dla programistów do biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

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
rm -fR $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%doc htmldocs/*
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*

%files static
%{_libdir}/*.a
%{_libdir}/*.la
