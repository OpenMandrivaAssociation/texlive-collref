%global tl_name collref
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.4
Release:	%{tl_revision}.1
Summary:	Collect blocks of references into a single reference
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/collref
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package automatically collects multiple \bibitem references, which
always appear in the same sequence in \cite, into a single \bibitem
block.

