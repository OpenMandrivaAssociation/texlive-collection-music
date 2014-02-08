# revision 26404
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-music
Epoch:		1
Version:	20120810
Release:	3
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
Requires:	texlive-m-tx
Requires:	texlive-musixguit
Requires:	texlive-musixtex
Requires:	texlive-musixtex-fonts
Requires:	texlive-pmx
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


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120810-1
+ Revision: 813967
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780504
- Update to latest release.
- Import texlive-collection-music
- Import texlive-collection-music

