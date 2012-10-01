# TODO
# - ruby hiliting from http://neugierig.org/software/ruby/
# - reexamine CVE-2008-5078 (no longer applicable?)
Summary:	Converts plain ASCII to PostScript
Summary(es.UTF-8):	Convierte texto ASCII a postscript
Summary(pl.UTF-8):	Konwertuje czyste ASCII do PostScriptu
Summary(pt_BR.UTF-8):	Converte texto ASCII para postscript
Name:		enscript
Version:	1.6.6
Release:	1
License:	GPL v3+
Group:		Applications/Publishing
Source0:	http://ftp.gnu.org/gnu/enscript/%{name}-%{version}.tar.gz
# Source0-md5:	3acc242b829adacabcaf28533f049afd
Patch0:		%{name}-mail.patch
Patch1:		%{name}-debian.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-php.patch
Patch4:		%{name}-ac.patch
URL:		http://www.gnu.org/software/enscript/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	texinfo
Obsoletes:	nenscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enscript is a print filter. It can take ASCII input and format it into
PostScript output. At the same time, it can also do nice
transformations like putting two ASCII pages on one physical page
(side by side) or changing fonts.

%description -l es.UTF-8
Convierte texto ASCII a postscript.

%description -l pl.UTF-8
Enscript jest filtrem wykorzystywanym przy drukowaniu. Na wejściu
przyjmuje dane ASCII i konwertuje je na PostScript. Potrafi
równocześnie dokonać pewnych użytecznych przekształceń, jak np.
umieszczenie dwóch stron ASCII na jednej stronie fizycznej (obok
siebie) czy zmiana czcionki.

%description -l pt_BR.UTF-8
O enscript é um filtro de impressão. Ele pega texto ascii e o formata
em postscript. Além disto, ele pode também fazer várias
transformações, como por exemplo colocar duas páginas ascii em uma
página física (lado a lado) ou modificar as fontes do texto.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-media=A4 \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf enscript $RPM_BUILD_ROOT%{_bindir}/nenscript

%find_lang %{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO docs/FAQ.html
%config(noreplace) %{_sysconfdir}/enscript.cfg
%attr(755,root,root) %{_bindir}/diffpp
%attr(755,root,root) %{_bindir}/enscript
%attr(755,root,root) %{_bindir}/mkafmmap
%attr(755,root,root) %{_bindir}/nenscript
%attr(755,root,root) %{_bindir}/over
%attr(755,root,root) %{_bindir}/sliceprint
%attr(755,root,root) %{_bindir}/states
%{_datadir}/enscript
%{_mandir}/man1/diffpp.1*
%{_mandir}/man1/enscript.1*
%{_mandir}/man1/sliceprint.1*
%{_mandir}/man1/states.1*
%{_infodir}/enscript.info*
