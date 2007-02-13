
%define		pname HappyDoc
%define		ver 2_1

Summary:	Tool for extracting documentation from Python source code
Summary(pl.UTF-8):	Narzędzie do generowania dokumentacji ze źródeł programów napisanych w języku Python
Name:		happydoc
Version:	%(echo %ver | sed 's/_/./g')
Release:	3
License:	BSD-like
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/happydoc/%{pname}_r%{ver}.tar.gz
# Source0-md5:	7791988bb7498d4281636ab5f5852e67
URL:		http://happydoc.sourceforge.net/
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HappyDoc is a tool for extracting documentation from Python source
code. It differs from other such applications by the fact that it uses
the parse tree for a module to derive the information used in its
output, rather that importing the module directly. This allows the
user to generate documentation for modules which need special context
to be imported.

%description -l pl.UTF-8
HappyDoc jest narzędziem do generowania dokumentacji ze źródeł
programów napisanych w języku Python. Program ten, w przeciwności do
innych aplikacji tego typu, które muszą uruchomić moduł, analizuje
strukturę danego modułu i na jej podstawie tworzy dokumentację.
Pozwala to na generowanie dokumentacji dla tych modułów/programów,
które muszą być uruchamiane w odpowiednim środowisku.

%prep
%setup  -q -n %{pname}-r%{ver}

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH
python ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt srcdocs/*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/happydoclib
