# revision 25121
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-music
Version:	20120223
Release:	1
Summary:	Music typesetting
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-music.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-abc
Requires:	texlive-figbas
Requires:	texlive-gchords
Requires:	texlive-gtrcrd
Requires:	texlive-guitar
Requires:	texlive-harmony
Requires:	texlive-musixguit
Requires:	texlive-musixtex
Requires:	texlive-musixtex-fonts
Requires:	texlive-songbook
Requires:	texlive-collection-latex

%description
Music-related fonts and packages.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
