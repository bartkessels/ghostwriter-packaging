Name:		ghostwriter
Version:	1.5.0
Release:	1%{?dist}
Summary:	Distraction free Markdown editor

License:	GPLv3+
URL:		https://github.com/wereturtle/ghostwriter
Source0:	https://github.com/wereturtle/ghostwriter/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	hunspell-devel
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	qt5-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtmultimedia-devel

Requires:	qt5-qtbase
Requires:	qt5-qtwebkit
Requires:	qt5-qtsvg
Requires:	qt5-qtmultimedia
Requires:	hunspell

%description
ghostwriter is a Windows and Linux text editor for Markdown, which is a plain
text markup format created by John Gruber. For more information about Markdown,
please visit John Gruber’s website at http://www.daringfireball.net.

ghostwriter provides a relaxing, distraction-free writing environment, whether
your masterpiece be that next blog post, your school paper, or your NaNoWriMo
novel.

%global debug_package %{nil}

%prep
%autosetup -p1

%build
qmake-qt5 PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
export INSTALL_ROOT=%{buildroot}
make install

%files
%{_bindir}/ghostwriter
%{_datarootdir}/ghostwriter/*
%{_datarootdir}/appdata/ghostwriter.appdata.xml
%{_datarootdir}/applications/ghostwriter.desktop
%{_datarootdir}/icons/hicolor/*/apps/ghostwriter.*
%{_datarootdir}/pixmaps/*
%{_mandir}/man1/*
%doc COPYING CREDITS.md

%changelog
* Mon Jun 19 2017 Bart Kessels <bartkessels@outlook.com> 1.5.0-1
- Initial packaging
