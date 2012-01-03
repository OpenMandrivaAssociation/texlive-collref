# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/collref
# catalog-date 2009-11-09 14:16:05 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-collref
Version:	2.0
Release:	2
Summary:	Collect blocks of references into a single reference
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package automatically collects multiple \bibitem
references, which always appear in the same sequence in \cite,
into a single \bibitem block.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/collref/collref.sty
%doc %{_texmfdistdir}/doc/latex/collref/README
%doc %{_texmfdistdir}/doc/latex/collref/collref.pdf
%doc %{_texmfdistdir}/doc/latex/collref/collsamp.tex
#- source
%doc %{_texmfdistdir}/source/latex/collref/collref.dtx
%doc %{_texmfdistdir}/source/latex/collref/collref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
