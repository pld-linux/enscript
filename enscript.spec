Summary:	Converts plain ASCII to PostScript
Summary(es):	Convierte texto ASCII a postscript
Summary(pl):	Konwertuje czyste ASCII do PostScriptu
Summary(pt_BR):	Converte texto ASCII para postscript
Name:		enscript
Version:	1.6.1
Release:	15
License:	GPL
Group:		Applications/Publishing
Group(de):	Applikationen/Publizieren
Group(es):	Aplicaciones/Editoración
Group(pl):	Aplikacje/Publikowanie
Group(pt_BR):	Aplicações/Editoração
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-ac_fixes.patch
Patch2:		%{name}-am_fixes.patch
Patch3:		%{name}-mail.patch
URL:		http://www.iki.fi/~mtr/genscript/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nenscript

%description
Enscript is a print filter. It can take ASCII input and format it into
PostScript output. At the same time, it can also do nice
transformations like putting two ASCII pages on one physical page
(side by side) or changing fonts.

%description -l es
Convierte texto ASCII a postscript.

%description -l pl
Enscript jest filtrem wykorzystywanym przy drukowaniu. Na wej¶ciu
przyjmuje dane ASCII i konwertuje je na PostScript. Potrafi
równocze¶nie dokonaæ pewnych u¿ytecznych przekszta³ceñ, jak np.
umieszczenie dwóch stron ASCII na jednej stronie fizycznej (obok
siebie) czy zmiana czcionki.

%description -l pt_BR
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

%build
rm -rf missing
gettextize --copy --force
aclocal
autoheader
autoconf
automake -a -c
%configure \
	--with-media=A4 \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf enscript $RPM_BUILD_ROOT%{_bindir}/nenscript

gzip -9nf AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz FAQ.html
%config(noreplace) %{_sysconfdir}/enscript.cfg
%attr(755,root,root) %{_bindir}/diffpp
%attr(755,root,root) %{_bindir}/sliceprint
%attr(755,root,root) %{_bindir}/enscript
%attr(755,root,root) %{_bindir}/nenscript
%attr(755,root,root) %{_bindir}/mkafmmap
%attr(755,root,root) %{_bindir}/states
%attr(755,root,root) %{_bindir}/over
%{_datadir}/enscript
%{_mandir}/man1/*
