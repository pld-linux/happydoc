%include	/usr/lib/rpm/macros.python

%define pname HappyDoc
%define ver 2_0_1

Summary:	Tool for extracting documentation from Python source code
Summary(pl):	Narz�dzie do generowania dokumentacji ze �r�de� program�w napisanych w j�zyku Python
Name:		happydoc
Version:	2.0.1
Release:	1
License:	BSD-like
Group:		Development/Tools
Group(cs):	V�vojov� prost�edky/N�stroje
Group(de):	Entwicklung/Tools
Group(es):	Desarrollo/Herramientas
Group(fr):	Development/Outils
Group(ja):	��ȯ/�ġ���
Group(pl):	Programowanie/Narz�dzia
Group(pt):	Desenvolvimento/Ferramentas
Group(ru):	����������/�����������
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
HappyDoc jest narz�dziem do generowania dokumentacji ze �r�de�
program�w napisanych w j�zyku Python. Program ten, w przeciwno�ci do
innych aplikacji tego typu, kt�re musz� uruchomi� modu�, analizuje
struktur� danego modu�u i na jej podstawie tworzy dokumentacj�.
Pozwala to na generowanie dokumentacji dla tych modu��w/program�w,
kt�re musz� by� uruchamiane w odpowiednim �rodowisku.

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
