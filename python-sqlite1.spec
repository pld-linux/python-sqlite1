# TODO:
# - not compatible with 2.0 version:
#   file /usr/lib/python2.4/site-packages/_sqlite.so from install of python-sqlite1-1.1.6-0.1 conflicts with file from package python-sqlite-1.1.1-3
#   file /usr/lib/python2.4/site-packages/sqlite/__init__.pyc from install of python-sqlite1-1.1.6-0.1 conflicts with file from package python-sqlite-1.1.1-3
#   file /usr/lib/python2.4/site-packages/sqlite/__init__.pyo from install of python-sqlite1-1.1.6-0.1 conflicts with file from package python-sqlite-1.1.1-3

%define		module	sqlite

Summary:	A DB API v1.0 compatible interface to SQLite
Summary(pl.UTF-8):	Interfejs do SQLite kompatybilny z DB API v1.0
Name:		python-%{module}1
Version:	1.1.7
Release:	6
License:	Free
Group:		Development/Languages/Python
Source0:	http://initd.org/pub/software/pysqlite/releases/1.1/%{version}/pysqlite-%{version}.tar.gz
# Source0-md5:	edbed4ccfdc114754c73081e79163be1
URL:		http://www.pysqlite.org/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	sqlite3-devel
Provides:	python(sqlite)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension module for the SQLite embedded relational
database. It tries to conform to the Python DB-API Spec v2 as far as
possible. One problem is that SQLite returns everything as text. This
is a result of SQLite's internal representation of data, however it
still may be possible to return data in the type specified by the
table definitions.

%description -l pl.UTF-8
Ten pakiet zawiera moduł rozszerzenia dla osadzalnej relacyjnej bazy
danych SQLite. Próbuje on być w zgodzie ze specyfikacją Python DB-API
v2 na tyle, na ile to możliwe. Jednym problemem jest to, że SQLite
zwraca wszystko jako tekst. Jest to wynik wewnętrznej reprezentacji
danych przez SQLite; mimo to nadal jest możliwe zwracanie danych typu
podanego w definicji tabeli.

%prep
%setup -q -n pysqlite

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.py
cp -aR examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc/rest/manual.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
%attr(755,root,root) %{py_sitedir}/_%{module}.so
