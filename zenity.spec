Summary:	The GNOME port of dialog
Summary(pl.UTF-8):	Port dialog dla GNOME
Name:		zenity
Version:	2.16.3
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/zenity/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	773579408f3237b38fa4d18a182c0ca6
URL:		http://freshmeat.net/projects/zenity/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.9
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	libgnomecanvas >= 2.14.0
Conflicts:	gnome-utils < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

%description -l pl.UTF-8
zenity jest kontynuacją programu gdialog, portu dialog dla GNOME.
Umożliwia on wyświetlanie okien dialogowych z linii komend i ze
skryptów powłoki.

%prep
%setup -q

%build
%{__gnome_doc_prepare}
%{__intltoolize}
%{__gnome_doc_common}
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

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}-0.1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
