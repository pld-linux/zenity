#
# Conditional build:
%bcond_without	webkit		# build without webkit

Summary:	The GNOME port of dialog
Summary(pl.UTF-8):	Port programu dialog dla GNOME
Name:		zenity
Version:	3.32.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/zenity/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	ba2b2a13248773b4ec0fd323d95e6d5a
URL:		https://wiki.gnome.org/Projects/Zenity
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.19.4
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+3-devel >= 3.0.0
%{?with_webkit:BuildRequires:	gtk-webkit4-devel >= 2.8.1}
BuildRequires:	libnotify-devel >= 0.6.1
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	gtk+3 >= 3.0.0
%{?with_webkit:Requires:	gtk-webkit4 >= 2.8.1}
Requires:	libnotify >= 0.6.1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{__enable_disable webkit webkitgtk}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
