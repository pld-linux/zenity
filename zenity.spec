Summary:	The GNOME port of dialog
Summary(pl):	Port dialog dla GNOME
Name:		zenity
Version:	2.5.90
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	5ad1b4fc94b2f8f3921dd7dd7513388d
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.5.90
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade2-devel >= 2.3.0
BuildRequires:	libgnomecanvas-devel >= 2.5.90
BuildRequires:	perl-base
BuildRequires:	popt-devel
BuildRequires:	scrollkeeper
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
%patch0 -p1

mv po/{no,nb}.po

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# zenity-0.1.mo but gnome/help/zenity
%find_lang %{name}-0.1 --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
