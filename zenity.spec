Summary:	The GNOME port of dialog
Summary(pl):	Port dialog dla GNOME
Name:		zenity
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/zenity/1.0/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomecanvas-devel >= 2.2.0
Requires(post):	scrollkeeper
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

%find_lang zenity-0.1

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update

%files -f zenity-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
