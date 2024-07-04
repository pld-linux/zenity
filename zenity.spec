# TODO: use gtk4-update-icon-cache
#
# Conditional build:
%bcond_without	webkit		# WebKitGtk support

Summary:	The GNOME port of dialog
Summary(pl.UTF-8):	Port programu dialog dla GNOME
Name:		zenity
Version:	4.0.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/zenity/4.0/%{name}-%{version}.tar.xz
# Source0-md5:	08ba19bb3fe5c180402690d5c40c6cc3
URL:		https://wiki.gnome.org/Projects/Zenity
BuildRequires:	gettext-tools >= 0.19.4
%{?with_webkit:BuildRequires:	gtk-webkit6-devel >= 2.40}
BuildRequires:	libadwaita-devel >= 1.2
BuildRequires:	meson >= 0.57.0
BuildRequires:	ninja >= 1.5
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
%{?with_webkit:Requires:	gtk-webkit6 >= 2.40}
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.2
Conflicts:	gnome-utils < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%description -l pl.UTF-8
zenity jest kontynuacją programu gdialog, portu programu dialog dla
GNOME. Umożliwia on wyświetlanie okien dialogowych z linii poleceń i
ze skryptów powłoki.

%prep
%setup -q

%build
%meson build \
	%{?with_webkit:-Dwebkitgtk=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/zenity
%{_desktopdir}/org.gnome.Zenity.desktop
%{_iconsdir}/hicolor/48x48/apps/zenity.png
%{_mandir}/man1/zenity.1*
