Summary:	BNF Converter
Summary(pl.UTF-8):	Konwerter BNF
Name:		BNFC
Version:	2.3
Release:	0.b.2
License:	GPL
Group:		Development/Tools
Source0:	http://www.cs.chalmers.se/~markus/BNFC/%{name}_%{version}b.tgz
# Source0-md5:	1c31e0ef06ed27032a0f50d1b0ea860d
URL:		http://www.cs.chalmers.se/~markus/BNFC/
BuildRequires:	ghc
BuildRequires:	gmp-devel
BuildRequires:	tetex-format-pdflatex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BNF Converter is a compiler construction tool generating
a compiler front-end from a Labelled BNF grammar. It was originally
written to generate Haskell, but starting from version 2.0,
it can also be used for generating Java, C++, and C.

%description -l pl.UTF-8
BNF Converter to narzędzie do tworzenia kompilatorów generujące
frontend kompilatora z gramatyki w postaci Labelled BNF. Pierwotnie
zostało napisane do generowania Haskella, ale począwszy of wersji 2.0
potrafi także generować kod w Javie, C++ i C.

%prep
%setup -q -n %{name}_%{version}b

%build
%{__make}

cd doc
pdflatex LBNF-report.tex

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install bnfc $RPM_BUILD_ROOT%{_bindir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
