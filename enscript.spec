Summary:	Converts plain ASCII to PostScript
Summary(es):	Convierte texto ASCII a postscript
Summary(pl):	Konwertuje czyste ASCII do PostScriptu
Summary(pt_BR):	Converte texto ASCII para postscript
Name:		enscript
Version:	1.6.4
Release:	0.9
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.iki.fi/mtr/genscript/%{name}-%{version}.tar.gz
# Source0-md5: b5174b59e4a050fb462af5dbf28ebba3
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-am_fixes.patch
Patch2:		%{name}-mail.patch
Patch3:		%{name}-debian.patch
Patch4:		%{name}-info.patch
URL:		http://www.iki.fi/mtr/genscript/
BuildRequires:	autoconf >= 2.57
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
%patch4 -p1

%build
rm -rf missing
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf enscript $RPM_BUILD_ROOT%{_bindir}/nenscript

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO docs/FAQ.html
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
%{_infodir}/*.info*
