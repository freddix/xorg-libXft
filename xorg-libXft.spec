Summary:	X Font Rendering library
Name:		xorg-libXft
Version:	2.3.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXft-%{version}.tar.bz2
# Source0-md5:	78d64dece560c9e8699199f3faa521c0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xft is a font rendering library for X.

%package devel
Summary:	Header files for libXft library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Xft is a font rendering library for X.

This package contains the header files needed to develop programs that
use libXft.

%prep
%setup -qn libXft-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libXft.so.?
%attr(755,root,root) %{_libdir}/libXft.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXft.so
%{_libdir}/libXft.la
%dir %{_includedir}/X11/Xft
%{_includedir}/X11/Xft/*.h
%{_pkgconfigdir}/xft.pc
%{_mandir}/man3/*.3*

