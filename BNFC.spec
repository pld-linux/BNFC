Summary:	BNF Converter
Summary(pl.UTF-8):	Konwerter BNF
Name:		BNFC
Version:	2.4.2.0
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://hackage.haskell.org/packages/archive/BNFC/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fda25414352413879bc8f76d0558fcb4
Patch0:		%{name}-ghc72.patch
Patch1:		%{name}-alex3.patch
URL:		http://www.cse.chalmers.se/research/group/Language-technology/BNFC/
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
%setup -q

# undos the source
find -type f -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

%patch0 -p1
%patch1 -p1

%build
runhaskell Setup.lhs configure -v2 --enable-library-profiling \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version}

runhaskell Setup.lhs build
runhaskell Setup.lhs haddock --executables

%install
rm -rf $RPM_BUILD_ROOT

runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
rm -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}-doc/html/bnfc/*
%attr(755,root,root) %{_bindir}/*
