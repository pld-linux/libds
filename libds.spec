Summary:	Shared Library for Data Structures
Name:		libds
Version:	1.3.1
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://yallara.cs.rmit.edu.au/%7Emalsmith/C0A00201/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	5bec4654043863fb5b07d89b9df11f5d
Patch0:		%{name}-makefile.patch
URL:		http://yallara.cs.rmit.edu.au/~malsmith/products/libds/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared Library for Data Structures

%package devel
Group:		Development/Libraries
Requires:	libds = %{version}
Summary:	Support for developing libds-based applications

%description devel
Support for developing libds-based applications

%prep
%setup -q

%patch -p1

%build
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
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
