Summary:	Converts plain ASCII to PostScript.
Summary(pl):	Konwertuje czyste ASCII do PostScriptu.
Name:		enscript
Version:	1.6.1
Release:	8
License:	GNU
Group:		Applications/Publishing
Group(pl):	Aplikacje/Publikowanie
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		enscript-1.6.1-config.patch
URL:		http://www.ngs.fi/mtr/genscript/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nenscript

%description
Enscript is a print filter. It can take ASCII input and format it into
PostScript output. At the same time, it can also do nice
transformations like putting two ASCII pages on one physical page
(side by side) or changing fonts.

%description
Enscript jest filtrem wykorzystywanym przy drukowaniu. Na wej¶ciu
przyjmuje dane ASCII i konwertuje je na PostScript. Potrafi
równocze¶nie dokonaæ pewnych u¿ytecznych przekszta³ceñ, jak np.
umieszczenie dwóch stron ASCII na jednej stronie fizycznej (obok
siebie) czy zmiana czcionki.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
aclocal
autoconf
%configure \
	--with-media=A4 \
	--sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -s enscript $RPM_BUILD_ROOT%{_bindir}/nenscript

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,README.ESCAPES,THANKS,TODO}.gz FAQ.html
%config(noreplace) %{_sysconfdir}/enscript.cfg
%attr(755,root,root) %{_bindir}/diffpp
%attr(755,root,root) %{_bindir}/sliceprint
%attr(755,root,root) %{_bindir}/enscript
%attr(755,root,root) %{_bindir}/nenscript
%attr(755,root,root) %{_bindir}/mkafmmap
%attr(755,root,root) %{_bindir}/states
%attr(755,root,root) %{_bindir}/over
%dir %{_datadir}/enscript
%{_datadir}/enscript/*
%{_mandir}/man1/*
