Summary:	Converts plain ASCII to PostScript.
Name:		enscript
Version:	1.6.1
Release:	8
Copyright:	GNU
Group:		Applications/Publishing
Source:		ftp://ftp.gnu.org/pub/gnu/enscript-1.6.1.tar.gz
Patch:		enscript-1.6.1-config.patch
URL:		http://www.ngs.fi/mtr/genscript/index.html
BuildRoot:	/tmp/%{name}-root
Obsoletes:	nenscript

%description
Enscript is a print filter. It can take ASCII input
and format it into PostScript output. At the same time,
it can also do nice transformations like putting two
ASCII pages on one physical page (side by side) or
changing fonts.

%prep
%setup -q
%patch -p1

%build
%configure --with-media=A4 --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :

ln -s enscript $RPM_BUILD_ROOT%{_bindir}/nenscript

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,README.ESCAPES,THANKS,TODO}.gz FAQ.html
%config(noreplace) /etc/enscript.cfg
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
