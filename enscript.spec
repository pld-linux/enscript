Summary: Converts plain ASCII to PostScript.
Name: enscript
Version: 1.6.1
Release: 8
Copyright: GNU
Group: Applications/Publishing
Source0: ftp://ftp.gnu.org/pub/gnu/enscript-1.6.1.tar.gz
Patch: enscript-1.6.1-config.patch
URL: http://www.ngs.fi/mtr/genscript/index.html
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root
Obsoletes: nenscript

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
#./configure --prefix=/usr --with-media=Letter --sysconfdir=/etc
#CFLAGS="$RPM_OPT_FLAGS" make

%configure --with-media=Letter --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/{de,es,fi,fr,nl,sl}/LC_MESSAGES
make DESTDIR=$RPM_BUILD_ROOT install

# XXX note doubled %% in sed script below.
(cd $RPM_BUILD_ROOT;find .%{_prefix}/share/enscript/*) | \
	sed -e 's,^\.,,' | sed -e 's,*font.map,%%config &,' > share.list

{ cd $RPM_BUILD_ROOT
  strip .%{_prefix}/bin/* || :
  ln .%{_prefix}/bin/enscript .%{_prefix}/bin/nenscript
}


%clean
rm -rf $RPM_BUILD_ROOT

%files -f share.list
%defattr(-,root,root)
%{_prefix}/share/locale/*/LC_MESSAGES/enscript.mo
%{_prefix}/bin/diffpp
%{_prefix}/bin/sliceprint
%{_prefix}/bin/enscript
%{_prefix}/bin/nenscript
%{_prefix}/bin/mkafmmap
%{_prefix}/bin/states
%{_prefix}/bin/over

%{_prefix}/man/man1/*
%config /etc/enscript.cfg

%doc AUTHORS ChangeLog FAQ.html NEWS README README.ESCAPES THANKS TODO 
