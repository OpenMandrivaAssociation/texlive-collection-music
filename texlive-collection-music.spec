# revision 32405
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-music
Epoch:		1
Version:	20140215
Release:	4
Summary:	Music packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-music.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-latex
Requires:	texlive-abc
Requires:	texlive-figbas
Requires:	texlive-gchords
Requires:	texlive-gtrcrd
Requires:	texlive-guitar
Requires:	texlive-guitarchordschemes
Requires:	texlive-harmony
Requires:	texlive-lilyglyphs
Requires:	texlive-m-tx
Requires:	texlive-musixguit
Requires:	texlive-musixtex
Requires:	texlive-musixtex-fonts
Requires:	texlive-pmx
Requires:	texlive-pmxchords
Requires:	texlive-songbook
Requires:	texlive-songs

%description
Music-related fonts and packages.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
