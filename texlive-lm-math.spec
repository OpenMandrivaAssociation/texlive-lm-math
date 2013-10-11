# revision 29044
# category Package
# catalog-ctan /fonts/lm-math
# catalog-date 2013-02-06 18:13:15 +0100
# catalog-license lppl
# catalog-version 1.958
Name:		texlive-lm-math
Version:	1.958
Release:	1
Summary:	OpenType maths fonts for Latin Modern
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lm-math
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lm-math.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lm-math.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Latin Modern Math is a maths companion for the Latin Modern
family of fonts, in OpenType format. For use with LuaLaTeX or
XeLaTeX, support is available from the unicode-math package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/lm-math/latinmodern-math.otf
%doc %{_texmfdistdir}/doc/fonts/lm-math/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/lm-math/INSTALL.txt
%doc %{_texmfdistdir}/doc/fonts/lm-math/MANIFEST-Latin-Modern-Math.txt
%doc %{_texmfdistdir}/doc/fonts/lm-math/README-Latin-Modern-Math.txt
%doc %{_texmfdistdir}/doc/fonts/lm-math/math-test-context.tex
%doc %{_texmfdistdir}/doc/fonts/lm-math/math-test.tex
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-context-latinmodern_math.pdf
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-context-latinmodern_math.tex
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-lualatex-latinmodern_math.pdf
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-lualatex-latinmodern_math.tex
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-word-latinmodern_math.docx
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-word-latinmodern_math.pdf
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-xelatex-latinmodern_math.pdf
%doc %{_texmfdistdir}/doc/fonts/lm-math/test-xelatex-latinmodern_math.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
