Name:		texlive-collref
Version:	46358
Release:	2
Summary:	Collect blocks of references into a single reference
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
