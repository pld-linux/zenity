#
# Conditional build:
%bcond_without	libnotify	# desktop notification support
%bcond_without	webkit		# WebKitGtk support

Summary:	The GNOME port of dialog
Summary(pl.UTF-8):	Port programu dialog dla GNOME
Name:		zenity
Version:	3.42.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/zenity/3.42/%{name}-%{version}.tar.xz
# Source0-md5:	68314e87a303ad0345cc042443f675a9
URL:		https://wiki.gnome.org/Projects/Zenity
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	glib2-devel >= 1:2.43.4
BuildRequires:	gtk+3-devel >= 3.16.0
%{?with_webkit:BuildRequires:	gtk-webkit4-devel >= 2.8.1}
%{?with_libnotify:BuildRequires:	libnotify-devel >= 0.6.1}
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja >= 1.5
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.43.4
Requires:	gtk+3 >= 3.16.0
%{?with_webkit:Requires:	gtk-webkit4 >= 2.8.1}
%{?with_libnotify:Requires:	libnotify >= 0.6.1}
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
	%{?with_libnotify:-Dlibnotify=true} \
	%{?with_webkit:-Dwebkitgtk=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gdialog
%attr(755,root,root) %{_bindir}/zenity
%{_datadir}/zenity
%{_mandir}/man1/zenity.1*
