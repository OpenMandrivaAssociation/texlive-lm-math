%global tl_name lm-math
%global tl_revision 67718

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.959
Release:	%{tl_revision}.1
Summary:	OpenType maths fonts for Latin Modern
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/lm-math
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lm-math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lm-math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Latin Modern Math is a maths companion for the Latin Modern family of
fonts, in OpenType format. For use with LuaLaTeX or XeLaTeX, support is
available from the unicode-math package.

