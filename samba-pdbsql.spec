#
# TODO:
# - don't use samba sources, use some samba-devel packages
#
%define		_samba_ver	3.2.0
Summary:	Samba pdbsql - *SQL passdb backends
Summary(pl.UTF-8):	Samba pdbsql - backendy *SQL dla passdb
Name:		samba-pdbsql
%define	snap	rc1
Version:	0.4
Release:	0.%{snap}.1
Epoch:		2
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/pdbsql/pdbsql_32-%{version}-%{snap}.tar.bz2
# Source0-md5:	235254e18a78ad9395fd8d54aa6f6da7
Source1:	http://www.samba.org/samba/ftp/samba-3.2.5.tar.gz
# Source1-md5: 0f7539e09803ae60a2912e70adf1c747
Patch0:		%{name}-build.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	samba-devel >= %{_samba_ver}
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
Summary(pl.UTF-8):	Wtyczka Samby do przechowywania haseł w bazie MySQL
Group:		Networking/Daemons
Requires:	samba >= 1:%{_samba_ver}

%description -n samba-pdb-mysql
Samba MySQL password database plugin.

%description -n samba-pdb-mysql -l pl.UTF-8
Wtyczka Samby do przechowywania haseł w bazie MySQL.

%package -n samba-pdb-pgsql
Summary:	Samba PostgreSQL password database plugin
Summary(pl.UTF-8):	Wtyczka Samby do przechowywania haseł w bazie PostgreSQL
Group:		Networking/Daemons
Requires:	samba >= 1:%{_samba_ver}

%description -n samba-pdb-pgsql
Samba PostgreSQL password database plugin.

%description -n samba-pdb-pgsql -l pl.UTF-8
Wtyczka Samby do przechowywania haseł w bazie PostgreSQL.

%package -n samba-pdb-multi
Summary:	Samba backend which loads multiple passdb backends
Summary(pl.UTF-8):	Backend Samby wczytujący wiele backendów passdb
Group:		Networking/Daemons
Requires:	samba >= 1:%{_samba_ver}

%description -n samba-pdb-multi
Samba backend which loads multiple passdb backends.

%description -n samba-pdb-multi -l pl.UTF-8
Backend Samby wczytujący wiele backendów passdb.

%prep
%setup -q -n pdbsql_3_2 -a1
%patch -P0 -p1

%build
smbdir=$(ls -1d samba-*)
cd $smbdir/source
%configure
%{__make} proto
cd ../..

mv aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-samba-dir=$(pwd)/$(ls -1d samba-*)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -n samba-pdb-mysql
%defattr(644,root,root,755)
%doc docs/*mysql*
%attr(755,root,root) %{_libdir}/pdb/mysql.so

%files -n samba-pdb-pgsql
%defattr(644,root,root,755)
%doc docs/*pgsql*
%attr(755,root,root) %{_libdir}/pdb/pgsql.so

%files -n samba-pdb-multi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pdb/multi.so
