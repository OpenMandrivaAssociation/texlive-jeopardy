# revision 17757
# category Package
# catalog-ctan /macros/latex/contrib/jeopardy
# catalog-date 2010-04-14 18:01:33 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-jeopardy
Version:	1.1a
Release:	12
Summary:	Build a jeopardy game in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jeopardy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jeopardy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jeopardy.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jeopardy.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The jeopardy package allows to build a jeopardy game with
pdfLaTeX. It is based on the jj_game class and exerquiz
package, written by D. P. Story. The author of the game can use
multichoice questions or fill-in questions. The answer for
fill-in questions is either a mathematical formula or text
string (see the documentation of exerquiz and \RespBoxMath and
\RespBoxTxt commands to learn more about the capabilities).
JavaScripts are written to record the score. If the score is
greater than a given value, a hidden string is shown. The user
should use the style with some screen presentation package,
such as web. The package is distributed with some example
games, including both 1- and 2-player games.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jeopardy/jeopardy.cfg
%{_texmfdistdir}/tex/latex/jeopardy/jeopardy.sty
%doc %{_texmfdistdir}/doc/latex/jeopardy/README
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/aleq.jpg
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game1-two.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game1-two.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game1.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game1.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game1a.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game1a.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game2.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game2.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game2a.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game2a.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game3-CZ.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game3-CZ.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game3-oneplayer-CZ.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game3-oneplayer-CZ.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game4.pdf
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/game4.tex
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/joke.jpg
%doc %{_texmfdistdir}/doc/latex/jeopardy/example/picture.jpg
%doc %{_texmfdistdir}/doc/latex/jeopardy/jeopardy.pdf
#- source
%doc %{_texmfdistdir}/source/latex/jeopardy/jeopardy.dtx
%doc %{_texmfdistdir}/source/latex/jeopardy/jeopardy.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 752896
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 718750
- texlive-jeopardy
- texlive-jeopardy
- texlive-jeopardy
- texlive-jeopardy

