%include	/usr/lib/rpm/macros.python

%define pname HappyDoc
%define ver 2_0_1

Summary:	Tool for extracting documentation from Python source code
Summary(pl):	Narzêdzie do generowania dokumentacji ze ¼róde³ programów napisanych w jêzyku Python
Name:		happydoc
Version:	2.0.1
Release:	1
License:	BSD-like
Group:		Development/Tools
Group(cs):	Vývojové prostøedky/Nástroje
Group(de):	Entwicklung/Tools
Group(es):	Desarrollo/Herramientas
Group(fr):	Development/Outils
Group(ja):	³«È¯/¥Ä¡¼¥ë
Group(pl):	Programowanie/Narzêdzia
Group(pt):	Desenvolvimento/Ferramentas
Group(ru):	òÁÚÒÁÂÏÔËÁ/éÎÓÔÒÕÍÅÎÔÙ
Source0:	http://prdownloads.sourceforge.net/happydoc/%{pname}_r%{ver}.tar.gz
Patch0:		%{name}-pluginloader.patch
Patch1:		%{name}-fix.patch
URL:		http://happydoc.sourceforge.net
BuildRequires:	rpm-pythonprov >= 4.0.2-50
%requires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HappyDoc is a tool for extracting documentation from Python source
code. It differs from other such applications by the fact that it uses
the parse tree for a module to derive the information used in its
output, rather that importing the module directly. This allows the
user to generate documentation for modules which need special context
to be imported.

%description -l pl
HappyDoc jest narzêdziem do generowania dokumentacji ze ¼róde³
programów napisanych w jêzyku Python. Program ten, w przeciwno¶ci do
innych aplikacji tego typu, które musz± uruchomiæ modu³, analizuje
strukturê danego modu³u i na jej podstawie tworzy dokumentacjê.
Pozwala to na generowanie dokumentacji dla tych modu³ów/programów,
które musz± byæ uruchamiane w odpowiednim ¶rodowisku.

%prep
%setup  -q -n %{pname}-r%{ver}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH
python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py | xargs rm -f

gzip -9nf *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz srcdocs/*
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/happydoclib
