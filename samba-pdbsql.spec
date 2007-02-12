%define		_samba_ver	3.0.23
Summary:	Samba pdbsql - *SQL passdb backends
Summary(pl.UTF-8):   Samba pdbsql - backendy *SQL dla passdb
Name:		samba-pdbsql
Version:	0.1
Release:	2
Epoch:		2
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/pdbsql/pdbsql-%{version}-samba_%{_samba_ver}.tar.bz2
# Source0-md5:	52b18a8d18eac908d2c06b250c269eb3
Patch0:		%{name}-build.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	samba-devel
URL:		http://pdbsql.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	%{_prefix}/%{_lib}/samba

%description
As of release 3.0.23, support for MySQL and PostgreSQL passdb backends
has been removed from the Samba tree, due to the lack of active
maintainer. We now provide this here as an external module for samba.

%description -l pl.UTF-8
Wraz z wydaniem 3.0.23 backendy MySQL i PostgreSQL dla passdb zostały
usunięte z drzewa Samby ze względu na brak aktywnego maintainera. Ten
pakiet udostępnia je jako zewnętrzne moduły dla pakietu samba.


%package -n samba-pdb-mysql
Summary:	Samba MySQL password database plugin
Summary(pl.UTF-8):   Wtyczka Samby do przechowywania haseł w bazie MySQL
Group:		Networking/Daemons
Requires:	samba >= 1:%{_samba_ver}

%description -n samba-pdb-mysql
Samba MySQL password database plugin.

%description -n samba-pdb-mysql -l pl.UTF-8
Wtyczka Samby do przechowywania haseł w bazie MySQL.

%package -n samba-pdb-pgsql
Summary:	Samba PostgreSQL password database plugin
Summary(pl.UTF-8):   Wtyczka Samby do przechowywania haseł w bazie PostgreSQL
Group:		Networking/Daemons
Requires:	samba >= 1:%{_samba_ver}

%description -n samba-pdb-pgsql
Samba PostgreSQL password database plugin.

%description -n samba-pdb-pgsql -l pl.UTF-8
Wtyczka Samby do przechowywania haseł w bazie PostgreSQL.

%package -n samba-pdb-multi
Summary:	Samba backend which loads multiple passdb backends
Summary(pl.UTF-8):   Backend Samby wczytujący wiele backendów passdb
Group:		Networking/Daemons
Requires:	samba >= 1:%{_samba_ver}

%description -n samba-pdb-multi
Samba backend which loads multiple passdb backends.

%description -n samba-pdb-multi -l pl.UTF-8
Backend Samby wczytujący wiele backendów passdb.

%prep
%setup -q -n pdbsql-%{version}-samba_%{_samba_ver}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-samba-dir=%{_includedir}/samba
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n samba-pdb-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pdb/mysql.so

%files -n samba-pdb-pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pdb/pgsql.so

%files -n samba-pdb-multi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pdb/multi.so
