Summary:	The GNOME port of dialog
Summary(pl):	Port dialog dla GNOME
Name:		zenity
Version:	1.3
Release:	3
License:	GPL
Group:		X11/Applications
# Source0-md5:	b7a0770fd2b9cd6e37480049bafc749c
Source0:	http://ftp.gnome.org/pub/GNOME/sources/zenity/1.3/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomecanvas-devel >= 2.2.0
Requires(post):	scrollkeeper
Conflicts:	gnome-utils < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%description -l pl
zenity jest kontynuacj� programu gdialog, portu dialog dla GNOME.
Umo�liwia on wy�wietlanie okien dialogowych z linii komend i ze
skrypt�w pow�oki.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang zenity-0.1

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update

%files -f zenity-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/zenity
%attr(755,root,root) %{_bindir}/gdialog
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
