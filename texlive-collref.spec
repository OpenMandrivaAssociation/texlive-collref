Name:		texlive-collref
Version:	2.0c
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

%define		_unpackaged_subdirs_terminate_build	0

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
%{_texmfdistdir}/tex/latex/collref
%doc %{_texmfdistdir}/doc/latex/collref
#- source
%doc %{_texmfdistdir}/source/latex/collref

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
