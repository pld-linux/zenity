Summary:	The GNOME port of dialog
Summary(pl):	Port dialog dla GNOME
Name:		zenity
Version:	1.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.7/%{name}-%{version}.tar.bz2
# Source0-md5:	977e88e14e686bd0db23f67db94c8038
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomecanvas-devel >= 2.4.0
Conflicts:	gnome-utils < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%description -l pl
zenity jest kontynuacj± programu gdialog, portu dialog dla GNOME.
Umo¿liwia on wy¶wietlanie okien dialogowych z linii komend i ze
skryptów pow³oki.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# zenity-0.1.mo but gnome/help/zenity
%find_lang zenity-0.1 --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f zenity-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/zenity
%attr(755,root,root) %{_bindir}/gdialog
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
